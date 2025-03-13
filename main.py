from stats import num_of_words, char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    try:
        content = get_book_text(sys.argv[1])
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    num_of_words(content)
    print("--------- Character Count -------")
    chars = char_count(content)
    for x in chars:
        for k, v in x.items():
            if k.isalpha():
                print(f"{k}: {v}")
    print("============= END ===============")

main()
