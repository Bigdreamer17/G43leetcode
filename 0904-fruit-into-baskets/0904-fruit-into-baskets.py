class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0 
        if len(fruits) < 2:
            return 1
        
        MAX = 0 
        basket = defaultdict(int)
         
        
        for right in range(len(fruits)):
          
            basket[fruits[right]] += 1
    
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1
                    
            MAX = max(MAX, right - left + 1)
            
        return MAX