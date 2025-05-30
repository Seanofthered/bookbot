def get_num_words(contents):
    whole_string = contents
    word_split = whole_string.split()
    count = 0
    for word in word_split:
        count += 1
    return count



def char_count(contents):
     whole_string = contents
     word_split = whole_string.split()
     word_list = str(word_split)
     word_list = word_list.lower()
     char_dict = {}
     for char in word_list:
        if char in char_dict:
             char_dict[char] += 1
        else:
             char_dict[char] = 1
     return char_dict

def get_chars_dict(char_dict):
     sorted_list_of_dicts = []
     for char in char_dict:
          if char.isalpha():
               count = char_dict[char]
               new_dict = {'char': char, 'num': count}
               sorted_list_of_dicts.append(new_dict)
     sorted_list_of_dicts.sort(reverse=True, key=sort_on)
     return sorted_list_of_dicts



def sort_on(dict):
     return dict["num"]

