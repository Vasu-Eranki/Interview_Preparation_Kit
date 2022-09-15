# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        all_heads = recursive_solution(head)
        return(all_heads)
    
def recursive_solution(linked_list):
    if(linked_list==None ):
        return 
    if(linked_list.next==None):
        return linked_list
    else:
        result = recursive_solution(linked_list.next)
        linked_list.next.next = linked_list
        linked_list.next = None
        return result
        
