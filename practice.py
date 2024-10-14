def repeating_elements(nums):
    # implement this
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        seen.add(num)
    repeated = list(sorted(repeated))

    return repeated


print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
print(repeating_elements([-1, 2, 3, -1, 2, 3]))  # expected output : [-1, 2, 3]
print(repeating_elements([1, 2, 3, 4, 5]))  # expected output : []

