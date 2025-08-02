import argparse
from nepali_num2word import convert_to_words

def main():
    parser = argparse.ArgumentParser(description='Convert number to words in Nepali style (crore, lakh, thousand).')
    parser.add_argument('number', type=str, help='Enter number to convert (int or float)')
    parser.add_argument('--lang', choices=['en', 'np'], default='en', help='Language output (en for English, np for Nepali)')
    args = parser.parse_args()

    try:
        # Handle both integer and float inputs
        if '.' in args.number:
            number = float(args.number)
        else:
            number = int(args.number)
        
        result = convert_to_words(number, lang=args.lang)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()