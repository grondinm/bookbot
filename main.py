def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count = word_count(text)
    print(f"The number of words in the text is {count}")

def word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()