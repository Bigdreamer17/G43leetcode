class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        hashh = {}
        monostack = []
        count = 0
        for i, num in enumerate(temp):
            while monostack and monostack[-1][-1] < num:
                indx, val = monostack.pop()
                hashh[(indx, val)] = i - indx
            monostack.append([i, num])
        for i, val in enumerate(temp):
            if (i,val) in hashh:
                temp[i] = hashh[(i, val)]
            else:
                temp[i] = 0
        return temp
            