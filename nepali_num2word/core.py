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
            return _format_integer_part(integer_part)
        else:
            # Split into integer and decimal parts
            integer_part = int(number)
            decimal_part = str(number).split('.')[1]
            
            if integer_part == 0:
                return f"0.{decimal_part}"
            else:
                formatted_integer = _format_integer_part(integer_part)
                return f"{formatted_integer}.{decimal_part}"
    
    # Handle integer numbers
    return _format_integer_part(number)


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