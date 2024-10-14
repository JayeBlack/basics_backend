print("LIST COMPREHENSION")
print("*********************************")


def filter_list(_):
    even = [e for e in _ if e % 2 == 0]
    odd = [odd ** 2 for odd in _ if odd not in even]
    return f"Given this list {_}\nEven numbers in the list: {sorted(even)} \nOdd numbers squared in the list: {odd}"


print(filter_list([1, 3, 4, 5, 2, 6]))

print("                    ")
print("LAMBDA EXPRESSIONS")
print("*********************************")
first = [1, 2, 3]
second = [4, 5, 6]
letters = ["a", "b", "c"]
example1 = list(map(lambda x, y: x * y, first, second))
example2 = (lambda x, y: list(x) + list(y))
print(example1)
print(example2(first, letters))

print("                    ")
print("FIBONACCI SERIES")
print("*********************************")


def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 5
result = list(fibo(n))
print(f"The first {n} fibonacci numbers:{result}")
