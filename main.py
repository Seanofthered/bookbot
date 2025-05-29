def main():
    read_frankenstein = get_book_text('books/frankenstein.txt')


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_split = file_contents.split()
        count = 0
        for word in word_split:
            count += 1
        print(f'{count} words found in the document')
if __name__ == "__main__":
    main()