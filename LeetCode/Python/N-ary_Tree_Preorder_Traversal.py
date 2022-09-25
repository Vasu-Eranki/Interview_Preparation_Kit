# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = dfs(root)
        return answer
        
def dfs(root):
    if(root ==None):
        return []
    visited = deque([root])
    answer = []
    while(visited):
        p = visited.popleft()
        answer.append(p.val)
        for i in reversed(p.children):
            visited.appendleft(i)
    return answer
