import sys
from typing import List
from collections import defaultdict
input = sys.stdin.readline

class Solution:
    def __init__(self) -> None:
        strs = ["eat","tea","tan","ate","nat","bat"]
        self.groupAnagrams(strs)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for string in strs:
            lowercaseArray = [0] * 26
            for character in string:
                lowercaseArray[ord(character) - ord('a')] += 1
            store[str(lowercaseArray)].append(string)
        
        result = []
        for item in store.values():
            result.append(item)

        return result


Solution()