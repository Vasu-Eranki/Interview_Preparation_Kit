# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = bfs(root)
        return answer
    
def bfs(root):
    if(root==None):
        return []
    graph = [root]
    answer = []
    while graph:
        length = len(graph)
        level  = []
        for _ in range(length):
            p = graph.pop()
            level.append(p.val)
            if(p.left):
                graph.insert(0,p.left)
            if(p.right):
                graph.insert(0,p.right)
        answer.append(level)
    return answer
