def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    print_a_report(book_path, num_words, chars_dict)
    
def sort_on(dict):
    return dict["num"]
	
def print_a_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    chars_list = []
    for char in chars_dict:
        chars_list.append({"char": char, "num": chars_dict[char]})
    chars_list.sort(reverse=True, key=sort_on)
    for item in chars_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print(f"--- End Report ---")
    

def get_num_characters(text):
    lowered_text = text.lower()
    characters = {}
    for char in lowered_text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return(characters)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
