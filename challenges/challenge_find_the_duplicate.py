def order_numbers(numbers):
    if not numbers:
        return numbers

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    left = list([num for num in numbers if num < pivot])
    middle = list([num for num in numbers if num == pivot])
    right = list([num for num in numbers if num > pivot])

    return order_numbers(left) + middle + order_numbers(right)


array = [1, 1]


def find_duplicate(nums):
    nums = order_numbers(nums)
    for i in range(len(nums) - 1):
        if isinstance(nums[i], str):
            return False
        if nums[i] < 0 or nums[i + 1] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
    raise NotImplementedError


print(find_duplicate(array))
