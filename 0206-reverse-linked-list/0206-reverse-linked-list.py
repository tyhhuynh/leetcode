# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head 

        while current:
            next_node = current.next # pointer for next node after current
            current.next = prev # links node backwards to prev
            prev = current # prev iterates forward
            current = next_node # current becomes the next node
        return prev # points to last node of OG LL / new head of reversed LL