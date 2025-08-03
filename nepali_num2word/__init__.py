"""
nepali-num2word: Convert numbers to Nepali-style words and formatting.

This package provides functionality to convert numbers to words using the 
Nepali numbering system (crore, lakh, thousand) and format numbers with 
Nepali-style comma separation.

Main functions:
    convert_to_words: Convert numbers to words
    format_number: Format numbers with Nepali-style commas
    compact_number: Convert numbers to compact, human-readable format
"""

from .core import convert_to_words, format_number, compact_number

__version__ = "0.2.0"
__author__ = "Kushal"
__email__ = "work.kusal@gmail.com"

__all__ = ['convert_to_words', 'format_number', 'compact_number']

