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
        return count_result
    except Exception as e:
        return f"ERROR: {e}"

def sort_on(items):
    return items["nums"]

def sorted_char_count(book_chars_dict):
    sorted_list = []
    try:
        for book_char in book_chars_dict:
            sorted_list.append({"char": book_char, "nums": book_chars_dict[book_char]})
        sorted_list.sort(reverse=True, key=sort_on)
        return sorted_list      
    except Exception as e:
        return f"ERROR: {e}"