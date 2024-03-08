class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        
        def dfs(node):
            right = node.right
            left = node.left
            if right and left:
                depth = max(dfs(left), dfs(right)) + 1
            elif right and not left:
                depth = dfs(right) + 1
            elif left and not right:
                depth = dfs(left) + 1
            else:
                return 1
            return depth
        

        return dfs(root)
    
#O(n) time

#neetcode solution (dfs)
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
#BFS
from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        level = 1
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level
    
#iterative DFS
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        stack = [[root, 1]]
        result = 0
        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result        