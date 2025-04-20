def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text:
        lower = char.lower()
        if lower in char_count:
            char_count[lower] += 1
        else:
            char_count[lower] = 1
    return char_count