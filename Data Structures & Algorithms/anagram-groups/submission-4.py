class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = "".join(sorted(word))  # "cat" → "act"
            if key not in group:
                group[key] = []          # new group, start empty list
            group[key].append(word)      # add original word to group
        return list(group.values())  