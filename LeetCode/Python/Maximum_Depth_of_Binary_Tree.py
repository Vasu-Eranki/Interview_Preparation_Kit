# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length = recursive_solution(root,0)
        return length
        
def recursive_solution(root,depth):
    if(not root):
        return depth
    else:
        return max(recursive_solution(root.left,depth+1),recursive_solution(root.right,depth+1))
