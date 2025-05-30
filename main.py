import sys
from stats import get_num_words
from stats import char_count
from stats import get_chars_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def print_report(sorted, word_count):
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {filepath}...')
        print('----------- Word Count ----------')
        print(f'Found {word_count} total words')
        print('--------- Character Count -------')
        for dict in sorted:
            print(f'{dict["char"]}: {dict["num"]}')

    contents = get_book_text(filepath)
    analysis = char_count(contents)
    sorted = get_chars_dict(analysis)
    word_count = get_num_words(contents)
    final_report = print_report(sorted, word_count)

if __name__ == "__main__":
    main()