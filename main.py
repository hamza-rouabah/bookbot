from stats import get_num_words, get_char_num
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("--------- Character Count -------")
    num_words = get_num_words(get_book_text(path_to_book))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_char_num(get_book_text(path_to_book))
    for key in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{key[0]}: {key[1]}")
        
if __name__=="__main__":
    main()