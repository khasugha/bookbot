def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    get_num_characters(text)

def get_num_characters(text):
    lowered_text = text.lower()
    characters = {}
    for char in lowered_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    print(characters)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
