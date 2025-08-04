from collections import defaultdict

def groupAnagrams(words):
    result = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        result[key].append(word)
    return list(result.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
