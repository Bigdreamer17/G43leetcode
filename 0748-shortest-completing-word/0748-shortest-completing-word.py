class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l=licensePlate.lower()
        o=[]
        for i in words:
            m=True
            for j in set(l):
                if j!=' 'and not j.isnumeric():
                    if j in i and i.count(j)>=l.count(j):
                        
                        continue
                    else:
                        m=False
                        break
            if m:
                o.append(i)

        if o :
            o=sorted(o,key=len)
            
            return o[0]
        return