"""
Pytest configuration and fixtures for nepali-num2word tests.
"""

import pytest


@pytest.fixture
def sample_integers():
    """Sample integer test cases."""
    return [
        (0, "zero"),
        (5, "five"),
        (15, "fifteen"),
        (25, "twenty-five"),
        (99, "ninety-nine"),
        (100, "one hundred"),
        (101, "one hundred one"),
        (1000, "one thousand"),
        (1001, "one thousand one"),
        (100000, "one lakh"),
        (120000, "one lakh twenty thousand"),
        (100001, "one lakh one"),
        (1000000, "ten lakh"),
        (10000000, "one crore"),
        (10000001, "one crore one"),
        (34000000, "three crore forty lakh"),
    ]


@pytest.fixture
def sample_decimals():
    """Sample decimal test cases with currency formatting."""
    return [
        (0.0, "zero"),
        (0.01, "one paisa"),
        (0.99, "ninety-nine paise"),
        (1.0, "one rupee"),
        (1.01, "one rupee and one paisa"),
        (5.0, "five rupees"),
        (123.0, "one hundred twenty-three rupees"),
        (123.23, "one hundred twenty-three rupees and twenty-three paise"),
        (123.45, "one hundred twenty-three rupees and forty-five paise"),
        (120000.50, "one lakh twenty thousand rupees and fifty paise"),
    ]


@pytest.fixture
def sample_edge_cases():
    """Edge cases for testing."""
    return [
        (1, "one"),
        (11, "eleven"),
        (21, "twenty-one"),
        (100, "one hundred"),
        (1000, "one thousand"),
        (100000, "one lakh"),
        (10000000, "one crore"),
    ]
