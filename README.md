
# 🇳🇵 nepali-num2word

Convert numbers into **Nepali-style currency words** — supports both **English transliteration** (e.g., "one lakh twenty thousand") and **Nepali Unicode** (e.g., "एक लाख बीस हजार").

---

## 🚀 Features

- ✅ Convert integer and float to Nepali-style number words  
- ✅ Supports **crore**, **lakh**, **thousand**, **hundred** grouping  
- ✅ Handles **decimal amounts** → outputs **rupees** and **paise**  
- ✅ Supports **Nepali Unicode output**  
- ✅ Provides **CLI command**: `nepaliword <number> --lang en|np`  
- ✅ Easy-to-use Python function: `convert_to_words(number, lang='en')`

---

## 📦 Installation

```bash
# After publishing to PyPI
pip install nepali-num2word
```

For local testing:

```bash
git clone https://github.com/yourname/nepali-num2word
cd nepali-num2word
python cli/main.py 120000 --lang np
```

---

## 🧑‍💻 Usage

### ➤ Python Function

```python
from nepali_num2word import convert_to_words

print(convert_to_words(120000))              # → one lakh twenty thousand
print(convert_to_words(34000000))            # → three crore forty lakh
print(convert_to_words(123.45))              # → one hundred twenty-three rupees and forty-five paise

print(convert_to_words(120000, lang='np'))   # → एक लाख बीस हजार
print(convert_to_words(123.45, lang='np'))   # → एक सय तेइस रुपैयाँ र पैंतालीस पैसा
```

---

### ➤ CLI Command

```bash
nepaliword 120000
# → one lakh twenty thousand

nepaliword 123.45 --lang np
# → एक सय तेइस रुपैयाँ र पैंतालीस पैसा
```

---

## 🧠 API Reference

```python
convert_to_words(number: int | float, lang='en') -> str
```

- `number`: number to convert (int or float)  
- `lang`: `'en'` for English (default), `'np'` for Nepali Unicode

---

## 🛠 Roadmap

- [x] Integer to words in Nepali format  
- [x] Decimal (paise) support  
- [x] Nepali Unicode output  
- [x] CLI tool support  
- [ ] More natural phrasing for compound numbers  
- [ ] Reverse conversion (Nepali words → number)  

---

## 📄 License

MIT License

---

## 🙏 Credits

Created by Kushal — built with ❤️ for Nepal 🇳🇵
