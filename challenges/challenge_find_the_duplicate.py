def find_duplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if isinstance(nums[i], str):
            return False
        if nums[i] < 0 or nums[i + 1] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False