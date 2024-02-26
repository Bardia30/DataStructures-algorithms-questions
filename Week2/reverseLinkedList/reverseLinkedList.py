# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prevNode = None
        currNode = head


        while currNode:
            nxt = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nxt

        return prevNode

#recursive    
class Solution:
    def reverseList(self, head):
        if not head: 
            return None
    
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead


#another recursive    
class Solution:
    def reverseList(self, head):
        def rec(prev, cur):
            if not cur:
                return prev
            tail = rec(cur, cur.next)
            cur.next = prev
            return tail
        
        return rec(None, head)