class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        curr = i
        left = 2 * curr + 1
        right = 2 * curr + 2
        
        if left < n and arr[left] > arr[curr]:
            curr = left
        if right < n and arr[right] > arr[curr]:
            curr = right
        if curr != i:
            arr[i], arr[curr] = arr[curr], arr[i]
            self.heapify(arr,n,curr)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n//2, -1, -1):
            self.heapify(arr,n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        n = len(arr)
        self.buildHeap(arr,n)
        
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr,i,0)
