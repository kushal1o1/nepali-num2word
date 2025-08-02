"""
Tests for the core functionality of nepali-num2word package.
"""

import pytest
from nepali_num2word import convert_to_words, format_number


class TestConvertToWords:
    """Test cases for convert_to_words function."""
    
    def test_integers(self, sample_integers):
        """Test integer conversion to words."""
        for number, expected in sample_integers:
            result = convert_to_words(number)
            assert result == expected, f"convert_to_words({number}) should return '{expected}', got '{result}'"
    
    def test_decimals(self, sample_decimals):
        """Test decimal conversion to words with currency formatting."""
        for number, expected in sample_decimals:
            result = convert_to_words(number)
            assert result == expected, f"convert_to_words({number}) should return '{expected}', got '{result}'"
    
    def test_language_parameter_english(self):
        """Test language parameter with English."""
        result = convert_to_words(120000, lang='en')
        expected = "one lakh twenty thousand"
        assert result == expected
    
    def test_language_parameter_nepali_fallback(self):
        """Test language parameter with Nepali (should fallback to English for now)."""
        result = convert_to_words(120000, lang='np')
        expected = "one lakh twenty thousand"  # Falls back to English
        assert result == expected
    
    def test_zero_cases(self):
        """Test various zero cases."""
        assert convert_to_words(0) == "zero"
        assert convert_to_words(0.0) == "zero"
    
    def test_single_digit_numbers(self):
        """Test single digit numbers."""
        test_cases = [
            (1, "one"),
            (2, "two"),
            (5, "five"),
            (9, "nine")
        ]
        for number, expected in test_cases:
            assert convert_to_words(number) == expected
    
    def test_teens_numbers(self):
        """Test teen numbers (11-19)."""
        test_cases = [
            (11, "eleven"),
            (12, "twelve"),
            (13, "thirteen"),
            (15, "fifteen"),
            (19, "nineteen")
        ]
        for number, expected in test_cases:
            assert convert_to_words(number) == expected
    
    def test_tens_numbers(self):
        """Test tens numbers (20, 30, etc.)."""
        test_cases = [
            (20, "twenty"),
            (30, "thirty"),
            (50, "fifty"),
            (80, "eighty"),
            (90, "ninety")
        ]
        for number, expected in test_cases:
            assert convert_to_words(number) == expected
    
    def test_compound_tens(self):
        """Test compound tens numbers (21, 32, etc.)."""
        test_cases = [
            (21, "twenty-one"),
            (32, "thirty-two"),
            (45, "forty-five"),
            (67, "sixty-seven"),
            (89, "eighty-nine")
        ]
        for number, expected in test_cases:
            assert convert_to_words(number) == expected
    
    def test_hundreds(self):
        """Test hundreds."""
        test_cases = [
            (100, "one hundred"),
            (200, "two hundred"),
            (500, "five hundred"),
            (900, "nine hundred")
        ]
        for number, expected in test_cases:
            assert convert_to_words(number) == expected
    
    def test_currency_singular_plural(self):
        """Test singular/plural currency formatting."""
        # Single rupee/paisa
        assert convert_to_words(1.0) == "one rupee"
        assert convert_to_words(0.01) == "one paisa"
        assert convert_to_words(1.01) == "one rupee and one paisa"
        
        # Multiple rupees/paise
        assert convert_to_words(2.0) == "two rupees"
        assert convert_to_words(0.02) == "two paise"
        assert convert_to_words(2.02) == "two rupees and two paise"


class TestFormatNumber:
    """Test cases for format_number function."""
    
    def test_format_number_not_implemented(self):
        """Test that format_number is not yet implemented."""
        result = format_number(1000000)
        assert result is None
    
    def test_format_number_various_inputs(self):
        """Test format_number with various inputs (should all return None for now)."""
        test_numbers = [120000, 1000000, 123.45, 0, 1]
        for number in test_numbers:
            result = format_number(number)
            assert result is None


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_large_numbers(self):
        """Test very large numbers."""
        # Test numbers in crores
        assert convert_to_words(10000000) == "one crore"
        assert convert_to_words(99999999) == "nine crore ninety-nine lakh ninety-nine thousand nine hundred ninety-nine"
    
    def test_decimal_precision(self):
        """Test decimal precision handling."""
        # Test that decimals are properly rounded to paise
        assert "forty-five paise" in convert_to_words(123.45)
        assert "fifty paise" in convert_to_words(100.50)
    
    def test_type_consistency(self):
        """Test that function handles both int and float consistently."""
        # Same number as int and float should give same result for integer part
        int_result = convert_to_words(123)
        float_result = convert_to_words(123.0)
        
        assert "one hundred twenty-three" in int_result
        assert "one hundred twenty-three" in float_result
