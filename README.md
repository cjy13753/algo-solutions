# Solutions to algorithm problems in [baekjoon](https://www.acmicpc.net/problemset) and [leetcode](https://leetcode.com/problemset/all/)

For python code snippet generation in VS Code, refer to this [codepen work](http://codepen.io/mrmlnc/pen/GqrqPg) to make template code into multiple strings separated by comma. This needs sign-up for the website.

# Time complexity brief reminder
- Topological Sort w/ BFS
    - Time Complexity
        - O(V + E) because you loop through all vertices to find ones with 0 indegree and then remove edges extending from 0 indgree nodes.
    - Space Complexity
        - O(V) where V is the number of vertices

# Code Snippet for python3
- Custom descending sorting order
``` python3
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
```
