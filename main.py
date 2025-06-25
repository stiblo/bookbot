def main():
    print(get_book_text("books/frankenstein.txt"))

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

