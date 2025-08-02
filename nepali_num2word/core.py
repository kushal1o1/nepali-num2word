"""
Core module for nepali-num2word package.

This module provides functions to convert numbers to words in Nepali-style format
and format numbers with Nepali-style comma separation.
"""

# Basic number words mapping (0-19)
ONES = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
    'seventeen', 'eighteen', 'nineteen'
]

# Tens (20, 30, 40, etc.)
TENS = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]


def convert_to_words(number, lang='en'):
    """
    Convert a number to words in Nepali-style format (crore, lakh, thousand).
    
    Args:
        number (int or float): The number to convert to words.
                              Can be integer or float.
        lang (str, optional): Language for output. 'en' for English, 'np' for Nepali.
                              Defaults to 'en'. Currently only 'en' is implemented.
    
    Returns:
        str: The number converted to words.
             For integers: "one lakh twenty thousand"
             For floats: "one hundred twenty-three rupees and forty-five paise"
    
    Examples:
        >>> convert_to_words(120000)
        'one lakh twenty thousand'
        >>> convert_to_words(123.45)
        'one hundred twenty-three rupees and forty-five paise'
        >>> convert_to_words(120000, lang='np')
        'one lakh twenty thousand'  # Falls back to English for now
    """
    # For now, only English is implemented
    if lang == 'np':
        # TODO: Implement Nepali Unicode support
        pass
        # For now, fallback to English
    
    # Handle decimal numbers (rupees and paise)
    if isinstance(number, float) or '.' in str(number):
        if isinstance(number, str):
            number = float(number)
        
        integer_part = int(number)
        decimal_part = round((number - integer_part) * 100)
        
        if integer_part == 0 and decimal_part == 0:
            return 'zero'
        
        result_parts = []
        
        if integer_part > 0:
            rupees_word = convert_integer_to_words(integer_part)
            if integer_part == 1:
                result_parts.append(f"{rupees_word} rupee")
            else:
                result_parts.append(f"{rupees_word} rupees")
        
        if decimal_part > 0:
            paise_word = convert_integer_to_words(decimal_part)
            if decimal_part == 1:
                result_parts.append(f"{paise_word} paisa")
            else:
                result_parts.append(f"{paise_word} paise")
        
        if len(result_parts) == 2:
            return f"{result_parts[0]} and {result_parts[1]}"
        else:
            return result_parts[0] if result_parts else 'zero'
    
    # Handle integer numbers
    return convert_integer_to_words(number)

def convert_integer_to_words(number):
    """
    Convert an integer to words in Nepali-style format (crore, lakh, thousand).
    
    Args:
        number (int): The integer to convert to words.
    
    Returns:
        str: The integer converted to words using Nepali-style grouping.
    
    Examples:
        >>> convert_integer_to_words(120000)
        'one lakh twenty thousand'
        >>> convert_integer_to_words(34000000)
        'three crore forty lakh'
    """
    if number == 0:
        return 'zero'
    
    result = []
    
    # Handle crores (10,000,000)
    if number >= 10000000:
        crores = number // 10000000
        result.append(f"{basic_number_to_words(crores)} crore")
        number = number % 10000000
    
    # Handle lakhs (100,000)
    if number >= 100000:
        lakhs = number // 100000
        result.append(f"{basic_number_to_words(lakhs)} lakh")
        number = number % 100000
    
    # Handle thousands (1,000)
    if number >= 1000:
        thousands = number // 1000
        result.append(f"{basic_number_to_words(thousands)} thousand")
        number = number % 1000
    
    # Handle hundreds (100)
    if number >= 100:
        hundreds = number // 100
        result.append(f"{basic_number_to_words(hundreds)} hundred")
        number = number % 100
    
    # Handle remaining (1-99)
    if number > 0:
        result.append(basic_number_to_words(number))
    
    return ' '.join(result)

def basic_number_to_words(number):
    """
    Convert basic numbers (1-99) to words.
    
    Args:
        number (int): The number to convert (should be between 0-99).
    
    Returns:
        str: The number converted to words.
    
    Examples:
        >>> basic_number_to_words(25)
        'twenty-five'
        >>> basic_number_to_words(15)
        'fifteen'
        >>> basic_number_to_words(90)
        'ninety'
    """
    if number < 20:
        return ONES[number]
    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        if ones_digit == 0:
            return TENS[tens_digit]
        else:
            return f"{TENS[tens_digit]}-{ONES[ones_digit]}"
    return str(number)  # fallback

def format_number(number):
    """
    Format a number with Nepali-style comma separation.
    
    In Nepali numbering system, commas are placed differently than Western style:
    - First comma after 3 digits from the right
    - Then every 2 digits thereafter
    - Example: 1000000 becomes 10,00,000 (not 1,000,000)
    
    Args:
        number (int or float): The number to format.
    
    Returns:
        str: The formatted number string with Nepali-style comma placement.
        
    Examples:
        >>> format_number(1000000)
        '10,00,000'
        >>> format_number(120000)
        '1,20,000'
        >>> format_number(123.45)
        '123.45'
    
    Note:
        This function is currently not implemented and returns None.
        Implementation is planned for future releases.
    """
    # TODO: Implement Nepali-style number formatting
    pass