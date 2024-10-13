

def anagram(s, t):

    if len(s) != len(t):
        return False
    
    # sorted counts frequesncy of a character
    return sorted(s) == sorted(t)


# this is using frequency counter with dictionary.
class Solution:
    def char_freq(self, word):
        frequency = {}
        for char in word:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def anagram2(self, s, t):

        if len(s) != len(t):
            return False
        
        return self.char_freq(s) == self.char_freq(t)


s = "anagram"
t = "nagaram"

solution = Solution()

print(anagram(s, t))
print(solution.anagram2(s, t))

