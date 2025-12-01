from src.Benchmark import timeit_once
from src.sort.QuickSort import QuickSort


class BucketSort:
    """ 
    The main idea is to somehow split given unsorted list to buckets,
    then apply any sorting algorithm to each bucket.
    """

    @staticmethod
    @timeit_once
    def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
        if buckets is None:
            n = len(a)
        else:
            n = buckets
        buckets_list = [[] for _ in range(n)]

        for num in a:
            if num >= 1.0 or num < 0.0:
                raise ValueError("Bucket sort works only with float numbers in range [0,1)")
            bi = int(n * num)
            buckets_list[bi].append(num)

        for bucket in buckets_list:
            QuickSort.quick_sort(bucket)

        index = 0
        for bucket in buckets_list:
            for num in bucket:
                a[index] = num
                index += 1

        return a
