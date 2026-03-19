#Basic way of doing selection sort

from ast import List


class Solution:
    def selection_sort(self,arr):
        for i in range(0,len(arr)-1):
            mini = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[mini]:
                   mini = j
            arr[i],arr[mini] = arr[mini],arr[i]       

           
        return arr


arr:list[int] = [7,54,3,2,5,6,7,9,88,44]

result = Solution()
print(result.selection_sort(arr))


#Professional way
#note class,function and variable name are to be same not writing same here because of mismatch
class Sol:
    def selec_sort(self,arr:list[int])->list[int]:
        n : int = len(arr)

        for i in range(0,n-1):# note here we are travesing till n-2 as last index is n-1 and range func predefined to take for n-1. so it means (n-1)-1
            mi:int = i
            for j in range(i+1,n):
                if arr[j]<arr[mi]:
                    mi = j
            arr[i],arr[mi] = arr[mi],arr[i]

        return arr 

res: Sol = Sol()
print(res.selec_sort(arr))               

