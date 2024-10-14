def find_anagram_words(list_1, list_2):
    sorted1 = set(tuple(sorted(word)) for word in list_1)
    sorted2 = set(tuple(sorted(word)) for word in list_2)

    common_words = sorted1 & sorted2
    list1 = [word for word in list_1 if tuple(sorted(word)) in common_words]
    list2 = [word for word in list_2 if tuple(sorted(word)) in common_words]
    output = []
    for word1 in list1:
        for word2 in list2:
            if tuple(sorted(word1)) == tuple(sorted(word2)):
                output.append((word1, word2))
                break
    if not output:
        return "No anagrams found"
    else:
        return output


print(find_anagram_words(['cinema', 'ama', 'ok'], ['iceman', 'maa','shoe','eansb']))  # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett']))  # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir']))  # should return []
