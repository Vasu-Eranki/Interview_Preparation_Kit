# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = hash_map(head)
        return answer
    

def hash_map(linked_list):
    hash_map = {}
    while(linked_list):
        if(linked_list in hash_map):
             return linked_list
        hash_map[linked_list] = 0
        linked_list = linked_list.next
    return None
