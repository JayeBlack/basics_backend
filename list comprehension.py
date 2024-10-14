## A simple list
numbers = [x for x in range(10)]
print(numbers)

##Square
squares = [x**2 for x in range(10)]
print(squares)
def exclusive_products(inventory1, inventory2):
    # implement this
    set1, set2 = set(inventory1), set(inventory2)
    set1 = {item.upper() for item in set1}
    set2 = {item.upper() for item in set2}
    result1 = set1 - set2
    result2 = set2 - set1
    result1 = sorted(list(result1))
    result2 = sorted(list(result2))
    return result1, result2


inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
