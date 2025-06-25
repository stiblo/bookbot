def count_book_words(book_content):
    try:
        list_of_words = book_content.split()
        return len(list_of_words)
    except Exception as e:
        return f"ERROR: {e}"
    
def count_book_chars(book_content):
    count_result = {}
    list_of_words = book_content.split()
    try:
        for word in list_of_words:
            for letter in word:
                lower_letter = letter.lower()
                if lower_letter not in count_result:
                    count_result[lower_letter] = 1
                elif lower_letter in count_result:
                    count_result[lower_letter] += 1
        print(count_result)
    except Exception as e:
        return f"ERROR: {e}"
        