def count_items(nums):
    if nums == []:
        return 0

    return 1 + count_items(nums[1:])

print(count_items([2,14,1]))