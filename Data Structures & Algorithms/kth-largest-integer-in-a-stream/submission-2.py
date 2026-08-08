import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top_k = k
        self.nums = []
        for num in nums:
            heapq.heappush(self.nums, num)
            if len(self.nums) > k:
                heapq.heappop(self.nums)
            
        
        print("".join(map(str, self.nums)))
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        return heapq.nlargest(self.top_k, self.nums)[-1]
        
