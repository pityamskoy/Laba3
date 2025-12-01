from src.Benchmark import timeit_once


class CountingSort:
    @staticmethod
    @timeit_once
    def counting_sort(a: list[int]) -> list[int]:
        offset = -min(a)
        max_val = max(a) + offset
        count = [0] * (max_val + 1)
        output = [0] * len(a)

        """
        frequency of each element
        """
        for num in a:
            count[num + offset] += 1

        """
        Something happens there what I don't understand.
        Wiki says it is prefix sum.
        My explanation: each element move an index of the next one by a quantity of itself
        """
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        """
        count[num] is the index of an element + 1 in output list
        according to previous steps.
        """
        for num in reversed(a):
            offset_index = num + offset
            output[count[offset_index] - 1] = num
            count[offset_index] -= 1

        return output
