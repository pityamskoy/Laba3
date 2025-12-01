from src.Benchmark import timeit_once

class QuickSort:
    @staticmethod
    @timeit_once
    def quick_sort_timed(a: list[int]) -> list[int]:
        return QuickSort.quick_sort(a)

    @staticmethod
    def quick_sort(a: list[int]) -> list[int]:
        if len(a) <= 1:
            return a

        pivot = a[0]
        left = []
        right = []
        for i in range(len(a)):
            if a[i] <= pivot and i != 0:
                left.append(a[i])
            elif a[i] > pivot:
                right.append(a[i])

        return QuickSort.quick_sort(left) + [pivot] + QuickSort.quick_sort(right)
