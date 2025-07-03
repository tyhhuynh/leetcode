# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one, two = head, head
        
        while two and two.next:
            one = one.next
            two = two.next.next

        if two == None or two.next == None:
            return one
        
        # if two.next == None:
        #     return one
        

