# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        header_list = recursion_list(list1,list2)
        return header_list
        
def recursion_list(a,b):
    temp = ListNode(None,None)
    if(a):
        if(b):
            if(a.val>=b.val):
                temp.val = b.val
                temp.next = recursion_list(a,b.next)
            else:
                temp.val = a.val
                temp.next = recursion_list(a.next,b)
        else:
            temp.val = a.val
            temp.next = recursion_list(None,a.next)
    elif(b):
        temp.val = b.val
        temp.next = recursion_list(None,b.next)
    else:
        return 
    return temp
