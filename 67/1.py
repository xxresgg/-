
def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if nums[j] > nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


grades = [14, 2, 5, 3, 5, 4, 31]
print(selection_sort(grades))
