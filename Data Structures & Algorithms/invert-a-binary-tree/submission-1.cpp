
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;

        swap(root->left,root->right);
        invertTree(root->right);
        invertTree(root->left);

        return root;
    }
};
