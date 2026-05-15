"""Simple test runner for nepali-num2word package.

Run this to quickly test core functionality without pytest.
"""

import os
import sys

# Add the parent directory to the path so we can import nepali_num2word
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from nepali_num2word import convert_to_words, format_number  # noqa: E402


def test_basic_functionality():
    """Test basic functionality with key examples."""
    print(" Testing Basic Functionality")
    print("=" * 40)

    test_cases = [
        (120000, "one lakh twenty thousand"),
        (123.45, "one hundred twenty-three rupees and forty-five paise"),
        (34000000, "three crore forty lakh"),
        (1.01, "one rupee and one paisa"),
        (0.99, "ninety-nine paise"),
        (0, "zero"),
        (25, "twenty-five"),
        (101, "one hundred one"),
    ]

    passed = 0
    failed = 0

    for number, expected in test_cases:
        result = convert_to_words(number)
        if result == expected:
            print(f" {number} -> {result}")
            passed += 1
        else:
            print(f" {number} -> {result} (expected: {expected})")
            failed += 1

    print(f"\n Results: {passed} passed, {failed} failed")
    return failed == 0


def test_language_parameter():
    """Test language parameter functionality."""
    print("\n Testing Language Parameter")
    print("=" * 40)

    # Test English (default)
    result_en = convert_to_words(120000, lang="en")
    print(f" English: {result_en}")

    # Test Nepali (now implemented)
    result_np = convert_to_words(120000, lang="np")
    print(f" Nepali: {result_np}")

    # Verify they're different (English vs Nepali)
    return result_en == "one lakh twenty thousand" and result_np == "एक लाख बीस हजार"


def test_format_function():
    """Test format_number function."""
    print("\n Testing Format Function")
    print("=" * 40)

    test_cases = [
        (1000000, "10,00,000"),
        (120000, "1,20,000"),
        (123.45, "123.45"),
        (34000000, "3,40,00,000"),
        (100, "100"),
        (0, "0"),
        (-120000, "-1,20,000"),
    ]

    passed = 0
    failed = 0

    for number, expected in test_cases:
        result = format_number(number)
        if result == expected:
            print(f" format_number({number}) -> {result}")
            passed += 1
        else:
            print(f" format_number({number}) -> {result} (expected: {expected})")
            failed += 1

    print(f" Format Tests: {passed} passed, {failed} failed")
    return failed == 0


def main():
    """Run all tests."""
    print("🇳🇵 nepali-num2word Test Runner")
    print("=" * 50)

    all_passed = True

    all_passed &= test_basic_functionality()
    all_passed &= test_language_parameter()
    all_passed &= test_format_function()

    print("\n" + "=" * 50)
    if all_passed:
        print(" All tests passed! :)")
        sys.exit(0)
    else:
        print(" Some tests failed! :)")
        sys.exit(1)


if __name__ == "__main__":
    main()
