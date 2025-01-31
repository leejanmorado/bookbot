def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for i in get_char_count_list(chars_dict):
        print(f"The '{i["char"]}' character was found {i["count"]} times")
    
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_char_count_list(char_dict):
    chars = []
    for char in char_dict:
        if char.isalpha():
            chars.append({"char": char, "count": char_dict[char]})
        else:
            continue
    chars.sort(reverse=True, key=lambda c : c["count"])

    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
