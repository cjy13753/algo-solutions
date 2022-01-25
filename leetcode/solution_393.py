'''
Summary - Attempt #1

Your own answer?: Yes
Time spent: 65m

Time complexity: O(N)
Runtime: 112 ms, faster than 74.16% of Python3 online submissions for UTF-8 Validation.
Space complexity: O(1)
Memory Usage: 14.5 MB, less than 64.11% of Python3 online submissions for UTF-8 Validation.
'''

import sys
from typing import List
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        data = [145]
        print(self.validUtf8(data))

    def validUtf8(self, data: List[int]) -> bool:
        def validateFirstTwoBits(num):
            if num & 1<<7 != 0 and num & 1<<6 == 0:
                return True
            else:
                return False

        i = 0
        bit_mask = 1<<7
        while i < len(data):
            cnt = 0
            iter_mask = bit_mask
            present_bit = data[i] & iter_mask
            if present_bit != 0:
                cnt += 1
                iter_mask = iter_mask>>1
                present_bit = data[i] & iter_mask
                while present_bit != 0:
                    cnt += 1
                    iter_mask = iter_mask>>1
                    present_bit = data[i] & iter_mask
                if cnt == 1 or cnt >4:
                    return False
                j = 0
                while j < cnt - 1:
                    i += 1
                    if i >= len(data):
                        return False
                    if not validateFirstTwoBits(data[i]):
                        return False
                    j += 1
            i += 1
                    
        return True

Solution()