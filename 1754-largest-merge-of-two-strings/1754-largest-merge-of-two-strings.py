class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        size1 = len(word1)
        size2 = len(word2)
        merge = []
        ptr1 = ptr2 = 0
        
        while ptr1 < size1 and ptr2 < size2:
            if word1[ptr1] == word2[ptr2]:
                if word1[ptr1: ] >= word2[ptr2: ]:
                    merge.append(word1[ptr1])
                    ptr1 += 1
                else:
                    merge.append(word2[ptr2])
                    ptr2 += 1
                
            elif word1[ptr1] > word2[ptr2]:
                merge.append(word1[ptr1])
                ptr1 += 1
            else:
                merge.append(word2[ptr2])
                ptr2 += 1
        
        merge.extend(word1[ptr1: ])
        merge.extend(word2[ptr2: ])
        return ''.join(merge)