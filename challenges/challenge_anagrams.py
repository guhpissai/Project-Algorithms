def order_string(string):
    if len(string) <= 1:
        return string

    pivot = string[len(string) // 2]
    left = ''.join([char for char in string if char < pivot])
    middle = ''.join([char for char in string if char == pivot])
    right = ''.join([char for char in string if char > pivot])

    return order_string(left) + middle + order_string(right)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return tuple([first_string, second_string, False])

    first_ordered = order_string(first_string)
    second_ordered = order_string(second_string)

    return tuple([
        first_ordered, second_ordered, first_ordered == second_ordered])

    raise NotImplementedError
