/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaves1;
        vector<int> leaves2;
        getLeaves(root1,leaves1);
        getLeaves(root2,leaves2);
        return leaves1==leaves
    }
    void getLeaves(TreeNode* root, vector<int>& leaves){
        if(!root) return;
        if (!root->left&&!root->right){
            leaves.push_back(root->val);
        }
        getLeaves(root->left,leaves);
        getLeaves(root->right,leaves);
    }
};

//QED
//Problem 872 (Leaf-Similar Trees) - Jason Balayev (cpp)