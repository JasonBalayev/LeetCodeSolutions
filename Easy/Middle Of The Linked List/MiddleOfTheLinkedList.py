# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count =  0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        middle_pos = count // 2
        curr = head

        for i in range(middle_pos):
            curr = curr.next
        return curr

#QED
#QED
#Problem 876 (Easy Of Middle Of The Linked List) - Jason Balayev (python)  
 
        