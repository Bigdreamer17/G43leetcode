class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create two pointers 
        left = 0
        right = len(s) - 1

        while left < right:
            # check if its alphanumeric and move pointers
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                # check if they are equal
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True