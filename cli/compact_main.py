"""
Command-line interface for compact number representation.

This module provides the CLI for converting numbers to compact, human-readable format
like "1.2 lakhs", "4.5 crores" etc.
"""

import argparse
import sys
import os
from typing import Union

# Add parent directory to path for importing nepali_num2word
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from nepali_num2word import compact_number


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


def main():
    """
    Main function for the CLI.
    """
    parser = argparse.ArgumentParser(
        description="Convert numbers to compact format (e.g., 1.2 lakhs, 4.5 crores).",
        epilog="""Examples:
  nepalicompact 120000
  nepalicompact 4200000 --lang en
  nepalicompact 42000000 --lang np""",
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
    
    try:
        args = parser.parse_args()
        number = parse_number(args.number)
        result = compact_number(number, lang=args.lang)
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
