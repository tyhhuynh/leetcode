class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
    
        for p in points:
            x, y = p[0], p[1]
            dist = x*x + y*y 
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, p)) # push tuple of distance and coordinates into max_heap) 
                # NOTE: Python heapq only has min-heap feat. to simulate max-heap, negate all elements
            else:
                 # if current distance is less than current largest eleemnt, replace via .heappop() & .heappush()
                if dist < -max_heap[0][0]: # negated first element of max_heap to simulate largest value
                    heapq.heappop(max_heap) 
                    heapq.heappush(max_heap, (-dist, p))
                    
        return [point for (_, point) in max_heap]
        # _ ignores distance and only returns point (x,y)-coordinates in max_heap
        # max_heap contains k tuples in the format (distance, [x,y])