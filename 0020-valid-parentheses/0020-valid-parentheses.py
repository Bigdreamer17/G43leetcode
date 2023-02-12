class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
		
        s= [x for x in s]
		
        dicta = {
            '(':')',
            '[':']',
            '{':'}'
        }
        
        while s:
            if len(stack)!=0:
			
                if s[0]==dicta.get(stack[-1]):           
                    s.pop(0)
                    stack.pop(-1)
					
                else:
                    stack.append(s.pop(0))
					
            else:
                stack.append(s.pop(0))
        
        return False if stack else True