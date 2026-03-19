class Bubble:
    def bubble_sort(self, arr: list[int]) -> list[int]:
        n: int = len(arr)
        didSwap = False

        # Outer loop controls number of passes
        # After each pass, the largest element "bubbles up" to its correct position at the end
        for i in range(n, 0, -1):  
            # We iterate from n → 1 (reverse), because after every pass,
            # the last i-th position is already sorted

            # Inner loop compares adjacent elements
            # It runs till i-1 because we compare arr[j] with arr[j+1](i-1 because for last element there will be no one to compare with throwing runtime error)
            for j in range(0, i - 1):  
                # Compare current element with next element
                if arr[j] > arr[j + 1]:
                    # Swap if elements are in wrong order
                    # This pushes the larger element one step toward the end
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    didSwap = True

            if didSwap == False:
                break            # for the case when the array is already sorted and time complexity beomes O(n) not O(n^2)

        # After all passes, array becomes sorted
        return arr


arr: list[int] = [7, 54, 3, 2, 5, 6, 7, 9, 88, 44]

res: Bubble = Bubble()
print(res.bubble_sort(arr))