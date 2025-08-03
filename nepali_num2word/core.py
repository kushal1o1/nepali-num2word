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

# Nepali number words mapping (0-99) - Complete lookup table
ONES_NP = [
    'शून्य', 'एक', 'दुई', 'तीन', 'चार', 'पाँच', 'छ', 'सात', 'आठ', 'नौ',
    'दश', 'एघार', 'बाह्र', 'तेह्र', 'चौध', 'पन्ध्र', 'सोह्र', 'सत्र', 'अठार', 'उन्नाइस',
    'बीस', 'एक्काइस', 'बाइस', 'तेइस', 'चौबीस', 'पच्चिस', 'छब्बिस', 'सत्ताइस', 'अठ्ठाईस', 'उनन्तीस',
    'तीस', 'एकतीस', 'बत्तीस', 'तेत्तीस', 'चौँतीस', 'पैँतीस', 'छत्तीस', 'सैँतीस', 'अठतीस', 'उनन्चालीस',
    'चालीस', 'एकचालीस', 'बयालीस', 'त्रिचालीस', 'चवालीस', 'पैँतालीस', 'छयालीस', 'सच्चालीस', 'अठचालीस', 'उनन्चास',
    'पचास', 'एकाउन्न', 'बाउन्न', 'त्रिपन्न', 'चौवन्न', 'पच्पन्न', 'छपन्न', 'सन्ताउन्न', 'अन्ठाउन्न', 'उनन्साठी',
    'साठी', 'एकसठ्ठी', 'बयसट्ठी', 'त्रिसठ्ठी', 'चौँसठ्ठी', 'पैँसठ्ठी', 'छयसट्ठी', 'सतसट्ठी', 'अठसट्ठी', 'उनन्सत्तरी',
    'सत्तरी', 'एकहत्तर', 'बहत्तर', 'त्रिहत्तर', 'चौहत्तर', 'पचहत्तर', 'छयहत्तर', 'सतहत्तर', 'अठहत्तर', 'उनासी',
    'असी', 'एकासी', 'बयासी', 'त्रियासी', 'चौरासी', 'पचासी', 'छयासी', 'सतासी', 'अठासी', 'उनान्नब्बे',
    'नब्बे', 'एकान्नब्बे', 'बयान्नब्बे', 'त्रियान्नब्बे', 'चौरान्नब्बे', 'पन्चान्नब्बे', 'छयान्नब्बे', 'सन्तान्‍नब्बे', 'अन्ठान्नब्बे', 'उनान्सय'
]

# Nepali scale words
SCALE_NP = {
    'hundred': 'सय',
    'thousand': 'हजार',
    'lakh': 'लाख',
    'crore': 'करोड'
}


