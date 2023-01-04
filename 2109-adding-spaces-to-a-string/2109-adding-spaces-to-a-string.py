class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ModifiedString = []
        # Intialzing pointer
        pointer1 = 0
        SpacesSize = len(spaces)
        Ssize = len(s)
        
        while pointer1 < SpacesSize:
            for i in range(Ssize):
                # Check pointer does not passs space size
                # Check if index is equal to spaces value
                if pointer1 < SpacesSize and i == spaces[pointer1]:
                    ModifiedString.append(" ")
                    pointer1 += 1
                # Append if index not in Spaces
                ModifiedString.append(s[i])
                
        # Return Joined Modified string
        return ''.join(ModifiedString)
        
        """
        spec = set(spaces)
        for i in range(len(s)):
            if i in spec:
                ans.append(" ")
        
            ans.append(s[i])
        return ''.join(ans)
        """