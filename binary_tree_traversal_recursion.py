# pre-order binary tree traversal
# implemented using recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        
        traversed = [root.val]

        if root.left:
            traversed += self.preorderTraversal(root.left)

        if root.right:
            traversed += self.preorderTraversal(root.right)

        return traversed

        
# in-order binary tree traversal
# implemented using recursion

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        traversed = []
        root_cache = None # caching speeds the code up
        
        if root.left:
            root_cache = root.val
            traversed += self.inorderTraversal(root.left)
            traversed += [root_cache]
            
        else:
            traversed += [root.val]
        
        if root.right:
            traversed += self.inorderTraversal(root.right)
        
        return traversed


# post-order binary tree traversal
# implemented using recursion

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        traversed = []
        
        if root.left:
            traversed += self.postorderTraversal(root.left)
        
        if root.right:
            traversed += self.postorderTraversal(root.right)
        
        traversed += [root.val]
        
        return traversed
