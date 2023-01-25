class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = ceil(sqrt(c))
        left = 0
        while left <= right:
            if right ** 2 + left ** 2 > c:
                right -= 1
            if right ** 2 + left ** 2 < c:
                left += 1
            else:
                return True
        return False

#         for i in range(c):
#             if i ** 2 <= c:
#                 possibles.append(i)
        
#         # if len(possibles) < 2:
#         #     return False
#         ptr1 = 0
#         ptr2 = 0
        
#         while ptr1 < len(possibles) or ptr2 < len(possibles) :
#             if (possibles[ptr1] ** 2) + (possibles[ptr2] ** 2) > c:
#                 ptr2 += 1
#             elif (possibles[ptr1] ** 2) + (possibles[ptr2] ** 2) < c:
#                 ptr1 += 1
#             else:
#                 return True
#         return False
            