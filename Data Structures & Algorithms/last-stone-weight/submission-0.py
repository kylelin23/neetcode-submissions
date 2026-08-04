import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): 
            stones[i] *= -1
        heapq.heapify(stones)
        while(len(stones) > 1): 
            stone1 = stones[0]
            heapq.heappop(stones)
            stone2 = stones[0]
            if(stone1 == stone2): 
                heapq.heappop(stones)
            else: 
                heapq.heappop(stones)
                heapq.heappush(stones, stone1 - stone2)
        if len(stones) == 0: 
            return 0
        else: 
            return stones[0] * -1