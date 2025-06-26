# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = ListNode(0) # temp marker indicating start
        current = tempNode

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next # after attaching node, move current forward

        current.next = list1 if list1 else list2 # move current forward depending on which list is non-empty
        return tempNode.next # current tempNode is marker, tempNode.next is actual head