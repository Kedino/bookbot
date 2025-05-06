import sys
from stats import get_book_text, get_wordcount, get_character_count, get_character_count_sorted

def main():
    if len(sys.argv) != 2:
        print("Incorrect command format")
        print("Usage: python3 main.py <path_to_book>")
        print("Example: python3 main.py books/frankenstein.txt")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    wordcount = get_wordcount(text)
    sorted_wordcount = get_character_count_sorted(get_character_count(text))
    print_report(wordcount, sorted_wordcount, filepath)
    

def print_report(word_count, sorted_chars, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character on a new line
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")

main()