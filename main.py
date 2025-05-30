from stats import get_num_words
from stats import char_count
from stats import get_chars_dict

def main():
    
    def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    def print_report(sorted, word_count):
        print('============ BOOKBOT ============')
        print('Analyzing book found at books/frankenstein.txt...')
        print('----------- Word Count ----------')
        print(f'Found {word_count} total words')
        print('--------- Character Count -------')
        for dict in sorted:
            print(f'{dict["char"]}: {dict["num"]}')

    contents = get_book_text('books/frankenstein.txt')
    analysis = char_count(contents)
    sorted = get_chars_dict(analysis)
    word_count = get_num_words(contents)
    final_report = print_report(sorted, word_count)

if __name__ == "__main__":
    main()