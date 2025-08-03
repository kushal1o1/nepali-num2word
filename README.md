# nepali-num2word

[![PyPI version](https://badge.fury.io/py/nepali-num2word.svg)](https://badge.fury.io/py/nepali-num2word)
[![Python Support](https://img.shields.io/pypi/pyversions/nepali-num2word.svg)](https://pypi.org/project/nepali-num2word/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](https://static.pepy.tech/badge/nepali-num2word/month)](https://pepy.tech/projects/nepali-num2word)

A comprehensive Python library for converting numbers to Nepali-style currency words with support for both English transliteration and Nepali Unicode (Devanagari script). Perfect for financial applications, educational tools, and any system requiring Nepali number formatting.

## ✨ Features

- **🔢 Number to Words Conversion**: Convert integers and floats to Nepali-style number words
- **🇳🇵 Dual Language Support**: English transliteration and authentic Nepali Unicode (Devanagari)
- **💰 Currency Support**: Automatic rupees and paise handling for decimal amounts
- **📊 Nepali Number Formatting**: Format numbers with traditional Nepali comma placement (10,00,000)
- **📦 Compact Representation**: Human-readable format (1.2 lakhs, 4.5 crores)
- **⚡ CLI Tools**: Complete command-line interface suite
- **🛡️ Robust Error Handling**: Comprehensive input validation and clear error messages
- **➖ Negative Number Support**: Handles negative values seamlessly

## 🚀 Quick Start

### Installation

```bash
pip install nepali-num2word
```

### Basic Usage

```python
from nepali_num2word import convert_to_words, format_number, compact_number

# Convert to words (English)
print(convert_to_words(123456))
# Output: one lakh twenty-three thousand four hundred fifty-six

# Convert to words (Nepali)
print(convert_to_words(123456, lang='np'))
# Output: एक लाख तेइस हजार चार सय छप्पन्न

# Format with Nepali-style commas
print(format_number(1234567))
# Output: 12,34,567

# Format with Nepali Unicode digits
print(format_number(1234567, lang='np'))
# Output: १२,३४,५६७

# Compact representation
print(compact_number(1234567))
# Output: 12.3 lakhs
```

## 📖 Documentation

### API Reference

#### `convert_to_words(number, lang='en')`

Convert numbers to words in Nepali numbering system.

**Parameters:**
- `number` (int | float | str): Number to convert (supports negative numbers)
- `lang` (str): Language code - `'en'` for English, `'np'` for Nepali Unicode

**Returns:** `str` - Number converted to words

**Examples:**
```python
convert_to_words(120000)                    # "one lakh twenty thousand"
convert_to_words(34000000)                  # "three crore forty lakh"
convert_to_words(123.45)                    # "one hundred twenty-three rupees and forty-five paise"
convert_to_words(-123)                      # "-one hundred twenty-three"

# Nepali Unicode
convert_to_words(120000, lang='np')         # "एक लाख बीस हजार"
convert_to_words(123.45, lang='np')         # "एक सय तेइस रुपैयाँ र पैँतालीस पैसा"
```

#### `format_number(number, lang='en')`

Format numbers with Nepali-style comma separation.

**Parameters:**
- `number` (int | float): Number to format
- `lang` (str): Language code - `'en'` for English digits, `'np'` for Nepali Unicode digits

**Returns:** `str` - Formatted number string

**Examples:**
```python
format_number(1000000)                      # "10,00,000"
format_number(120000)                       # "1,20,000"
format_number(34000000)                     # "3,40,00,000"

# Nepali Unicode digits
format_number(1000000, lang='np')           # "१०,००,०००"
format_number(120000, lang='np')            # "१,२०,०००"
format_number(123.45, lang='np')            # "१२३.४५"
```

#### `compact_number(number, lang='en')`

Convert numbers to compact, human-readable format.

**Parameters:**
- `number` (int | float | str): Number to convert
- `lang` (str): Language code - `'en'` for English, `'np'` for Nepali Unicode

**Returns:** `str` - Compact number representation

**Examples:**
```python
compact_number(999)                         # "999"
compact_number(1500)                        # "1.5 thousand"
compact_number(100000)                      # "1 lakh"
compact_number(4200000)                     # "42 lakhs"
compact_number(42000000)                    # "4.2 crores"

# Nepali Unicode
compact_number(4200000, lang='np')          # "४२ लाख"
compact_number(42000000, lang='np')         # "४.२ करोड"
```

### Command Line Interface

The package includes three CLI commands:

#### `nepaliword` - Convert numbers to words
```bash
nepaliword 120000
# Output: one lakh twenty thousand

nepaliword 123.45 --lang np
# Output: एक सय तेइस रुपैयाँ र पैंतालीस पैसा
```

#### `nepaliformat` - Format with Nepali-style commas
```bash
nepaliformat 1000000
# Output: 10,00,000

nepaliformat 1000000 --lang np
# Output: १०,००,०००
```

#### `nepalicompact` - Compact number representation
```bash
nepalicompact 4200000
# Output: 42 lakhs

nepalicompact 42000000 --lang np
# Output: ४.२ करोड
```

## 🛡️ Error Handling

The library provides comprehensive error handling with clear, actionable error messages:

### Supported Input Types
- ✅ Integers: `123`, `-456`
- ✅ Floats: `123.45`, `-67.89`
- ✅ Numeric strings: `"123"`, `"123.45"`, `"-456"`

### Error Examples
```python
# Type errors
convert_to_words(None)          # TypeError: Number cannot be None
convert_to_words(True)          # TypeError: Boolean values are not supported
convert_to_words([])            # TypeError: Unsupported type: list

# Value errors
convert_to_words("")            # ValueError: Empty string is not a valid number
convert_to_words("hello")       # ValueError: 'hello' is not a valid number
convert_to_words(1000000000)    # ValueError: Number too large (max: 999,999,999)
```

## 🎯 Use Cases

- **Financial Applications**: Convert amounts to words for checks, invoices, and receipts
- **Educational Software**: Teaching Nepali number systems and currency
- **Government Systems**: Official documents requiring Nepali number representation
- **Banking Software**: Amount verification and display in Nepali format
- **E-commerce**: Price display in traditional Nepali numbering

## 🔧 Development

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/kushal1o1/nepali-num2word.git
cd nepali-num2word

# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/

# Test CLI locally
python cli/main.py 120000 --lang np
python cli/format_main.py 1000000
python cli/compact_main.py 4200000
```

### Project Structure

```
nepali-num2word/
├── nepali_num2word/
│   ├── __init__.py
│   └── core.py
├── cli/
│   ├── main.py
│   ├── format_main.py
│   └── compact_main.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_core.py
│   └── test_cli.py
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── setup.py
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`python -m pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📋 Roadmap

- [x] Integer to words in Nepali format
- [x] Decimal (paise) support
- [x] Nepali Unicode output
- [x] CLI tool support
- [x] Nepali-style number formatting
- [x] Compact number representation
- [x] Comprehensive error handling
- [ ] More natural phrasing for compound numbers
- [ ] Reverse conversion (Nepali words → number)
- [ ] Support for ordinal numbers
- [ ] Date formatting in Nepali style

## 📊 Performance

The library is optimized for performance with minimal dependencies:
- Zero external dependencies for core functionality
- Efficient string building algorithms
- Comprehensive input validation
- Memory-efficient processing

## 🌍 Language Support

| Feature | English | Nepali Unicode |
|---------|---------|----------------|
| Number to Words | ✅ | ✅ |
| Currency (Rupees/Paise) | ✅ | ✅ |
| Negative Numbers | ✅ | ✅ |
| Compact Format | ✅ | ✅ |
| CLI Support | ✅ | ✅ |

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ for the Nepali community
- Inspired by the need for proper Nepali number formatting in software applications
- Thanks to all contributors who help improve this library

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/kushal1o1/nepali-num2word/issues)
- **Discussions**: [GitHub Discussions](https://github.com/kushal1o1/nepali-num2word/discussions)
- **Email**: [Contact maintainer](mailto:work.kusal@gmail.com)

---

**Made in Nepal 🇳🇵 | Created by [Kushal](https://github.com/kushal1o1)**