"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


"""
* `if not root:`: This is an `if` statement that checks if the `root` parameter is `None` (i.e., if there's no tree node). If `root` is `None`, it means that there's no tree, so the method immediately returns 0, indicating that the tree's depth is 0.


* `return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1`: If the `root` is not `None`, this line calculates the maximum depth of a binary tree recursively:

   - `self.maxDepth(root.left)`: This is a recursive call to the `maxDepth` method on the left subtree of the current `root`. It calculates the maximum depth of the left subtree.

   - `self.maxDepth(root.right)`: Similarly, this is a recursive call to the `maxDepth` method on the right subtree of the current `root`. It calculates the maximum depth of the right subtree.

   - `max(...)`: The `max` function is used to find the maximum value between the depths of the left and right subtrees.

   - `+ 1`: After finding the maximum depth of the left and right subtrees, 1 is added to account for the current level (the level of the current `root` node).

   - `return`: The final result, which is the maximum depth of the binary tree rooted at the current `root`, is returned.

In summary, this code defines a class method `maxDepth` for calculating the maximum depth of a binary tree. It does this by recursively traversing the tree, finding the maximum depth of the left and right subtrees, and adding 1 for the current level. If the `root` is `None`, it returns 0 as there is no tree.
"""
