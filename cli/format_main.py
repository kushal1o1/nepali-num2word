"""
Command-line interface for number formatting with Nepali-style comma separation.

This module provides the CLI for formatting numbers with Nepali-style comma placement.
Currently not implemented - returns None for all inputs.
"""

import argparse
import sys
from typing import Union

from nepali_num2word import format_number


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
    Main CLI function for formatting numbers with Nepali-style commas.
    
    Parses command-line arguments and formats the provided number with
    Nepali-style comma separation.
    
    Note:
        This function is currently not implemented and will output None.
    """
    parser = argparse.ArgumentParser(
        description='Format numbers with Nepali-style comma separation.',
        epilog='Examples:\n'
               '  %(prog)s 1000000  # Output: 10,00,000\n'
               '  %(prog)s 120000   # Output: 1,20,000\n'
               '  %(prog)s 123.45   # Output: 123.45',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'number', 
        type=str, 
        help='Number to format (integer or float)'
    )
    
    args = parser.parse_args()

    try:
        number = parse_number(args.number)
        result = format_number(number)
        
        if result is None:
            print("Format function not yet implemented. Returns None.", file=sys.stderr)
        else:
            print(result)
            
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
