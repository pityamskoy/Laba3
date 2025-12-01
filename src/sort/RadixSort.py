from src.Benchmark import timeit_once

"""
Counting sort supports only not negative values!
With negative values it will return incorrect results.
"""
class RadixSort:
    @staticmethod
    @timeit_once
    def radix_sort(a: list[int], base: int = 10) -> list[int]:
        max_num = max(a)
        exp = 1  # Exp is degree of 10 on which we should make division

        while max_num // exp > 0:
            n = len(a)
            output = [0] * n
            count = [0] * base  # For digits 0–9

            # Count frequency of each digit
            for num in a:
                digit = (num // exp) % base
                count[digit] += 1

            # Similar to prefix sum in counting sort.
            for i in range(1, base):
                count[i] += count[i - 1]

            negative_bucket = []
            # for i in range(len(reversed(a))):
            for i in range(n - 1, -1, -1):
                digit = (a[i] // exp) % base
                output[count[digit] - 1] = a[i]
                count[digit] -= 1

            if len(negative_bucket) > 0:
                output = negative_bucket + output

            for i in range(n):
                a[i] = output[i]

            exp *= base

        return a
