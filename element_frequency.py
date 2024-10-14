from collections import Counter

say = [2, 2, 3, 3, 3, 4, 1]
# USING DICTIONARIES
frequency = {}
for item in say:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)
# USING COLLECTIONS.COUNTER
counter = Counter(say)
print(counter)

#USING LIST COMPREHENSION
list_com = {item: say.count(item) for item in set(say)}
print(list_com)