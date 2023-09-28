class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getResult(s):
            st = []
            for c in s:
                if c == '#':
                    if st:
                        st.pop()
                else:
                    st.append(c)
            return "".join(st)
        
        return getResult(s) == getResult(t)
