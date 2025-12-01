from src.Benchmark import timeit_once


class BubbleSort:
    @staticmethod
    @timeit_once
    def bubble_sort(a: list[int]) -> list[int]:
        n = len(a)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

        return a
