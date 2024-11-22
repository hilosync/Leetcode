# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        currNode = head
        length = 0

        while currNode:
            length += 1
            currNode = currNode.next

        nodeToRemove = length - n
        
        if nodeToRemove < 0:
            return None
        if nodeToRemove == 0:
            return head.next
        
        currNode = head.next
        prevNode = head
        while nodeToRemove > 0:
            nodeToRemove -= 1
            if nodeToRemove == 0:
                prevNode.next = currNode.next
                currNode.next = None
                return head
            prevNode = currNode
            currNode = currNode.next
