import argparse
from nepali_num2word import format_number

def main():
    parser = argparse.ArgumentParser(description='Format numbers with Nepali-style comma separation.')
    parser.add_argument('number', type=str, help='Enter number to format (int or float)')
    args = parser.parse_args()

    try:
        # Handle both integer and float inputs
        if '.' in args.number:
            number = float(args.number)
        else:
            number = int(args.number)
        
        result = format_number(number)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
