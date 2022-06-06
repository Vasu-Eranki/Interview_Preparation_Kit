# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        (head,_) = calc_len_and_removal(head,n)
        return head
    
def calc_len_and_removal(head,n):
    length = 1 
    if(head==None):
        return (None,0) 
    else:
        (head.next,length) = calc_len_and_removal(head.next,n)
        length = length+1
        if(length==n):
            return (head.next,length)
    return (head,length)
