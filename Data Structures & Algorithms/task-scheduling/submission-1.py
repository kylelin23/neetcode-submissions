import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks: 
            if t in counts:
                counts[t] -= 1
            else: 
                counts[t] = -1
        
        heap = []
        for t in counts: 
            heap.append(counts[t])
        heapq.heapify(heap)
        
        cooldown = deque()
        time = 0
        while heap or cooldown: 
            time += 1
            if heap: 
                most_freq = heapq.heappop(heap);
                most_freq += 1
                if most_freq < 0: 
                    temp = []
                    temp.append(most_freq)
                    temp.append(time + n)
                    cooldown.append(temp)
            
            if cooldown and cooldown[0][1] <= time: 
                count, _ = cooldown.popleft()
                heapq.heappush(heap,count)

        return time
            
