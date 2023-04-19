class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        visited = set()
        visited.add(0)
        self.grayCodeHelper(n, visited, result)
        return result
    
    def grayCodeHelper(self, n, visited, result):
        
        if len(result) == 1 << n:
            return True
        
        
        last_number = result[-1]
        
        for i in range(0,n):
            new_number = last_number ^ (1 << i)
                
            if new_number not in visited:
                visited.add(new_number)
                result.append(new_number)
                if self.grayCodeHelper(n, visited, result):
                    return True
                result.pop(-1)
                visited.remove(new_number)
        return False