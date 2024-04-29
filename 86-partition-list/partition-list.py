# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyNode1 = ListNode(1)
        dummyNode2 = ListNode(1)
        
        lessThanList = dummyNode1
        moreThanList = dummyNode2
        
        currentNode = head
        
        while currentNode:
            if currentNode.val < x:
                lessThanList.next = currentNode
                lessThanList = lessThanList.next
            else:
                moreThanList.next = currentNode
                moreThanList = moreThanList.next
                
            currentNode = currentNode.next
            
        lessThanList.next = dummyNode2.next
        moreThanList.next = None
        
        return dummyNode1.next