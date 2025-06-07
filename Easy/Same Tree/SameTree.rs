// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match(p,q){
            (None,None)=>true,
            (Some(node_p),Some(node_q))=>{
                let p_ref=node_p.borrow();
                let q_ref=node_q.borrow();
                p_ref.val==q_ref.val 
                    && Solution::is_same_tree(p_ref.left.clone(),q_ref.left.clone())
                    && Solution::is_same_tree(p_ref.right.clone(),q_ref.right.clone())
            }
            _=>false,
        }
    }
}

//QED
//Problem 100 (Easy of Same Tree) - Jason Balayev (rust)