import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap =[]
        for s in stones:
            heapq.heappush(heap, s)
        
        while len(heap) > 1:
            biggest_stones = heapq.nlargest(2, heap)
            print(biggest_stones)

            if len(biggest_stones) == 2:
                stone_1 = biggest_stones[0]
                stone_2 = biggest_stones[1]

                heap.remove(stone_1)
                heap.remove(stone_2)

                if stone_1 != stone_2:
                    print(stone_1 - stone_2)
                    heapq.heappush(heap, stone_1 - stone_2)
                    print(f"Elements : {heap}")

                heapq.heapify(heap)
            
        return 0 if not heap else heap[0]





            