# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_map = recursive_hashing(headA,{})
        get_intersection = recursive_mapping(headB,hash_map)
        return get_intersection
    

def recursive_hashing(root,hash_dict):
    if(not root):
        return hash_dict 
    hash_dict[root] = 1
    hash_dict = recursive_hashing(root.next,hash_dict)
    return hash_dict
    
def recursive_mapping(root,hash_dict):
    if(not root):
        return
    if(root in hash_dict):
        result = root
    else:
        result = recursive_mapping(root.next,hash_dict)
    return result
    
    