def convert_to_words(number, lang='en'):
    """
    Convert a number to words in Nepali-style format (crore, lakh, thousand).
    
    Args:
        number (int or float): The number to convert to words.
                              Can be integer or float, including negative numbers.
        lang (str, optional): Language for output. 'en' for English, 'np' for Nepali.
                              Defaults to 'en'. Both languages are now supported.
    
    Returns:
        str: The number converted to words.
             For integers: "one lakh twenty thousand" or "एक लाख बीस हजार"
             For floats: "one hundred twenty-three rupees and forty-five paise" 
                        or "एक सय तेइस रुपैयाँ र पैँतालीस पैसा"
             For negatives: "-one hundred twenty-three" or "-एक सय तेइस"
    
    Raises:
        TypeError: If number is not a valid numeric type.
        ValueError: If number cannot be converted to a numeric value.
    
    Examples:
        >>> convert_to_words(120000)
        'one lakh twenty thousand'
        >>> convert_to_words(120000, lang='np')
        'एक लाख बीस हजार'
        >>> convert_to_words(123.45)
        'one hundred twenty-three rupees and forty-five paise'
        >>> convert_to_words(123.45, lang='np')
        'एक सय तेइस रुपैयाँ र पैँतालीस पैसा'
        >>> convert_to_words(-123, lang='np')
        '-एक सय तेइस'
    """
    # Type validation and conversion
    if number is None:
        raise TypeError("Number cannot be None")
    
    # Handle string inputs - try to convert to number
    if isinstance(number, str):
        if number.strip() == '':
            raise ValueError("Empty string is not a valid number")
        try:
            # Try to convert string to number
            if '.' in number:
                number = float(number)
            else:
                number = int(number)
        except ValueError:
            raise ValueError(f"'{number}' is not a valid number")
    
    # Handle boolean values explicitly (before numeric check since bool is subclass of int)
    if isinstance(number, bool):
        raise TypeError(f"Boolean values are not supported. Use 0 or 1 instead of {number}")
    
    # Check if it's a valid numeric type
    if not isinstance(number, (int, float)):
        raise TypeError(f"Unsupported type: {type(number).__name__}. Expected int, float, or numeric string")
    
    # Validate numeric range (optional - you can adjust these limits)
    if abs(number) > 999999999:  # 99 crores limit
        raise ValueError(f"Number {number} is too large. Maximum supported: 999,999,999")
    
    # Handle negative numbers
    if number < 0:
        positive_result = convert_to_words(abs(number), lang)
        return f"-{positive_result}"
    
    # Handle decimal numbers (rupees and paise)
    if isinstance(number, float) or '.' in str(number):
        if isinstance(number, str):
            number = float(number)
        
        integer_part = int(number)
        decimal_part = round((number - integer_part) * 100)
        
        if integer_part == 0 and decimal_part == 0:
            return 'शून्य' if lang == 'np' else 'zero'
        
        result_parts = []
        
        if integer_part > 0:
            rupees_word = convert_integer_to_words(integer_part, lang)
            if lang == 'np':
                result_parts.append(f"{rupees_word} रुपैयाँ")
            else:
                if integer_part == 1:
                    result_parts.append(f"{rupees_word} rupee")
                else:
                    result_parts.append(f"{rupees_word} rupees")
        
        if decimal_part > 0:
            paise_word = convert_integer_to_words(decimal_part, lang)
            if lang == 'np':
                result_parts.append(f"{paise_word} पैसा")
            else:
                if decimal_part == 1:
                    result_parts.append(f"{paise_word} paisa")
                else:
                    result_parts.append(f"{paise_word} paise")
        
        if len(result_parts) == 2:
            connector = " र " if lang == 'np' else " and "
            return f"{result_parts[0]}{connector}{result_parts[1]}"
        else:
            return result_parts[0] if result_parts else ('शून्य' if lang == 'np' else 'zero')
    
    # Handle integer numbers
    return convert_integer_to_words(number, lang)

def convert_integer_to_words(number, lang='en'):
    """
    Convert an integer to words in Nepali-style format (crore, lakh, thousand).
    
    Args:
        number (int): The integer to convert to words.
        lang (str, optional): Language for output. 'en' for English, 'np' for Nepali.
                              Defaults to 'en'.
    
    Returns:
        str: The integer converted to words using Nepali-style grouping.
    
    Examples:
        >>> convert_integer_to_words(120000)
        'one lakh twenty thousand'
        >>> convert_integer_to_words(120000, lang='np')
        'एक लाख बीस हजार'
        >>> convert_integer_to_words(34000000)
        'three crore forty lakh'
    """
    if number == 0:
        return 'शून्य' if lang == 'np' else 'zero'
    
    result = []
    
    # Handle crores (10,000,000)
    if number >= 10000000:
        crores = number // 10000000
        if lang == 'np':
            result.append(f"{basic_number_to_words(crores, lang)} करोड")
        else:
            result.append(f"{basic_number_to_words(crores, lang)} crore")
        number = number % 10000000
    
    # Handle lakhs (100,000)
    if number >= 100000:
        lakhs = number // 100000
        if lang == 'np':
            result.append(f"{basic_number_to_words(lakhs, lang)} लाख")
        else:
            result.append(f"{basic_number_to_words(lakhs, lang)} lakh")
        number = number % 100000
    
    # Handle thousands (1,000)
    if number >= 1000:
        thousands = number // 1000
        if lang == 'np':
            result.append(f"{basic_number_to_words(thousands, lang)} हजार")
        else:
            result.append(f"{basic_number_to_words(thousands, lang)} thousand")
        number = number % 1000
    
    # Handle hundreds (100)
    if number >= 100:
        hundreds = number // 100
        if lang == 'np':
            result.append(f"{basic_number_to_words(hundreds, lang)} सय")
        else:
            result.append(f"{basic_number_to_words(hundreds, lang)} hundred")
        number = number % 100
    
    # Handle remaining (1-99)
    if number > 0:
        result.append(basic_number_to_words(number, lang))
    
    return ' '.join(result)

