# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length = recursive_solution(root)
        return length
        
def recursive_solution(root):
    l_left = 0
    l_right =0
    if(not root):
        return 0
    elif(not root.left) and ( not root.right):
        return 1
    else:
        if(root.left):
            l_left = 1+recursive_solution(root.left)
        if(root.right):
            l_right = 1+recursive_solution(root.right)
    return max(l_left,l_right)
    
