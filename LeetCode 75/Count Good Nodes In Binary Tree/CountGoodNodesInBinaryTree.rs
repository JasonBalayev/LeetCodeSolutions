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
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node:&Option<Rc<RefCell<TreeNode>>>,max_path:i32)->i32{
            match node{
                None=>0,
                Some(n)=>{
                    let node_ref=n.borrow();
                    let curr=node_ref.val;
                    let good=if curr>=max_path{1} else {0};
                    let new_max=curr.max(max_path);
                    let left=dfs(&node_ref.left,new_max);
                    let right=dfs(&node_ref.right,new_max);
                    good+left+right
                }
            }
        }
        dfs(&root,std::i32::MIN)
    }
}

//QED
//Problem 1448 (Medium of Count Good Nodes In Binary Tree) - Jason Balayev (rust)