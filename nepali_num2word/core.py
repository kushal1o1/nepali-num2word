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
    """Convert a number to words in Nepali-style format (crore, lakh, thousand)"""
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
    """Convert an integer to words in Nepali-style format (crore, lakh, thousand)"""
    if number == 0:
        return 'zero'
    
    result = []
    
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
    """Convert basic numbers (1-99) to words"""
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