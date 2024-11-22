# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        dummyNode = ListNode()
        currNode = dummyNode

        while list1 and list2:
            if list1.val <= list2.val:
                currNode.next = list1
                currNode = currNode.next
                list1 = list1.next
            else:
                currNode.next = list2
                currNode = currNode.next
                list2 = list2.next
 
        if list1:
            currNode.next = list1
        elif list2:
            currNode.next = list2
        
        return dummyNode.next



        