def basic_number_to_words(number, lang='en'):
    """
    Convert basic numbers (0-99) to words.
    
    Args:
        number (int): The number to convert (should be between 0-99).
        lang (str, optional): Language for output. 'en' for English, 'np' for Nepali.
                              Defaults to 'en'.
    
    Returns:
        str: The number converted to words.
    
    Examples:
        >>> basic_number_to_words(25)
        'twenty-five'
        >>> basic_number_to_words(25, lang='np')
        'पच्चिस'
        >>> basic_number_to_words(15)
        'fifteen'
        >>> basic_number_to_words(90, lang='np')
        'नब्बे'
    """
    if lang == 'np':
        # For Nepali, use direct lookup from 0-99
        if 0 <= number <= 99:
            return ONES_NP[number]
        return str(number)  # fallback
    else:
        # English logic (existing)
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

def format_number(number, lang='en'):
    """
    Format a number with Nepali-style comma separation.
    
    In Nepali numbering system, commas are placed differently than Western style:
    - First comma after 3 digits from the right
    - Then every 2 digits thereafter
    - Example: 1000000 becomes 10,00,000 (not 1,000,000)
    
    Args:
        number (int or float): The number to format.
        lang (str, optional): Language for output. 'en' for English digits, 'np' for Nepali Unicode digits.
                              Defaults to 'en'.
    
    Returns:
        str: The formatted number string with Nepali-style comma placement.
        
    Examples:
        >>> format_number(1000000)
        '10,00,000'
        >>> format_number(1000000, lang='np')
        '१०,००,०००'
        >>> format_number(120000)
        '1,20,000'
        >>> format_number(120000, lang='np')
        '१,२०,०००'
        >>> format_number(123.45)
        '123.45'
        >>> format_number(123.45, lang='np')
        '१२३.४५'
    """
    # Handle string input
    if isinstance(number, str):
        try:
            number = float(number) if '.' in number else int(number)
        except ValueError:
            return str(number)  # Return as-is if not a valid number
    
    # Handle decimal numbers
    if isinstance(number, float):
        if number == int(number):
            # If it's a whole number (like 123.0), treat as integer
            integer_part = int(number)
            result = _format_integer_part(integer_part)
            return _convert_digits_to_nepali(result) if lang == 'np' else result
        else:
            # Split into integer and decimal parts
            integer_part = int(number)
            decimal_part = str(number).split('.')[1]
            
            if integer_part == 0:
                result = f"0.{decimal_part}"
                return _convert_digits_to_nepali(result) if lang == 'np' else result
            else:
                formatted_integer = _format_integer_part(integer_part)
                result = f"{formatted_integer}.{decimal_part}"
                return _convert_digits_to_nepali(result) if lang == 'np' else result
    
    # Handle integer numbers
    result = _format_integer_part(number)
    return _convert_digits_to_nepali(result) if lang == 'np' else result


def _format_integer_part(number):
    """
    Helper function to format the integer part with Nepali-style commas.
    
    Args:
        number (int): The integer to format.
    
    Returns:
        str: Formatted integer with Nepali-style commas.
    """
    if number == 0:
        return "0"
    
    # Convert to string and reverse for easier processing
    num_str = str(abs(number))
    reversed_digits = num_str[::-1]
    
    # Add commas: first after 3 digits, then every 2 digits
    result = []
    for i, digit in enumerate(reversed_digits):
        if i == 3 or (i > 3 and (i - 3) % 2 == 0):
            result.append(',')
        result.append(digit)
    
    # Reverse back and handle negative numbers
    formatted = ''.join(result[::-1])
    return f"-{formatted}" if number < 0 else formatted


