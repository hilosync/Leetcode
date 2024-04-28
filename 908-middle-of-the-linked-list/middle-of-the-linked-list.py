# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        currentNode = head
        while currentNode:
            currentNode = currentNode.next
            length += 1

        currentNode = head

        for _ in range(int(length/2)):
            currentNode = currentNode.next
        
        return currentNode

        