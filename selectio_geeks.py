class Solution: 
    def select(self, arr, i):
        # code here 
        self.arr = arr
        self.i = self.min_ind
    
    def selectionSort(self, arr,n):
        #code here
        for s in range(len(arr)):
            min_ind = s
            
            for i in range(s + 1,len(arr)):
                
                if arr[i] < arr[min_ind]:
                    min_ind = i
            arr[s], arr[min_ind] = arr[min_ind], arr[s]
        return arr