def compact_number(number, precision=1, lang='en'):
    """
    Convert numbers to compact, human-readable format using Nepali-style scales.
    
    Args:
        number (int or float): The number to convert.
        precision (int, optional): Decimal places to show (default: 1). 
                                 Auto-trims .0 for whole numbers.
        lang (str, optional): Language for output. 'en' for English, 'np' for Nepali.
                              Defaults to 'en'.
    
    Returns:
        str: Compact representation like "1.2 lakhs", "4.5 crores", "१.२ लाख"
    
    Raises:
        TypeError: If number is not a valid numeric type.
        ValueError: If number cannot be converted to a numeric value.
    
    Examples:
        >>> compact_number(999)
        '999'
        >>> compact_number(1500)
        '1.5 thousand'
        >>> compact_number(100000)
        '1 lakh'
        >>> compact_number(4200000)
        '4.2 crores'
        >>> compact_number(4000000)
        '4 crores'
        >>> compact_number(100000, lang='np')
        '१ लाख'
        >>> compact_number(4200000, lang='np')
        '४.२ करोड'
    """
    # Type validation (reuse same validation as convert_to_words)
    if number is None:
        raise TypeError("Number cannot be None")
    
    # Handle string inputs
    if isinstance(number, str):
        if number.strip() == '':
            raise ValueError("Empty string is not a valid number")
        try:
            if '.' in number:
                number = float(number)
            else:
                number = int(number)
        except ValueError:
            raise ValueError(f"'{number}' is not a valid number")
    
    # Handle boolean values
    if isinstance(number, bool):
        raise TypeError(f"Boolean values are not supported. Use 0 or 1 instead of {number}")
    
    # Check if it's a valid numeric type
    if not isinstance(number, (int, float)):
        raise TypeError(f"Unsupported type: {type(number).__name__}. Expected int, float, or numeric string")
    
    # Validate numeric range
    if abs(number) > 999999999:
        raise ValueError(f"Number {number} is too large. Maximum supported: 999,999,999")
    
    # Handle negative numbers
    if number < 0:
        positive_result = compact_number(abs(number), precision, lang)
        return f"-{positive_result}"
    
    # Handle zero
    if number == 0:
        return 'शून्य' if lang == 'np' else '0'
    
    # Determine scale and value
    if number >= 10000000:  # >= 1 crore
        value = number / 10000000
        scale = 'करोड' if lang == 'np' else 'crores'
    elif number >= 1000000:  # >= 10 lakhs - decide between crores and lakhs
        crore_value = number / 10000000
        lakh_value = number / 100000
        
        # Use crores only if it results in a cleaner representation (>= 1 crore)
        if crore_value >= 1:
            value = crore_value
            scale = 'करोड' if lang == 'np' else 'crores'
        else:
            value = lakh_value
            scale = 'लाख' if lang == 'np' else 'lakhs'
    elif number >= 100000:  # >= 1 lakh
        value = number / 100000
        scale = 'लाख' if lang == 'np' else 'lakhs'
    elif number >= 1000:    # >= 1 thousand
        value = number / 1000
        scale = 'हजार' if lang == 'np' else 'thousand'
    else:                   # < 1000
        # Return as-is for numbers less than 1000
        if lang == 'np':
            return _convert_digits_to_nepali(str(int(number)))
        else:
            return str(int(number))
    
    # Format the value with specified precision
    if value == int(value):
        # Whole number - don't show decimal
        formatted_value = str(int(value))
    else:
        # Decimal number - format with precision and trim trailing zeros
        formatted_value = f"{value:.{precision}f}".rstrip('0').rstrip('.')
    
    # Convert digits to Nepali if needed
    if lang == 'np':
        formatted_value = _convert_digits_to_nepali(formatted_value)
    
    # Handle singular vs plural for English
    if lang == 'en':
        if scale in ['crores', 'lakhs'] and float(formatted_value) == 1:
            scale = scale[:-1]  # Remove 's' for singular (crore, lakh)
    
    return f"{formatted_value} {scale}"


def _convert_digits_to_nepali(text):
    """
    Convert Western digits (0-9) to Nepali digits (०-९) in a string.
    
    Args:
        text (str): Text containing Western digits.
    
    Returns:
        str: Text with Nepali digits.
    """
    nepali_digits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']
    result = text
    for i, nepali_digit in enumerate(nepali_digits):
        result = result.replace(str(i), nepali_digit)
    return result