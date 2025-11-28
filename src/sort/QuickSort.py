class QuickSort:
    @staticmethod
    def quick_sort(a: list[int]) -> list[int]:
        if len(a) <= 1:
            return a

        pivot = a[0]
        left = []
        right = []
        for i in range(len(a)):
            if a[i] < pivot:
                left.append(a[i])
            elif a[i] > pivot:
                right.append(a[i])

        return QuickSort.quick_sort(left) + [pivot] + QuickSort.quick_sort(right)
