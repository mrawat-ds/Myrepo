# PDF Combiner

A simple Python script to combine multiple PDF files into a single PDF.

## Installation

1. Install the required dependency:
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install pypdf
```

## Usage

Basic syntax:
```bash
python combine_pdfs.py file1.pdf file2.pdf file3.pdf -o output.pdf
```

### Examples

Combine specific files:
```bash
python combine_pdfs.py report1.pdf report2.pdf report3.pdf -o combined_report.pdf
```

Combine all PDFs in current directory:
```bash
python combine_pdfs.py *.pdf -o all_combined.pdf
```

Combine PDFs matching a pattern:
```bash
python combine_pdfs.py chapter*.pdf -o book.pdf
```

## Features

- Combines multiple PDF files in the order specified
- Validates input files (checks if they exist and are PDFs)
- Simple command-line interface
- Clear progress messages
- Error handling for missing files

## Requirements

- Python 3.6+
- pypdf library

## Notes

- PDFs are combined in the order they are specified on the command line
- If a file is not found or is not a PDF, a warning is displayed and the file is skipped
- The output file will automatically have a `.pdf` extension added if not provided
