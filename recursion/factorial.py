def factorial(num):
    if num < 0:
        return None  # Indicate an error for negative numbers
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def factorials(nums):
    return [factorial(num) if factorial(num) is not None else 'Error' for num in nums]


print(factorials([2, 3, 4]))  # should print: [2, 6, 24]
print(factorials([1, 5, 6]))  # should print: [1, 120, 720]
print(factorials([0, -3, 10]))  # should print: [1, 'Error', 3628800]