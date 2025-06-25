def count_book_words(book_content):
    try:
        list_of_words = book_content.split()
        return len(list_of_words)
    except Exception as e:
        return f"ERROR: {e}"