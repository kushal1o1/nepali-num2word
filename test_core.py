# test_script.py
from nepali_num2word.core import convert_to_words

print(convert_to_words(120000))            # ➝ one lakh twenty thousand
print(convert_to_words(34000000, 'np'))    # ➝ तीन करोड चालीस लाख
print(convert_to_words(123.45))            # ➝ one hundred twenty-three rupees and forty-five paise
