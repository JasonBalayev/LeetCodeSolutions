# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node=head
        while(current_node and current_node.next):
            if(current_node.next.val==current_node.val):
                current_node.next=current_node.next.next
                continue
            current_node=current_node.next
        return head

#QED
#Problem 83 (Easy Of Remove Duplicates from Sorted List) - Jason Balayev (python)