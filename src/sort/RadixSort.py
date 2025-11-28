class RadixSort:
    @staticmethod
    def radix_sort(a: list[int]) -> list[int]:
        max_num = max(a)
        exp = 1  # Exp is degree of 10 on which we should make division

        while max_num // exp > 0:
            n = len(a)
            output = [0] * n
            count = [0] * 10  # For digits 0–9

            # Count frequency of each digit
            for num in a:
                digit = (num // exp) % 10
                count[digit] += 1

            # Similar to prefix sum in counting sort.
            for i in range(1, 10):
                count[i] += count[i - 1]

            # for i in range(len(reversed(a))):
            for i in range(n - 1, -1, -1):
                digit = (a[i] // exp) % 10
                output[count[digit] - 1] = a[i]
                count[digit] -= 1

            for i in range(n):
                a[i] = output[i]

            exp *= 10

        return a
