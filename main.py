from stats import get_num_words
from stats import get_char_count
import sys

def get_book_text(file_path):
    file_string = None
    with open(file_path) as f:
        file_string = f.read()
    return file_string

def report(word_count, char_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_count:
        print(f"{char}: {char_count[char]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    report(get_num_words(book_text), get_char_count(book_text))

main()