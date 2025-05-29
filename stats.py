def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

def get_num_words(filepath):
    whole_string = get_book_text(filepath)
    word_split = whole_string.split()
    count = 0
    for word in word_split:
        count += 1
    print(f'{count} words found in the document')



def char_count(filepath):
     whole_string = get_book_text(filepath)
     word_split = whole_string.split()
     word_list = str(word_split)
     word_list = word_list.lower()
     char_dict = {}
     for char in word_list:
        if char in char_dict:
             char_dict[char] += 1
        else:
             char_dict[char] = 1
     print(char_dict)
