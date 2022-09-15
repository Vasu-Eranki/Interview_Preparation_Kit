# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = get_len(head)
        head = get_mid(head,ceil(length/2))
        return head
def get_len(head):
    if( not head):
        return -1
    length = 1+get_len(head.next)
    return length
def get_mid(head,length):
    if(length==0):
        return head
    head = get_mid(head.next,length-1)
    return head
