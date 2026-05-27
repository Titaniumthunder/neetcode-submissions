class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq1 = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for j in t:
            if j in freq1:
                freq1[j] += 1
            else:
                freq1[j] = 1
        return freq == freq1


