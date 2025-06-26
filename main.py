from stats import count_book_words, count_book_chars, sorted_char_count

def main():
    book_text_string = get_book_text("books/frankenstein.txt")
    sorted_chars_list = sorted_char_count(count_book_chars(book_text_string))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_book_words(book_text_string)} total words")
    print("--------- Character Count -------")
    for sorted_char in sorted_chars_list:
        if sorted_char['char'].isalpha():
            print(f"{sorted_char['char']}: {sorted_char['nums']}")
    print("============= END ===============")

def get_book_text(book_file_path):
    try:
        with open(book_file_path) as f:
            book_contents = f.read()
            return book_contents
    except FileNotFoundError:
        return "ERROR: File not found"
    except Exception as e:
        return f"ERROR: {e}"
    
main()

