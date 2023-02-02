class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buffer, isBlockOpen = [], "", False
        for line in source:
            index = 0
            while index < len(line):
                if line[index] == '/' and index + 1 < len(line) and line[index+1] == "/" and not isBlockOpen:
                    index = len(line)
                elif line[index] == "/" and index + 1 < len(line) and line[index+1] == "*" and not isBlockOpen:
                    isBlockOpen = True
                    index += 2
                elif line[index] == "*" and index + 1 < len(line) and line[index+1] == "/" and isBlockOpen:
                    isBlockOpen = False
                    index += 2
                elif isBlockOpen:
                    index += 1
                else:
                    buffer += line[index]
                    index  += 1
            if not isBlockOpen and buffer:
                res.append(buffer)
                buffer = ""
        return res
        