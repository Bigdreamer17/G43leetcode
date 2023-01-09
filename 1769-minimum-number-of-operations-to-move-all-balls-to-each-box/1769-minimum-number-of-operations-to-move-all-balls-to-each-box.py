class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        IndexSum = 0
        arr_size = len(boxes)
        for i in range(arr_size):
            for j in range(arr_size):
                if boxes[j] == '1':
                    IndexSum += abs(i - j)
            answer.append(IndexSum)
            IndexSum = 0
        return answer