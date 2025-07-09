#!/usr/bin/env python3
"""
Binary file reassembler that ensures perfect reproduction of the original file.
"""

import os
import glob

def reassemble_file_binary(chunks_dir, output_file):
    """
    Reassemble binary chunks back into a single file.
    
    Args:
        chunks_dir (str): Directory containing the chunk files
        output_file (str): Path for the reassembled output file
    """
    # Find all chunk files
    chunk_pattern = os.path.join(chunks_dir, "dataset_part_*.csv")
    chunk_files = sorted(glob.glob(chunk_pattern))
    
    if not chunk_files:
        print(f"Error: No chunk files found in {chunks_dir}")
        return False
    
    print(f"Found {len(chunk_files)} chunk files:")
    for chunk_file in chunk_files:
        size_mb = os.path.getsize(chunk_file) / (1024 * 1024)
        print(f"  {os.path.basename(chunk_file)}: {size_mb:.2f} MB")
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    print(f"\nReassembling to: {output_file}")
    
    header_written = False
    total_bytes = 0
    
    with open(output_file, 'wb') as outfile:
        for i, chunk_file in enumerate(chunk_files, 1):
            print(f"Processing chunk {i}/{len(chunk_files)}: {os.path.basename(chunk_file)}")
            
            with open(chunk_file, 'rb') as infile:
                data = infile.read()
                
                if not data:
                    continue
                
                if not header_written:
                    # For the first chunk, write everything
                    outfile.write(data)
                    header_written = True
                    total_bytes += len(data)
                    print(f"  Added {len(data):,} bytes (including header)")
                else:
                    # For subsequent chunks, skip the header
                    # Find the first newline (end of header)
                    header_end = 0
                    while header_end < len(data) and data[header_end:header_end+1] not in (b'\n', b'\r'):
                        header_end += 1
                    if header_end < len(data):
                        # Include the newline character(s)
                        if (data[header_end:header_end+1] == b'\r' and 
                            header_end + 1 < len(data) and 
                            data[header_end+1:header_end+2] == b'\n'):
                            header_end += 2  # CRLF
                        else:
                            header_end += 1  # LF
                    
                    # Write only the data part (skip header)
                    data_part = data[header_end:]
                    outfile.write(data_part)
                    total_bytes += len(data_part)
                    print(f"  Added {len(data_part):,} bytes (data only)")
    
    # Get final file size
    final_size = os.path.getsize(output_file)
    final_size_mb = final_size / (1024 * 1024)
    
    print(f"\nReassembly complete!")
    print(f"Total bytes written: {total_bytes:,}")
    print(f"Final file size: {final_size:,} bytes ({final_size_mb:.2f} MB)")
    print(f"Output file: {output_file}")
    
    return True

if __name__ == "__main__":
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    chunks_dir = os.path.join(project_root, "asteriod", "data", "chunks")
    output_file = os.path.join(project_root, "asteriod", "data", "dataset_reassembled_binary.csv")
    
    # Check if chunks directory exists
    if not os.path.exists(chunks_dir):
        print(f"Error: Chunks directory not found: {chunks_dir}")
        print("Please run split_dataset_binary.py first to create the chunks.")
        exit(1)
    
    # Reassemble the file
    reassemble_file_binary(chunks_dir, output_file)
