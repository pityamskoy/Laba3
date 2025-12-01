from src.Benchmark import timeit_once


class HeapSort:
    @staticmethod
    @timeit_once
    def heap_sort(a: list[int]) -> list[int]:
        def heapify(list_to_heapify: list, quantity: int, index: int):
            """
            :param list_to_heapify: list of array to make nodes
            :param quantity: amount of elements
            :param index: index of the largest element
            :return: list with nodes
            """
            largest = index
            # creating correct indexes in the tree
            l = 2 * largest + 1
            r = 2 * largest + 2

            if l < quantity and list_to_heapify[l] > list_to_heapify[largest]:
                largest = l

            if r < quantity and list_to_heapify[r] > list_to_heapify[largest]:
                largest = r

            # otherwise child was chosen correctly
            if largest != index:
                list_to_heapify[index], list_to_heapify[largest] = list_to_heapify[largest], list_to_heapify[index]
                heapify(list_to_heapify, quantity, largest)

        n = len(a)

        # make Max Heap
        # it changes initial list a
        for i in range(n // 2 - 1, -1, -1):
            heapify(list_to_heapify=a, quantity=n, index=i)

        for i in range(n - 1, 0, -1):
            a[i], a[0] = a[0], a[i]  # Swap max to end
            heapify(list_to_heapify=a, quantity=i, index=0)

        return a
