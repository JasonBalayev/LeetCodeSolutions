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
    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let mut vals=Vec::new();
        let mut curr=head;
        while let Some(node)=curr{
            vals.push(node.val);
            curr=node.next;
        }
        let n=vals.len();
        let mut max_twin=0;
        for i in 0..(n/2){
            let twin=vals[i]+vals[n-1-i];
            max_twin=max_twin.max(twin);
        }
        max_twin
    }
}

//QED
//Problem 2130 - (Medium of Maximum Twin Sum Of A Linked List) - Jason Balayev (rust)