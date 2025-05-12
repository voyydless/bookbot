from stats import get_word_count, get_character_count, get_sorted_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def main():
    path_to_file = path_to_book
    book_text = get_book_text(path_to_file)

    file_contents = get_book_text(path_to_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing words found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file_contents)} total words")
    print("--------- Character Count -------")
    for char in get_sorted_count(file_contents):
        num = get_sorted_count(file_contents)[char]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    main()