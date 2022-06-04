# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = recursive_solution(head,1)
        return head
        
def recursive_solution(head,counter):
    if(head):
        if(counter%2)!=0:
            if(head.next):
                temp = head.val
                head.val = get_value(head.next)
                head.next = insert_value(head.next,temp)
                head.next = recursive_solution(head.next,counter+1)
            else:
                return head
        else:
            if(head.next):
                head.next = recursive_solution(head.next,counter+1)
            else:
                return head
        return head
    else:
        return
def get_value(head):
    return head.val
def insert_value(head,value):
    head.val = value
    return head
