class CountingSort:
    @staticmethod
    def counting_sort(a: list[int]) -> list[int]:
        max_val = max(a)
        count = [0] * (max_val + 1)
        output = [0] * len(a)

        """
        frequency of each element
        """
        for num in a:
            count[num] += 1

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
            output[count[num] - 1] = num
            count[num] -= 1

        # for i in range(len(a)):
        #    a[i] = output[i]

        # return a were there initially
        return output
