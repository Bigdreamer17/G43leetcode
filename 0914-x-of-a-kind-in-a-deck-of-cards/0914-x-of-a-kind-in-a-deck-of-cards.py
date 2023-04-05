class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def GCD(a,b):
            while b:
                a ,b = b, a % b
                
            return a
        
        count = {}
        for i in deck:
            if i not in count:
                count[i] = 0
            count[i] += 1
            
        gcd = count[deck[0]]
        for i in count.values():
            gcd = GCD(gcd, i)

        if gcd == 1:
            return False
        return True 