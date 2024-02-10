// This is the class of the input binary tree.
class BinaryTree {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}


const invertBinaryTree = tree => {
    let queue = [tree];


    while (queue.length) {
        let current = queue.shift();
        
        if (current) {
            swapLeftAndRight(current)
            queue.push(current.left);
            queue.push(current.right);
        }
    }
}

const swapLeftAndRight = tree => { 
    let dummy = tree.left;
    tree.left = tree.right;
    tree.right = dummy;
}


//recursive solution 


const invertBinaryTreeRecursive = tree => {
    if (!tree) {
        return null;
    }

    swapLeftAndRight(tree);
    invertBinaryTreeRecursive(tree.left);
    invertBinaryTreeRecursive(tree.right);
}