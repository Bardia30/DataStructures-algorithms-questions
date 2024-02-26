# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#recursive solution
def invertBinaryTree(tree):
    # Write your code here.
    
    if not tree:
        return None

    dummyNode = tree.left
    tree.left = tree.right
    tree.right = dummyNode

    invertBinaryTree(tree.right)
    invertBinaryTree(tree.left)


#iterative solution


def invertBinaryTreeIterative(tree):
    queue = [tree]


    while len(queue):
        current= queue.pop(0) 

        if current is None: 
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left