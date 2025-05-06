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
    pub fn odd_even_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none()||head.as_ref().unwrap().next.is_none(){
            return head;
        }
        let mut odd_dummy=Box::new(ListNode::new(0));
        let mut even_dummy=Box::new(ListNode::new(0));
        let mut odd_curr=&mut odd_dummy;
        let mut even_curr=&mut even_dummy;
        let mut curr=head;
        let mut idx=1;
        while let Some(mut node)=curr{
            curr=node.next.take();
            if idx%2==1{
                odd_curr.next=Some(node);
                odd_curr=odd_curr.next.as_mut().unwrap();
            }else{
                even_curr.next=Some(node);
                even_curr=even_curr.next.as_mut().unwrap();
            }
            idx+=1;
        }
        odd_curr.next=even_dummy.next;
        odd_dummy.next
    }
}

//QED
//Problem 328 - (Medium of Odd Even Linked List) - Jason Balayev (rust)