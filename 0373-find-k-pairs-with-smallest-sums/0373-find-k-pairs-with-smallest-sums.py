class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        resV = []  
        pq = []  

       
        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0]) 
        
        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[1]  

            resV.append([s - nums2[pos], nums2[pos]])

            
            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

            k -= 1  

        return resV