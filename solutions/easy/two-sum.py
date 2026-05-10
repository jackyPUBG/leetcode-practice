"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

解題思路：
1. 要做什麼？找兩個數字加起來等於 target，回傳它們的 index
2. 需要什麼資料？兩個 index，nums 裡的值
3. 用什麼方法？雙層 for 迴圈，內層從 i+1 開始避免重複

學到的東西：
- 內層 range(i+1, len(nums)) 可以避免重複比較和同一個 index
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for a in range(i+1, len(nums)):
                if nums[i] + nums[a] == target:
                    return [i,a]
        return []
