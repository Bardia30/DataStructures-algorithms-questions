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

// first solution
var middleNode = function(head) {
    let length = 0;
    let currentNode = head;

    while (currentNode) {
        length++;
        currentNode = currentNode.next;
    }

    let secondIterNode = head;
    let secondIterIdx = 0;

    while (secondIterNode) {
        if (secondIterIdx === Math.floor(length / 2)) {
            return secondIterNode;
        }
        secondIterIdx++;
        secondIterNode = secondIterNode.next;
    }
};



//second solution 
var middleNode = function(head) {
    let fast = head;
    let slow = head;


    while (fast) {
        if (!fast.next) {
            return slow
        }
        fast = fast.next.next;
        slow = slow.next;
    }
    return slow;
};
