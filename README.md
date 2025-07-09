### Dataset Structure
- **Original file**: `asteriod/data/dataset.csv` (~435MB, 958,525 rows)
- **Split chunks**: `asteriod/data/chunks/dataset_part_*.csv` (10 chunks, each <50MB)
- **Content**: Asteroid orbital and physical characteristics data

### Working with the Dataset

#### If you're cloning this repository:
1. Navigate to the `scripts` directory
2. Run the reassembly script:
   ```bash
   # On Windows (PowerShell/Command Prompt)
   cd scripts
   python reassemble_dataset_binary.py
   # Or double-click reassemble_dataset.bat
   
   # On Unix/Linux/Mac
   cd scripts
   python3 reassemble_dataset_binary.py
   ```

Each chunk file includes the CSV header and a portion of the data, making them independently usable for analysis if needed.

### Requirements
- Python 3.6 or higher
- No additional packages required for dataset scripts (uses only built-in modules)

### Git Configuration

**Important**: A `.gitattributes` file has been included to prevent Git from modifying line endings in the dataset chunks. This ensures binary integrity across different operating systems.

If you see Git warnings about "LF will be replaced by CRLF", this is normal and the `.gitattributes` file will handle it properly.

## Project Structure
```
logistic-regression/
├── README.md
├── .gitignore
├── .gitattributes
├── asteriod/
│   └── data/
│       └── chunks/              # Split dataset chunks (10 files)
│           ├── dataset_part_001.csv
│           ├── dataset_part_002.csv
│           ├── ...
│           └── dataset_part_010.csv
└── scripts/
    └── reassemble_dataset_binary.py # Reassemble chunks into original file (binary-safe)
```
