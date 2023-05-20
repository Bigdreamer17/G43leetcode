class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        res=[]
        cstr = str(num)
        for i in cstr:
            if int(i) % 2 == 0:
                even.append(-int(i))
            else:
                odd.append(-int(i))
        heapq.heapify(even)
        heapq.heapify(odd)
        for value in cstr:
            val=int(value)
            if val%2==0:
                res.append(str(-heapq.heappop(even)))
            else:
                res.append(str(-heapq.heappop(odd)))
        return int("".join(res))