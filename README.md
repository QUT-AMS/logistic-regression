<<<<<<< HEAD
### Dataset Structure

This repository contains 4 different datasets for logistic regression projects:

#### 1. Asteroid Dataset (Requires Reassembly)
- **Original file**: `asteriod/data/dataset.csv` (~435MB, 958,525 rows)
- **Split chunks**: `asteriod/data/chunks/dataset_part_*.csv` (22 chunks, each <50MB)
- **Content**: Asteroid orbital and physical characteristics data
- **Status**: Split into chunks, needs reassembly

#### 2. Fake News Detection Dataset (Requires Reassembly)
- **Original file**: `fakeNewsDetection/data/dataset.csv`
- **Split chunks**: `fakeNewsDetection/data/chunks/dataset_part_*.csv` (2 chunks)
- **Content**: News articles with labels for fake news detection
- **Status**: Split into chunks, needs reassembly

#### 3. Bank Loan Approval Dataset (Ready to Use)
- **File**: `bankLoanApproval/data/dataset.csv`
- **Content**: Bank loan application data for approval prediction
- **Status**: Complete dataset, ready for analysis

#### 4. Heart Disease Prediction Dataset (Ready to Use)
- **File**: `heartDiseasePrediction/data/dataset.csv`
- **Content**: Medical data for heart disease prediction
- **Status**: Complete dataset, ready for analysis

### Working with the Datasets

#### For Datasets that Need Reassembly (Asteroid & Fake News Detection):
If you're cloning this repository, you'll need to reassemble the split datasets:
=======
### Working with the Datasets
>>>>>>> 0dbe8e9799b8d83782b641cfbaff699c4c346196

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

<<<<<<< HEAD
This will create:
- `asteriod/data/dataset.csv` from the chunks in `asteriod/data/chunks/`
- `fakeNewsDetection/data/dataset.csv` from the chunks in `fakeNewsDetection/data/chunks/`

#### For Ready-to-Use Datasets (Bank Loan Approval & Heart Disease Prediction):
These datasets are already complete and can be used directly:
- `bankLoanApproval/data/dataset.csv`
- `heartDiseasePrediction/data/dataset.csv`

#### If you're contributing and need to split a large dataset:
1. Place your large `dataset.csv` in the appropriate dataset directory (e.g., `asteriod/data/` or `fakeNewsDetection/data/`)
2. Navigate to the `scripts` directory
3. Run the splitting script:
   ```bash
   # On Windows (PowerShell/Command Prompt)
   cd scripts
   python split_dataset_binary.py
   # Or double-click split_dataset.bat
   
   # On Unix/Linux/Mac
   cd scripts
   python3 split_dataset_binary.py
   ```

#### Files created by splitting:
- For asteroid dataset: `asteriod/data/chunks/dataset_part_001.csv` through `dataset_part_022.csv`
- For fake news dataset: `fakeNewsDetection/data/chunks/dataset_part_001.csv` through `dataset_part_002.csv`

=======
>>>>>>> 0dbe8e9799b8d83782b641cfbaff699c4c346196
Each chunk file includes the CSV header and a portion of the data, making them independently usable for analysis if needed.

### Requirements
- Python 3.6 or higher
- No additional packages required for dataset scripts (uses only built-in modules)

### Git Configuration

**Important**: A `.gitattributes` file has been included to prevent Git from modifying line endings in the dataset chunks. This ensures binary integrity across different operating systems.

If you see Git warnings about "LF will be replaced by CRLF", this is normal and the `.gitattributes` file will handle it properly.

## Current Structure
```
logistic-regression/
├── README.md
├── .gitignore
├── .gitattributes
├── asteriod/
│   └── data/
<<<<<<< HEAD
│       └── chunks/              # Split dataset chunks (22 files)
│           ├── dataset_part_001.csv
│           ├── dataset_part_002.csv
│           ├── ...
│           └── dataset_part_022.csv
├── fakeNewsDetection/
│   └── data/
│       └── chunks/              # Split dataset chunks (2 files)
│           ├── dataset_part_001.csv
│           └── dataset_part_002.csv
├── bankLoanApproval/
│   └── data/
│       └── dataset.csv          # Complete dataset (ready to use)
├── heartDiseasePrediction/
│   └── data/
│       └── dataset.csv          # Complete dataset (ready to use)
=======
│       └── chunks/              # Split dataset chunks
│           ├── dataset_part_001.csv
│           ├── dataset_part_002.csv
│           ├── ...
│           └── dataset_part_***.csv
>>>>>>> 0dbe8e9799b8d83782b641cfbaff699c4c346196
└── scripts/
    ├── reassemble_dataset_binary.py # Reassemble chunks into original files
    └── split_dataset_binary.py      # Split large datasets into chunks
```
<<<<<<< HEAD

## Getting Started

1. Clone this repository
2. **For datasets that need reassembly** (asteroid and fake news detection):
   - Follow the reassembly instructions above to create the complete dataset files
3. **For ready-to-use datasets** (bank loan approval and heart disease prediction):
   - You can start using them immediately
4. Install required Python packages for logistic regression:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
=======
>>>>>>> 0dbe8e9799b8d83782b641cfbaff699c4c346196
