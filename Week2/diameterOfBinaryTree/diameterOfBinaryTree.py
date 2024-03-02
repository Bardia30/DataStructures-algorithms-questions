class Solution:
    def diameterOfBinaryTree(self, root):
        res = [0]

        def dfs(root):
            # for null tree height is -1
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0],2 + left + right)

            return 1 + max(left, right)
        

        dfs(root)
        return res
    
######################################################
##########################
#AlgoExpert Solution


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)


    return TreeInfo(currentDiameter, currentHeight)


class TreeInfo:
    def __inti__(self, diameter, height):
        self.diameter = diameter
        self.height = height