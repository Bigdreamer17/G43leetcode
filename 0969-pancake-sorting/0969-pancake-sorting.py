class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        values = []
        for i in range(length):
            max_value = max(arr[: length - i])
            max_indx = arr.index(max_value) + 1
            arr[:max_indx] = reversed(arr[:max_indx])
            values.append(max_indx)
            
            arr[:length - i] = reversed(arr[:length - i])
            values.append(length - i)
        
        return values 