import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for p in points: 
            distance = (((p[0] * p[0]) + (p[1] * p[1]))** 0.5)
            temp = []
            temp.append(distance)
            temp.append(p)
            heapq.heappush(heap, tuple(temp))
        heapq.heapify(heap)

        for i in range(k): 
            result.append(heap[0][1])
            heapq.heappop(heap)
        return result