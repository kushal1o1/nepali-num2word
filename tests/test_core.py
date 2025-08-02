"""
Tests for the core functionality of nepali-num2word package.
"""

import pytest
from nepali_num2word import convert_to_words, format_number, compact_number


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
        """Test language parameter with Nepali (now implemented)."""
        result = convert_to_words(120000, lang='np')
        expected = "एक लाख बीस हजार"  # Now returns actual Nepali
        assert result == expected
    
    def test_nepali_basic_numbers(self):
        """Test basic Nepali number conversion."""
        test_cases = [
            (9, "नौ"),
            (25, "पच्चिस"),
            (67, "सतसट्ठी"),
            (99, "उनान्सय"),
            (123, "एक सय तेइस"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number, lang='np')
            assert result == expected, f"convert_to_words({number}, lang='np') should return '{expected}', got '{result}'"
    
    def test_nepali_currency(self):
        """Test Nepali currency formatting."""
        test_cases = [
            (123.45, "एक सय तेइस रुपैयाँ र पैँतालीस पैसा"),
            (1.01, "एक रुपैयाँ र एक पैसा"),
            (67.89, "सतसट्ठी रुपैयाँ र उनान्नब्बे पैसा"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number, lang='np')
            assert result == expected, f"convert_to_words({number}, lang='np') should return '{expected}', got '{result}'"
    
    def test_nepali_large_numbers(self):
        """Test Nepali large number conversion."""
        test_cases = [
            (1000, "एक हजार"),
            (10000, "दश हजार"),
            (100000, "एक लाख"),
            (1000000, "दश लाख"),
            (10000000, "एक करोड"),
            (12345678, "एक करोड तेइस लाख पैँतालीस हजार छ सय अठहत्तर"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number, lang='np')
            assert result == expected, f"convert_to_words({number}, lang='np') should return '{expected}', got '{result}'"
    
    def test_nepali_edge_cases(self):
        """Test Nepali edge cases with zeros."""
        test_cases = [
            (1002, "एक हजार दुई"),
            (1020, "एक हजार बीस"),
            (1200, "एक हजार दुई सय"),
            (10002, "दश हजार दुई"),
            (100200, "एक लाख दुई सय"),
            (2030, "दुई हजार तीस"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number, lang='np')
            assert result == expected, f"convert_to_words({number}, lang='np') should return '{expected}', got '{result}'"
    
    def test_nepali_negative_numbers(self):
        """Test Nepali negative number conversion."""
        test_cases = [
            (-123, "-एक सय तेइस"),
            (-1234, "-एक हजार दुई सय चौँतीस"),
            (-123.45, "-एक सय तेइस रुपैयाँ र पैँतालीस पैसा"),
            (-100000, "-एक लाख"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number, lang='np')
            assert result == expected, f"convert_to_words({number}, lang='np') should return '{expected}', got '{result}'"
    
    def test_nepali_zero_cases(self):
        """Test Nepali zero cases."""
        test_cases = [
            (0, "शून्य"),
            (0.0, "शून्य"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number, lang='np')
            assert result == expected, f"convert_to_words({number}, lang='np') should return '{expected}', got '{result}'"
    
    def test_nepali_compound_numbers(self):
        """Test Nepali compound numbers (0-99 direct lookup)."""
        test_cases = [
            (21, "एक्काइस"),
            (33, "तेत्तीस"),
            (45, "पैँतालीस"),
            (67, "सतसट्ठी"),
            (89, "उनान्नब्बे"),
            (99, "उनान्सय"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number, lang='np')
            assert result == expected, f"convert_to_words({number}, lang='np') should return '{expected}', got '{result}'"


class TestNegativeNumbers:
    """Test cases for negative numbers in both languages."""
    
    def test_negative_integers_english(self):
        """Test negative integer conversion in English."""
        test_cases = [
            (-123, "-one hundred twenty-three"),
            (-1000, "-one thousand"),
            (-120000, "-one lakh twenty thousand"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number)
            assert result == expected, f"convert_to_words({number}) should return '{expected}', got '{result}'"
    
    def test_negative_decimals_english(self):
        """Test negative decimal conversion in English."""
        test_cases = [
            (-123.45, "-one hundred twenty-three rupees and forty-five paise"),
            (-1.01, "-one rupee and one paisa"),
        ]
        for number, expected in test_cases:
            result = convert_to_words(number)
            assert result == expected, f"convert_to_words({number}) should return '{expected}', got '{result}'"
    
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
            (14, "fourteen"),
            (15, "fifteen"),
            (16, "sixteen"),
            (17, "seventeen"),
            (18, "eighteen"),
            (19, "nineteen")
        ]
        for number, expected in test_cases:
            assert convert_to_words(number) == expected
    
    def test_tens_numbers(self):
        """Test tens numbers (10, 20, 30, etc.)."""
        test_cases = [
            (10, "ten"),
            (20, "twenty"),
            (30, "thirty"),
            (40, "forty"),
            (50, "fifty"),
            (60, "sixty"),
            (70, "seventy"),
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
    
    def test_format_number_basic_cases(self):
        """Test format_number with basic cases."""
        test_cases = [
            (1000000, "10,00,000"),
            (120000, "1,20,000"),
            (34000000, "3,40,00,000"),
            (1000, "1,000"),
            (100, "100"),
            (10, "10"),
            (0, "0"),
            (99999, "99,999"),
            (100000, "1,00,000"),
            (999999, "9,99,999"),
            (10000000, "1,00,00,000"),
        ]
        
        for number, expected in test_cases:
            result = format_number(number)
            assert result == expected, f"format_number({number}) should return '{expected}', got '{result}'"
    
    def test_format_number_decimals(self):
        """Test format_number with decimal numbers."""
        test_cases = [
            (123.45, "123.45"),
            (123.0, "123"),  # Whole number decimal should format as integer
            (0.45, "0.45"),
            (1000000.50, "10,00,000.5"),
            (120000.123, "1,20,000.123"),
        ]
        
        for number, expected in test_cases:
            result = format_number(number)
            assert result == expected, f"format_number({number}) should return '{expected}', got '{result}'"
    
    def test_format_number_negative(self):
        """Test format_number with negative numbers."""
        test_cases = [
            (-120000, "-1,20,000"),
            (-1000000, "-10,00,000"),
            (-123.45, "-123.45"),
            (-100, "-100"),
        ]
        
        for number, expected in test_cases:
            result = format_number(number)
            assert result == expected, f"format_number({number}) should return '{expected}', got '{result}'"


class TestErrorHandling:
    """Test error handling for invalid inputs."""
    
    def test_none_input(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError, match="Number cannot be None"):
            convert_to_words(None)
    
    def test_boolean_input(self):
        """Test that boolean input raises TypeError."""
        with pytest.raises(TypeError, match="Boolean values are not supported"):
            convert_to_words(True)
        
        with pytest.raises(TypeError, match="Boolean values are not supported"):
            convert_to_words(False)
    
    def test_invalid_string_input(self):
        """Test that invalid string input raises ValueError."""
        with pytest.raises(ValueError, match="'hello' is not a valid number"):
            convert_to_words("hello")
        
        with pytest.raises(ValueError, match="'123abc' is not a valid number"):
            convert_to_words("123abc")
    
    def test_empty_string_input(self):
        """Test that empty string input raises ValueError."""
        with pytest.raises(ValueError, match="Empty string is not a valid number"):
            convert_to_words("")
        
        with pytest.raises(ValueError, match="Empty string is not a valid number"):
            convert_to_words("   ")  # whitespace only
    
    def test_unsupported_type_input(self):
        """Test that unsupported types raise TypeError."""
        with pytest.raises(TypeError, match="Unsupported type: list"):
            convert_to_words([])
        
        with pytest.raises(TypeError, match="Unsupported type: dict"):
            convert_to_words({})
        
        with pytest.raises(TypeError, match="Unsupported type: set"):
            convert_to_words(set())
    
    def test_large_number_input(self):
        """Test that numbers too large raise ValueError."""
        with pytest.raises(ValueError, match="Number 1000000000 is too large"):
            convert_to_words(1000000000)
        
        with pytest.raises(ValueError, match="too large"):
            convert_to_words(-1000000000)
    
    def test_valid_string_numbers(self):
        """Test that valid string numbers work correctly."""
        assert convert_to_words("123") == "one hundred twenty-three"
        assert convert_to_words("123.45") == "one hundred twenty-three rupees and forty-five paise"
        assert convert_to_words("-123") == "-one hundred twenty-three"
        assert convert_to_words("0") == "zero"
        assert convert_to_words("0.0") == "zero"


class TestCompactNumber:
    """Test cases for compact_number function."""
    
    def test_basic_numbers(self):
        """Test basic number compacting in English."""
        test_cases = [
            (0, "0"),
            (999, "999"),
            (1000, "1 thousand"),
            (1500, "1.5 thousand"),
            (10000, "10 thousand"),
            (50000, "50 thousand"),
            (99000, "99 thousand"),
        ]
        for number, expected in test_cases:
            result = compact_number(number)
            assert result == expected, f"compact_number({number}) should return '{expected}', got '{result}'"
    
    def test_lakhs(self):
        """Test lakh compacting in English."""
        test_cases = [
            (100000, "1 lakh"),
            (150000, "1.5 lakhs"),
            (500000, "5 lakhs"),
            (1000000, "10 lakhs"),
            (4200000, "42 lakhs"),
            (9900000, "99 lakhs"),
        ]
        for number, expected in test_cases:
            result = compact_number(number)
            assert result == expected, f"compact_number({number}) should return '{expected}', got '{result}'"
    
    def test_crores(self):
        """Test crore compacting in English."""
        test_cases = [
            (10000000, "1 crore"),
            (42000000, "4.2 crores"),
            (100000000, "10 crores"),
            (500000000, "50 crores"),
        ]
        for number, expected in test_cases:
            result = compact_number(number)
            assert result == expected, f"compact_number({number}) should return '{expected}', got '{result}'"
    
    def test_auto_trim_decimals(self):
        """Test auto-trimming of .0 decimals."""
        test_cases = [
            (4000000, "40 lakhs"),  # 40.0 lakhs -> 40 lakhs
            (10000000, "1 crore"),   # 1.0 crore -> 1 crore
            (50000000, "5 crores"),  # 5.0 crores -> 5 crores
        ]
        for number, expected in test_cases:
            result = compact_number(number)
            assert result == expected, f"compact_number({number}) should return '{expected}', got '{result}'"
    
    def test_nepali_language(self):
        """Test compact number in Nepali language."""
        test_cases = [
            (999, "९९९"),
            (1500, "१.५ हजार"),
            (100000, "१ लाख"),
            (150000, "१.५ लाख"),
            (4200000, "४२ लाख"),
            (42000000, "४.२ करोड"),
            (100000000, "१० करोड"),
        ]
        for number, expected in test_cases:
            result = compact_number(number, lang='np')
            assert result == expected, f"compact_number({number}, lang='np') should return '{expected}', got '{result}'"
    
    def test_negative_numbers(self):
        """Test compact number with negative values."""
        test_cases = [
            (-999, "-999"),
            (-1500, "-1.5 thousand"),
            (-100000, "-1 lakh"),
            (-4200000, "-42 lakhs"),
            (-42000000, "-4.2 crores"),
        ]
        for number, expected in test_cases:
            result = compact_number(number)
            assert result == expected, f"compact_number({number}) should return '{expected}', got '{result}'"
    
    def test_precision_parameter(self):
        """Test custom precision parameter."""
        test_cases = [
            (4230000, 0, "42 lakhs"),    # 0 precision
            (4230000, 1, "42.3 lakhs"),  # 1 precision (default)
            (4230000, 2, "42.3 lakhs"),  # 2 precision (auto-trim)
            (4235000, 2, "42.35 lakhs"), # 2 precision with actual decimals
        ]
        for number, precision, expected in test_cases:
            result = compact_number(number, precision=precision)
            assert result == expected, f"compact_number({number}, precision={precision}) should return '{expected}', got '{result}'"
    
    def test_string_inputs(self):
        """Test valid string number inputs."""
        test_cases = [
            ("100000", "1 lakh"),
            ("1500", "1.5 thousand"),
            ("42000000", "4.2 crores"),
        ]
        for number_str, expected in test_cases:
            result = compact_number(number_str)
            assert result == expected, f"compact_number('{number_str}') should return '{expected}', got '{result}'"
    
    def test_singular_plural(self):
        """Test singular vs plural forms in English."""
        test_cases = [
            (1000, "1 thousand"),     # singular
            (2000, "2 thousand"),     # plural (no 's' for thousand)
            (100000, "1 lakh"),       # singular
            (200000, "2 lakhs"),      # plural
            (10000000, "1 crore"),    # singular
            (20000000, "2 crores"),   # plural
        ]
        for number, expected in test_cases:
            result = compact_number(number)
            assert result == expected, f"compact_number({number}) should return '{expected}', got '{result}'"


class TestCompactNumberErrors:
    """Test error handling for compact_number function."""
    
    def test_invalid_types(self):
        """Test error handling for invalid input types."""
        with pytest.raises(TypeError, match="Number cannot be None"):
            compact_number(None)
        
        with pytest.raises(TypeError, match="Boolean values are not supported"):
            compact_number(True)
        
        with pytest.raises(TypeError, match="Unsupported type: list"):
            compact_number([])
    
    def test_invalid_strings(self):
        """Test error handling for invalid string inputs."""
        with pytest.raises(ValueError, match="Empty string is not a valid number"):
            compact_number("")
        
        with pytest.raises(ValueError, match="'hello' is not a valid number"):
            compact_number("hello")
    
    def test_large_numbers(self):
        """Test error handling for numbers too large."""
        with pytest.raises(ValueError, match="Number 1000000000 is too large"):
            compact_number(1000000000)


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
