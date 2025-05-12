def get_word_count(file_contents):
    num_words = len(file_contents.split())
    return num_words

def get_character_count(file_contents):
    to_count = file_contents.lower()
    count = {}
    for letter in to_count:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    return count

def get_sorted_count(file_contents):
    count = get_character_count(file_contents)
    
    sorted_count = sorted(count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    sorted_count = dict(sorted_count)

    return sorted_count
