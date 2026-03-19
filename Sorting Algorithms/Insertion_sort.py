class Insert:
    def insertion_sort(self, arr: list[int]) -> list[int]:
        n: int = len(arr)

        # Outer loop: iterate through array
        # We start from 1 because index 0 is already considered sorted
        for i in range(1, n):

            # j represents current index to be inserted correctly
            j: int = i

            # Move current element left until it's in correct position
            # Compare with previous elements and swap if needed
            while j > 0 and arr[j - 1] > arr[j]:
                # Swap adjacent elements
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

                # Move one step left
                j -= 1

        return arr


arr: list[int] = [7, 54, 3, 2, 5, 6, 7, 9, 88, 44]

res: Insert = Insert()
print(res.insertion_sort(arr))

"""“Insertion sort is adaptive because the number of operations depends on how sorted the array already is—the inner loop runs fewer times when the array is nearly sorted. Selection sort is not adaptive because it always performs the same number of comparisons regardless of input order.”"""


"""🔥 Better Version (More Efficient)

Previous version swaps repeatedly. A better version shifts instead of swapping:"""

class Insert:
    def insertion_sort(self, arr: list[int]) -> list[int]:
        n: int = len(arr)

        for i in range(1, n):
            key: int = arr[i]
            j: int = i - 1

            # Shift elements instead of swapping
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            # Place key at correct position
            arr[j + 1] = key

        return arr
    

arr: list[int] = [7, 54, 3, 2, 5, 6, 7, 9, 88, 44]

res: Insert = Insert()
print(res.insertion_sort(arr))    