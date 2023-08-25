def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if word[low_index] == word[high_index]:
        try:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        except IndexError:
            return True
    else:
        return False
