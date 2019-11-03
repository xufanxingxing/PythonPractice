# design a service to return all anagrams of a given string

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        

        d = {}

        for c in p:
            d[c] = d.get(c,0) + 1

        r = 0
        l = 0
        count = 0
        res = []

        while r < len(s):
            cr = s[r]
            cl = s[l]

            if cr in d.keys():
                d[cr] = d.get(cr) - 1
                if d[cr] >= 0:
                    count += 1

            if r >= len(p):
                if cl in d.keys():
                    d[cl] = d.get(cl) + 1
                    if d[cl] > 0:
                        count -= 1
                l += 1

            if count == len(p):
                res.append(l)

            r += 1

        return res











