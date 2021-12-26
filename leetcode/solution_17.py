'''
Summary

Attempt #1
Your own answer?: Yes
Time spent: 40m
Time Complexity: O(V+E) where V is the size of 'digits' string and E is the the size of 'digits' - 1
Runtime: 26 ms, faster than 85.26% of Python3 online submissions for Letter Combinations of a Phone Number.
Space Complexity: O(V) where V is the size of 'digits' string
Memory Usage: 14.4 MB, less than 33.48% of Python3 online submissions for Letter Combinations of a Phone Number.
'''

import sys
from typing import List
input = sys.stdin.readline



class Solution:
    def __init__(self) -> None:
        digits = "23"
        print(self.letterCombinations(digits))

    def letterCombinations(self, digits: str) -> List[str]:
        digits_size = len(digits)
        if digits_size == 0:
            return []
        
        digits_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = []

        def dfs(curr_idx: int, end_idx: int, tmp_strg: str):
            if curr_idx == end_idx:
                digit = digits[curr_idx]
                letters = digits_dict[digit]
                for letter in letters:
                    ans.append(tmp_strg + letter)
                return

            digit = digits[curr_idx]
            letters = digits_dict[digit]
            for letter in letters:
                dfs(curr_idx + 1, end_idx, tmp_strg + letter)

        dfs(0, digits_size - 1, "")
        return ans

Solution()