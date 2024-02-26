
//Definition for singly - linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
}


/**
 * @param {ListNode} head
 * @return {boolean}
 */

var hasCycle = function (head) {
    const hasSeen = new Set();
    let currentNode = head;
    while (currentNode !== null) {
        if (hasSeen.has(currentNode)) {
            return true
        } else {
            hasSeen.add(currentNode)
        }
        currentNode = currentNode.next
    }
    return false;
};