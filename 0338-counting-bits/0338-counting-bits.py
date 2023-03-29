class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            cur = i
            count = 0
            
            while cur != 0:
                res = cur & 1
                if res == 1:
                    count += 1
                cur = cur >> 1
                
            ans.append(count)
        return ans