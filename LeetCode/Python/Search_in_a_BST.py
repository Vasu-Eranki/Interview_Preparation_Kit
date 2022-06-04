# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        result = recursive_solution(root,val)
        return result
    
def recursive_solution(root,val):
    result = None
    if(not root):
        return None
    if(root.val==val):
        return root
    elif(root.val<val):
        return recursive_solution(root.right,val)
    else:
        return recursive_solution(root.left,val)
