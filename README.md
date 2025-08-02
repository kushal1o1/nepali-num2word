
# 🇳🇵 nepali-num2word

Convert numbers into **Nepali-style currency words** — supports both **English transliteration** (e.g., "one lakh twenty thousand") and **Nepali Unicode** (e.g., "एक ल## 🛠 Roadmap

- [x] Integer to words in Nepali format  
- [x] Decimal (paise) support  
- [x] Nepali Unicode output  
- [x] CLI tool support  
- [x] **NEW**: Nepali-style number formatting (10,00,000)
- [x] **NEW**: Compact number representation (1.2 lakhs, 4.5 crores)
- [x] **NEW**: Complete CLI suite (nepaliword, nepaliformat, nepalicompact)
- [ ] More natural phrasing for compound numbers  
- [ ] Reverse conversion (Nepali words → number)र"). **Full Nepali language support now implemented!**

---

## 🚀 Features

- ✅ Convert integer and float to Nepali-style number words  
- ✅ Supports **crore**, **lakh**, **thousand**, **hundred** grouping  
- ✅ Handles **decimal amounts** → outputs **rupees** and **paise**  
- ✅ **Negative number support** → prefixed with "-" sign
- ✅ **Robust error handling** → clear error messages for invalid inputs
- ✅ **Compact number formatting** → human-readable format like "1.2 lakhs", "4.5 crores"
- ✅ **Full Nepali Unicode support** with authentic Devanagari words
- ✅ Provides **CLI command**: `nepaliword <number> --lang en|np`  
- ✅ Easy-to-use Python function: `convert_to_words(number, lang='en')`
- ✅ **NEW**: Format numbers with Nepali-style comma separation: `format_number(1000000)` → `10,00,000`
- ✅ **NEW**: Compact number representation: `compact_number(4200000)` → `42 lakhs`

---

## 🚀 Quick Start

```python
# Install the package
pip install nepali-num2word

# Basic usage
from nepali_num2word import convert_to_words, format_number, compact_number

# Convert numbers to words
convert_to_words(123456)                    # → "one lakh twenty-three thousand four hundred fifty-six"
convert_to_words(123456, lang='np')         # → "एक लाख तेइस हजार चार सय छप्पन्न"

# Format with Nepali-style commas  
format_number(1234567)                      # → "12,34,567"

# Compact representation
compact_number(1234567)                     # → "12.3 lakhs"
compact_number(12345678)                    # → "1.2 crores"
```

---

## 📦 Installation

```bash
# After publishing to PyPI
pip install nepali-num2word
```

For local testing:

```bash
git clone https://github.com/kushal1o1/nepali-num2word
cd nepali-num2word
python cli/main.py 120000 --lang np
```

---

## 🧑‍💻 Usage

### ➤ Python Function

```python
from nepali_num2word import convert_to_words, format_number, compact_number

# Convert to words
print(convert_to_words(120000))              # → one lakh twenty thousand
print(convert_to_words(34000000))            # → three crore forty lakh
print(convert_to_words(123.45))              # → one hundred twenty-three rupees and forty-five paise
print(convert_to_words(-123))                # → -one hundred twenty-three
print(convert_to_words(-123.45))             # → -one hundred twenty-three rupees and forty-five paise

print(convert_to_words(120000, lang='np'))   # → एक लाख बीस हजार
print(convert_to_words(123.45, lang='np'))   # → एक सय तेइस रुपैयाँ र पैँतालीस पैसा
print(convert_to_words(-123, lang='np'))     # → -एक सय तेइस
print(convert_to_words(-123.45, lang='np'))  # → -एक सय तेइस रुपैयाँ र पैँतालीस पैसा

# Format numbers with Nepali-style commas
print(format_number(1000000))                # → 10,00,000
print(format_number(120000))                 # → 1,20,000
print(format_number(34000000))               # → 3,40,00,000
print(format_number(123.45))                 # → 123.45

# Compact number representation
print(compact_number(999))                   # → 999
print(compact_number(1500))                  # → 1.5 thousand
print(compact_number(100000))                # → 1 lakh
print(compact_number(4200000))               # → 4.2 crores
print(compact_number(42000000))              # → 42 crores

print(compact_number(4200000, lang='np'))    # → ४२ लाख
print(compact_number(42000000, lang='np'))   # → ४२ करोड
print(compact_number(-1500000, lang='np'))   # → -१५ लाख
```

---

### ➤ CLI Command

```bash
# Convert to words
nepaliword 120000
# → one lakh twenty thousand

nepaliword 123.45 --lang np
# → एक सय तेइस रुपैयाँ र पैंतालीस पैसा

nepaliword -123 --lang np
# → -एक सय तेइस

# Format numbers with Nepali-style commas
nepaliformat 1000000
# → 10,00,000

# Compact number representation
nepalicompact 4200000
# → 42 lakhs

nepalicompact 42000000 --lang np
# → ४.२ करोड
```

---

## 🧠 API Reference

### Number to Words
```python
convert_to_words(number: int | float | str, lang='en') -> str
```

- `number`: number to convert (int, float, or numeric string - supports negative numbers with "-" prefix)  
- `lang`: `'en'` for English (default), `'np'` for Nepali Unicode
- **Raises**: `TypeError` for invalid types, `ValueError` for invalid values

### Number Formatting
```python
format_number(number: int | float) -> str
```

- `number`: number to format with Nepali-style comma separation
- Returns: formatted string with commas in Nepali style (e.g., `10,00,000`)

### Compact Number Representation
```python
compact_number(number: int | float | str, lang='en') -> str
```

- `number`: number to convert to compact format (int, float, or numeric string)
- `lang`: `'en'` for English (default), `'np'` for Nepali Unicode  
- Returns: human-readable compact format (e.g., `"1.2 lakhs"`, `"4.5 crores"`)
- **Raises**: `TypeError` for invalid types, `ValueError` for invalid values

#### Compact Number Examples:
```python
compact_number(999)        # → "999"
compact_number(1500)       # → "1.5 thousand" 
compact_number(100000)     # → "1 lakh"
compact_number(4200000)    # → "4.2 crores"
compact_number(4000000)    # → "4 crores"  # Auto-trims .0

# Nepali examples
compact_number(100000, lang='np')   # → "१ लाख"
compact_number(4200000, lang='np')  # → "४२ लाख"
compact_number(42000000, lang='np') # → "४२ करोड"
```

---

## � Error Handling

The package includes comprehensive error handling to provide clear, helpful error messages:

### Supported Input Types
- ✅ **Integers**: `123`, `-456`
- ✅ **Floats**: `123.45`, `-67.89`  
- ✅ **Numeric Strings**: `"123"`, `"123.45"`, `"-456"`

### Error Cases

#### Type Errors
```python
convert_to_words(None)          # → TypeError: Number cannot be None
convert_to_words(True)          # → TypeError: Boolean values are not supported. Use 0 or 1 instead of True
convert_to_words([])            # → TypeError: Unsupported type: list. Expected int, float, or numeric string
convert_to_words({})            # → TypeError: Unsupported type: dict. Expected int, float, or numeric string
```

#### Value Errors
```python
convert_to_words("")            # → ValueError: Empty string is not a valid number
convert_to_words("hello")       # → ValueError: 'hello' is not a valid number
convert_to_words("123abc")      # → ValueError: '123abc' is not a valid number
convert_to_words(1000000000)    # → ValueError: Number 1000000000 is too large. Maximum supported: 999,999,999
```

#### CLI Error Handling
```bash
# Invalid inputs are caught and reported clearly
nepaliword "hello"              # → Error: Invalid number format: hello
nepaliword True                 # → Error: Invalid number format: True
```

### Valid String Conversions
```python
# These string inputs work automatically
convert_to_words("123")         # → "one hundred twenty-three"
convert_to_words("123.45")      # → "one hundred twenty-three rupees and forty-five paise"
convert_to_words("-123")        # → "-one hundred twenty-three"
```

---

## �🛠 Roadmap

- [x] Integer to words in Nepali format  
- [x] Decimal (paise) support  
- [x] Nepali Unicode output  
- [x] CLI tool support  
- [x] **NEW**: Nepali-style number formatting (10,00,000)
- [ ] More natural phrasing for compound numbers  
- [ ] Reverse conversion (Nepali words → number)  
- [ ] CLI support for number formatting  

---

## 📄 License

MIT License

---

## 🙏 Credits

Created by Kushal — built with ❤️ for Nepal 🇳🇵
