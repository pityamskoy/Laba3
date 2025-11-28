from src.sort.QuickSort import QuickSort


class BucketSort:
    """
    The main idea is to somehow split given unsorted list to buckets,
    then apply any sorting algorithm to each bucket.
    """

    @staticmethod
    def bucket_sort(a: list[float]) -> list[float]:
        n = len(a)
        buckets = [[] for _ in range(n)]

        for num in a:
            bi = int(n * num)
            buckets[bi].append(num)

        for bucket in buckets:
            QuickSort.quick_sort(bucket)

        index = 0
        for bucket in buckets:
            for num in bucket:
                a[index] = num
                index += 1

        return a
