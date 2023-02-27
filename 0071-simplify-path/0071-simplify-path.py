class Solution:
    def simplifyPath(self, path: str) -> str:
        pah = path.split('/')
        ans = []
        for i in pah:
            if i == "..":
                if ans:
                    ans.pop()
            elif i != "" and i != ".":
                ans.append('/' + i)
        
        return ''.join(ans) if ans else '/'