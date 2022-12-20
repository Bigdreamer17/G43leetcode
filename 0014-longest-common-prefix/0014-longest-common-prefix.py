class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        srt = sorted(strs, key=len)
        short = srt[0]
        for i in range(len(short)):
            for word in strs:
                if short[i] != word[i]:
                    return ''.join(ans)
            ans.append(short[i])
        return ''.join(ans)