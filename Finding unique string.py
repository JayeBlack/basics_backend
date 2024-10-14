def find_unique_string(words):
    # implement this
    seen, duplicate = set(), set()
    for word in words:
        if word in seen:
            duplicate.add(word)
        else:
            seen.add(word)
    for word in words:
        if word not in duplicate:
            return word

    return "nothing"


print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string([]))  # It should print: ''