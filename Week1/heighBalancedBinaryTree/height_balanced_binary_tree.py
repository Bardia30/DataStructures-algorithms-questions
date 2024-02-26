class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced




def getTreeInfo(node):
    if node == None:
        return TreeInfo(True, -1)
    
    leftSubtreeInfo = getTreeInfo(node.left)
    rightSubtreeInfo = getTreeInfo(node.right)

    isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced and abs(leftSubtreeInfo.height - rightSubtreeInfo.height ) <=1
    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1
    return TreeInfo(isBalanced, height)


#############Neetcode Solution
# class Solution:
    
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
#         def dfs(root):
#             if not root:
#                 return [True, 0]
            
#             left, right = dfs(root.left), dfs(root.right)
#             balance = left[0] and right[0] and abs(left[1] - right[1]) <= 1

#             return [balance, 1 + max(left[1], right[1]) + 1 ]
        

#         return dfs(root)[0]
    


###another solution (neetcode without class Solution)
def heightBalancedBinaryTree(tree):
    # Write your code here.
    return dfs(tree)[0]

def dfs(node):
    if not node:
        return [True, 0]
    
    leftSubtree = dfs(node.left)
    rightSubtree = dfs(node.right)

    isBalanced = leftSubtree[0] and rightSubtree[0] and abs(leftSubtree[1] - rightSubtree[1]) <= 1

    return [isBalanced, max(leftSubtree[1], rightSubtree[1]) + 1]