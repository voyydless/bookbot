def get_word_count(file_contents):
    num_words = len(file_contents.split())
    return f"{num_words} words found in the document"

def get_character_count(file_contents):
    to_count = file_contents.lower()
    count = {}
    for letter in to_count:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    return count