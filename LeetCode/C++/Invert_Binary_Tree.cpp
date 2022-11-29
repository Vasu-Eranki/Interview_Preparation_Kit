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
    TreeNode* invertTree(TreeNode* root) {
        TreeNode* answer = recursive_solution(root);
        return answer;
    }
    TreeNode* recursive_solution(TreeNode* root)
    {
        if(root!=nullptr)
        {
         if(root->right!=nullptr);
         {
            swap(root->right,root->left);
            root->left = recursive_solution(root->left);
            root->right = recursive_solution(root->right);
         } 
         
        }
        return root;
    }
};
