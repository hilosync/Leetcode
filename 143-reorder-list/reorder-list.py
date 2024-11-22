# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return None
        
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        if length <= 2:
            return None
        
        curr = head
        for i in range((length)//2):
            curr = curr.next
        
        newList = curr.next
        curr.next = None

        prev = None    
        while newList:
            temp = newList.next
            newList.next = prev
            prev = newList
            newList = temp
        newList = prev

        curr = head
        while newList:
            temp = newList.next
            curr.next, newList.next = newList, curr.next
            newList = temp
            curr = curr.next.next
        
        return None
        
        

        

