# https://www.youtube.com/watch?v=eDmxPfVa81k&ab_channel=GregHogg


from collections import defaultdict     # default dict can add key:value pair automatically.

def groupAnagram(words):
    anagram_dict = defaultdict(list)
    for word in words:
        count = [0] * 26
        for char in word:
            # here assocating char with index
            count[ord(char) - ord("a")] += 1
        # list cannot be key of a dict, tuple can be.
        key = tuple(count)
        anagram_dict[key].append(word)
    return anagram_dict.values()


words = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(words))
