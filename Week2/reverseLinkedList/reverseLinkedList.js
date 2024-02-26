/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let currNode = head;
    let prevNode = null;

    while (currNode) {
        const tmp = currNode.next;
        currNode.next = prevNode;
        prevNode = currNode;
        currNode = tmp;
    }
    return prevNode;
};


const recursiveReverseList = head => {
    const rec = (prev, cur) => {
        if (!cur) {
            return prev;
        }
        let tail  = rec(cur, cur.next);
        cur.next = prev;
        return tail;
    }
    return rec(null, head)
}