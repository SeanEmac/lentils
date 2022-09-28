# Easy
# Arrays & Hashing

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false
    
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Build up a dict of letter frequencies and make sure they mach, eg
# sLetterCount = {
#   'r': 1,
#   'a': 1,
#   't': 1
# }
# sLetterCount = {
#   'c': 1,
#   'a': 1,
#   'r': 1
# }

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # Anagrams must be the same number of characters
    if len(s) != len(t):
        return False
    
    sLetterCount = {}
    tLetterCount = {}

    # Count the number of times each character appears
    for char in s:
        if char in sLetterCount:
            sLetterCount[char] = sLetterCount[char] + 1
        else:
            sLetterCount[char] = 1

    # Do it for both strings
    for c in t:
        if c in tLetterCount:
            tLetterCount[c] = tLetterCount[c] + 1
        else:
            tLetterCount[c] = 1
    
    # If it's an anagram, the dicts should be equal
    return sLetterCount == tLetterCount
        
            