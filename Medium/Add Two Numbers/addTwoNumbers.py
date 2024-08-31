# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # What is a Dummy Head/Node?
        # https://stackoverflow.com/questions/37324972/what-is-a-dummy-head
        dummy_head = ListNode(0)
        newTail = dummy_head
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = carry + x + y
            carry = total // 10
            newTail.next = ListNode(total%10)
            newTail = newTail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next
    
#QED
#Problem 2 (Add Two Numbers) - Jason Balayev (java)