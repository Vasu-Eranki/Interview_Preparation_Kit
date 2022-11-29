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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool answer = recursive_solution(p,q);
        return answer; 
    }
    bool recursive_solution(TreeNode* p,TreeNode *q)
    {
        if(p==nullptr &&q==nullptr)
        {
            return true; 
        }
        if(p!=nullptr&& q!=nullptr)
        {
            return recursive_solution(p->left,q->left)&& recursive_solution(p->right,q->right)&& (p->val==q->val);
        }
        else
        {
            return false;
        }
    }
};
