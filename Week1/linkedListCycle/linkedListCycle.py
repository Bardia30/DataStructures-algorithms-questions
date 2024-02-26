from types import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hasSeen = {}
        currentNode = head
        while currentNode:
            if currentNode in hasSeen:
                return True
            else:
                hasSeen[currentNode] = True
            currentNode = currentNode.next
        return False


#the turtle and hair solution: O(1) space solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False