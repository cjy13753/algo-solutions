# Solutions to algorithm problems in [baekjoon](https://www.acmicpc.net/problemset) and [leetcode](https://leetcode.com/problemset/all/)

For python code snippet generation in VS Code, refer to this [codepen work](http://codepen.io/mrmlnc/pen/GqrqPg) to make template code into multiple strings separated by comma. This needs sign-up for the website.

# Time complexity brief reminder
- Topological Sort w/ BFS
    - Time Complexity
        - O(V + E) because you loop through all vertices to find ones with 0 indegree and then remove edges extending from 0 indgree nodes.
    - Space Complexity
        - O(V) where V is the number of vertices