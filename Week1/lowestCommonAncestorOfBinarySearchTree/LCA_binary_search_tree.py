# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        currentNode = root
        while currentNode:
            if p.val < currentNode.val and q.val < currentNode.val:
                currentNode = currentNode.left
            elif p.val > currentNode.val and q.val > currentNode.val:
                currentNode = currentNode.right
            # elif p.val < currentNode.val and q.val > currentNode.val:
            #     return currentNode
            # elif p.val == currentNode.val or q.val == currentNode.val:
            #     return currentNode
            else:
                return currentNode