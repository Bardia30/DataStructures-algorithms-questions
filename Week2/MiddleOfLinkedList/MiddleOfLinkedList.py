# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

#O(n) time, O(1) Space
class Solution:
    def middleNode(self, head):
        currentNode = head
        length = 0

        #iterate over the LL to find the length
        while currentNode:
            length += 1
            currentNode = currentNode.next
        

        # intiate the head again and keep count of the position of index starting from 1 instead of 0
        # secondIterNode = head
        # secondIterIdx = 1

        # #second iteration to find the middle node
        # while secondIterNode:
        #     if length % 2 != 0:
        #         if secondIterIdx == math.ceil(length / 2):
        #             return secondIterNode
        #     else:
        #         if secondIterIdx == length / 2:
        #             return secondIterNode.next
        #     secondIterNode = secondIterNode.next
        #     secondIterIdx += 1
        
        thirdIterNode = head
        thirdIterIdx = 0
        #better second iteration
        while thirdIterNode:
            if thirdIterIdx == math.floor(length / 2):
                return thirdIterNode
            thirdIterNode = thirdIterNode.next
            thirdIterIdx += 1
    


#second solutions using two pointers
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast:
            if not fast.next:
                return slow
            fast = fast.next.next
            slow = slow.next
        return slow