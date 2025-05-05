// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn delete_middle(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none()||head.as_ref().unwrap().next.is_none(){
            return None; 
        }
        let mut dummy=Box::new(ListNode::new(0));
        dummy.next=head;
        let mut count=0;
        let mut curr=dummy.next.as_ref();
        while let Some(node)=curr{
            count+=1;
            curr=node.next.as_ref();
        }
        let middle_idx=count/2;
        let mut prev=&mut dummy;
        for i in 0..middle_idx{
            prev=prev.next.as_mut().unwrap();
        }
        let next_middle=prev.next.as_mut().unwrap().next.take();
        prev.next=next_middle;
        dummy.next
    }
}

//QED
//Problem 2095 - (Medium of Delete The Middle Node Of A Linked List) - Jason Balayev (rust)