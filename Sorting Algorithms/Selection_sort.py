class Soltuion:
    def selection_sort(self,arr):
        for i in range(0,len(arr)-1):
            mini = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[mini]:
                   mini = j
            arr[i],arr[mini] = arr[mini],arr[i]       

           
        return arr


arr = [7,54,3,2,5,6,7,9,88,44]

result = Soltuion()
print(result.selection_sort(arr))
