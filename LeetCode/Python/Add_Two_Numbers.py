# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        results = solution(l1,l2,0)
        return results
def solution(l1,l2,carry):
    temp = ListNode(None,None)
    total_sum = carry
    if(l1 or l2):
        if(l1):
            total_sum+=l1.val
        else:
            l1 = ListNode(None,None)
        if(l2):
            total_sum+=l2.val
        else:
            l2 = ListNode(None,None)
        remainder = total_sum%10
        carry = total_sum//10
        temp.val = remainder
        temp.next = solution(l1.next,l2.next,carry)
    else:
        if(carry>0):
            temp.val = carry
            return temp
        else:
            return 
    return temp
