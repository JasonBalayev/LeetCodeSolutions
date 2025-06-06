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
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if nums.is_empty(){
            return None;
        }
        Self::build_bst(&nums,0,nums.len()-1)
    }
    fn build_bst(nums:&Vec<i32>,left:usize,right:usize)->Option<Rc<RefCell<TreeNode>>>{
        if left>right{
            return None;
        }
        let mid=left+(right-left)/2;
        let mut root=TreeNode::new(nums[mid]);
        if mid>0{
            root.left=Self::build_bst(nums,left,mid-1);
        }
        if mid<right{
            root.right=Self::build_bst(nums,mid+1,right);
        }
        Some(Rc::new(RefCell::new(root)))
    }
}

//QED 
//Problem 108 (Easy of Convert Sorted Array To Binary Search Tree) - Jason Balayev (rust)