
lower_counts = {}
letter_list = []
dict_a = {}
dict_b = []


#The main funcion reads the contents of Frankenstein

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        

    word_count = wordcount(file_contents)
    print(f"{word_count} words found in the document\n")

    #charcount(file_contents)
    alpha_only(file_contents)
    alpha_dict(file_contents)
    list_of_dicts(file_contents)

    print("--- End report ---")

#The wordcount function counts every word in the book.
def wordcount(book_text):
    words = book_text.split()
    word_counts = len(words)
    return word_counts
    

# #The charcount function counts each individual letter, character, and space
# def charcount(book_text):
#     lower_case = list(book_text.lower())
#     for letter in lower_case:
#         if letter not in lower_counts:
#             lower_counts[letter] = 1
#         else:
#             lower_counts[letter] += 1
#     print(lower_counts)
        

#The alpha_only function removes special characters and only returns letters
def alpha_only(book_text):
    lower_case = list(book_text.lower())
    for i in lower_case:
        if i.isalpha() == True:
            letter_list.append(i)
    return letter_list

#The alpha_dict function creates a new dictionary with only letters and their counts
def alpha_dict(book_text):
    for letter in letter_list:
        if letter not in dict_a:
            dict_a[letter] = 1
        else:
            dict_a[letter] += 1

#This is a function that takes a dictionary and returns the vale of the "num" key
#This is how the ' .sort()' method knows how to sort the list of dictionaries

def sort_on(dict):
    return dict["num"]


#This converts the dictionary to a list of dictionaries
def list_of_dicts(book_text):
    for key, value in dict_a.items():
        dict_b.append({"char": key, "num": value})
        dict_b.sort(reverse=True, key=sort_on)

    for letter in dict_b:
        print(f"The '{letter["char"]}' character was found {letter["num"]} times.")






if __name__ == "__main__":
    main()

