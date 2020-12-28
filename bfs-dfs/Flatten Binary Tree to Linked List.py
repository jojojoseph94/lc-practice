"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

Solution : Recursive - Keep going left. Once you can't go left anymore, put the left child to the right and put the right child at the right most end of left child.
                        Then repeat the flattening original right subtree.

                    Time complexity : O(N)
                    Space complexity: O(N)

            Iterative : TODO
"""

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        #keep going left
        if root.left:
            self.flatten(root.left)
        #cannot go left anymore
        left = root.left
        right = root.right
        if left:
            root.left = None
            right = root.right
            root.right = left
            while left.right:
                left = left.right
            left.right = right
        self.flatten(right)