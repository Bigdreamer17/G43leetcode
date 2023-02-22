class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
        
            window = max(window, right - left + 1)
        return window
                