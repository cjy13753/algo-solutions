'''
Summary - Attempt #1 PASS

Your own answer?: Yes
Difficulty: Leetcode Medium
Time Spent: 68m

Time Complexity: O(n^4)
Space Complexity: O(n^4) 
※ where n is the length of the given string s and len(s) <= 20, 
therefore the effective time and space complexities are reduced to O(1).

Runtime: 54 ms, faster than 44.93% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 13.9 MB, less than 83.77% of Python3 online submissions for Restore IP Addresses.
'''

from itertools import combinations
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        if len(s) < 4 or len(s) > 12:
            return ans

        for c in s:
            if c.isdigit() is False:
                return ans
        
        indices = range(1, len(s))
        candidates = list(combinations(indices, 3))

        for candidate in candidates:
            newCandidate = [0]
            newCandidate.extend(candidate)
            charNums = []
            first = s[newCandidate[0]:newCandidate[1]]
            second = s[newCandidate[1]:newCandidate[2]]
            third = s[newCandidate[2]:newCandidate[3]]
            fourth = s[newCandidate[3]:]
            charNums = [first, second, third, fourth]
            temp = []
            for charNum in charNums:
                if len(charNum) > 1:
                    if charNum[0] == '0':
                        continue
                    elif int(charNum) > 255:
                        continue

                temp.append(charNum)
            if len(temp) == 4:
                ans.append('.'.join(temp))

        return ans

testcases = ["25525511135", "0000", "101023", "123"]
sol = Solution()
for testcase in testcases:
    print(sol.restoreIpAddresses(testcase))