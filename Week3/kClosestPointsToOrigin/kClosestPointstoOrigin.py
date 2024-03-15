from math import sqrt
#this sol takes the duplicate notes out. 
class Solution:
    def kClosest(self, points, k):
        hash_table = {}

        for point in points:
            euc_dist = sqrt((point[0])**2 + (point[1])**2)
            hash_table[(point[0], point[1])] = euc_dist
        hash_table =  dict(sorted(hash_table.items(), key=lambda item: item[1]))
        answer = []
        
        for key in hash_table.keys():
            answer.append([key[0], key[1]])
        
        return answer[:k]
    
class Solution:
    def kClosest(self, points, k):
        answer = []

        for point in points:
            euc_dist = sqrt((point[0])**2 + (point[1])**2)
            answer.append((point, euc_dist))

        answer.sort(key=lambda x: x[1])
        answer = [list(point) for point, dist in answer[:k]]

        return answer

#neetcode solution
import heapq    
class Solution:
    def kClosest(self, points, k):
        minHeap = []

        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res
sol = Solution()

print(sol.kClosest([[2,2],[2,2],[3,3],[2,-2],[1,1]], 4))