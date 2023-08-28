def is_palindrome_iterative(word):
    if not word:
        return False

    n = len(word)
    bol = list()

    for index in range(n):
        if word[index] == word[len(word) - index - 1]:
            bol.append(True)
        else:
            bol.append(False)

    result = set(bol)

    return False not in result

