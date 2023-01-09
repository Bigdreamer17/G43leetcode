class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        count = 0
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    count += abs(i - j)
            answer.append(count)
            count = 0
        return answer