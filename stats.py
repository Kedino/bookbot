def get_book_text (filepath = "books/frankenstein.txt"):
    with open(filepath) as file:
        text = file.read()
    return text

def get_wordcount(text):
    wordcount = len(text.split())
    return wordcount

def get_character_count(text):
    lower_case = text.lower()
    letter_dictionary = {}
    
    # Using .get() method for more concise code
    for letter in lower_case:
        letter_dictionary[letter] = letter_dictionary.get(letter, 0) + 1
    
    # Original solution:
    # for letter in lower_case:
    #     if letter in letter_dictionary:
    #         letter_dictionary[letter] += 1
    #     else:
    #         letter_dictionary[letter] = 1
    
    return letter_dictionary

def sort_on(dict):
    return dict["num"]

def get_character_count_sorted(letter_dictionary):
    sorted_letter_list = []
    for letter, count in letter_dictionary.items():
        if letter.isalpha():
            sorted_letter_list.append({"char": letter, "num": count})
    sorted_letter_list.sort(reverse=True, key=sort_on)
    return sorted_letter_list


