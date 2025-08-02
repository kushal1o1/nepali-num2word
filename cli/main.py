"""
Command-line interface for nepali-num2word package.

This module provides the CLI for converting numbers to words in Nepali-style format.
Supports both integer and float inputs with optional language parameter.
"""

import argparse
import sys
import os
from typing import Union

# Add parent directory to path for importing nepali_num2word
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from nepali_num2word import convert_to_words


def parse_number(number_str: str) -> Union[int, float]:
    """
    Parse a number string to int or float.
    
    Args:
        number_str (str): String representation of the number.
    
    Returns:
        Union[int, float]: Parsed number as int or float.
    
    Raises:
        ValueError: If the string cannot be parsed as a number.
    """
    try:
        if '.' in number_str:
            return float(number_str)
        else:
            return int(number_str)
    except ValueError:
        raise ValueError(f"Invalid number format: {number_str}")


def main() -> None:
    """
    Main CLI function for converting numbers to words.
    
    Parses command-line arguments and converts the provided number to words
    using the specified language (English or Nepali).
    """
    parser = argparse.ArgumentParser(
        description='Convert numbers to words in Nepali-style format (crore, lakh, thousand).',
        epilog='Examples:\n'
               '  %(prog)s 120000\n'
               '  %(prog)s 123.45 --lang en\n'
               '  %(prog)s 120000 --lang np',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'number', 
        type=str, 
        help='Number to convert (integer or float)'
    )
    
    parser.add_argument(
        '--lang', 
        choices=['en', 'np'], 
        default='en',
        help='Output language: en (English) or np (Nepali Unicode). Default: en'
    )
    
    args = parser.parse_args()

    try:
        number = parse_number(args.number)
        result = convert_to_words(number, lang=args.lang)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except TypeError as e:
        print(f"Type Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()