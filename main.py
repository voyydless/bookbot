from stats import get_word_count, get_character_count

def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    print(book_text)

if __name__ == "__main__": 
    file_contents = get_book_text("books/frankenstein.txt")
    print(get_word_count(file_contents))
    print(get_character_count(file_contents))
