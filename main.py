def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count = word_count(text)
    letterc = letter_count(text)
    report(book_path,count)
    print(letterc)

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    text_lower = text.lower()
    letter_dict = {}
    for letter in ''.join("abcdefghijklmnopqrstuvwxyz"):
        count = text_lower.count(letter)
        if count != 0:
            letter_dict[letter] = count
    return letter_dict

def report(book_path,count):
    print(f"--- Begin report of {book_path} ---")
    print(f"The number of words in the text is {count}\n\n")



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


#"Official" Solution for easy reference
#def get_chars_dict(text):
#    chars = {}
#    for c in text:
#        lowered = c.lower()
#        if lowered in chars:
#            chars[lowered] += 1
#        else:
#            chars[lowered] = 1
#    return chars