# Majority Element search:
# use case: A voting system
def major_element(list):
    element_count = {}
    for e in list:
        element_count[e] = element_count.get(e, 0) + 1
        if element_count[e] > len(list) // 2:
            return e
    return "No majority found"

test = [4,4,4,3,3,2,2,1]
print(major_element(test))