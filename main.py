from stats import count_book_words

def main():
    book_text_string = get_book_text("books/frankenstein.txt")
    book_word_count = count_book_words(book_text_string)
    print (f"{book_word_count} words found in the document")

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

