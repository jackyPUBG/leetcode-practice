"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""."""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                break
        return "".join(prefix)

"""
zip(*strs): iterate through the same position of multiple strings/lists simultaneously.
* (unpacking): expands a list into individual elements.
ex: nums = [1,2,3], print(*nums) >>> 1 2 3

set(): removes duplicates. If len(set(chars)) == 1, all elements are the same.
ex: set(['f','f','f']) >>> {'f'}
"""
    
