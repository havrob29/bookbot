def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    dict_lettercount = count_letters(text)
    list_lettercount = convert_dict(dict_lettercount)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for i in list_lettercount:
        print(f"The {i[0]} character was found {i[1]} times")
    print("--- End report ---")

def convert_dict(dict):
    lst_lettercount = list(dict.items())
    sorted_lst = []
    for i in lst_lettercount:
        if i[0].isalpha() == True:
            sorted_lst.append(i)
    sorted_lst = sorted(sorted_lst, key = lambda x:x[1], reverse=True)
    return sorted_lst

def number_of_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    dictionary = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in dictionary:
            dictionary[lowered] += 1
        else:
            dictionary[lowered] = 1
    return dictionary

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
