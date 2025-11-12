#!/usr/bin/env python3
"""
PDF Combiner - Merge multiple PDF files into a single PDF

Usage:
    python combine_pdfs.py file1.pdf file2.pdf file3.pdf -o output.pdf
    python combine_pdfs.py *.pdf -o combined.pdf
"""

import argparse
import sys
from pathlib import Path

try:
    from pypdf import PdfMerger
except ImportError:
    print("Error: pypdf library not found.")
    print("Please install it using: pip install pypdf")
    sys.exit(1)


def combine_pdfs(input_files, output_file):
    """
    Combine multiple PDF files into a single PDF.

    Args:
        input_files: List of input PDF file paths
        output_file: Output PDF file path
    """
    merger = PdfMerger()

    try:
        print(f"Combining {len(input_files)} PDF files...")

        for pdf_file in input_files:
            pdf_path = Path(pdf_file)

            if not pdf_path.exists():
                print(f"Warning: File not found: {pdf_file}")
                continue

            if not pdf_path.suffix.lower() == '.pdf':
                print(f"Warning: Skipping non-PDF file: {pdf_file}")
                continue

            print(f"  Adding: {pdf_file}")
            merger.append(str(pdf_path))

        # Write the combined PDF
        print(f"\nWriting combined PDF to: {output_file}")
        merger.write(output_file)
        merger.close()

        print(f"✓ Successfully combined PDFs into {output_file}")
        return True

    except Exception as e:
        print(f"Error combining PDFs: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Combine multiple PDF files into a single PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s file1.pdf file2.pdf file3.pdf -o output.pdf
  %(prog)s *.pdf -o combined.pdf
  %(prog)s document*.pdf -o merged_documents.pdf
        """
    )

    parser.add_argument(
        'input_files',
        nargs='+',
        help='Input PDF files to combine'
    )

    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output PDF file name'
    )

    args = parser.parse_args()

    # Ensure output has .pdf extension
    output_file = args.output
    if not output_file.lower().endswith('.pdf'):
        output_file += '.pdf'

    # Combine PDFs
    success = combine_pdfs(args.input_files, output_file)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
