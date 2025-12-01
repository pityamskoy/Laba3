import random

from src.math.Factorial import Factorial
from src.math.Fibo import Fibo
from src.sort.BubbleSort import BubbleSort
from src.sort.BucketSort import BucketSort
from src.sort.CountingSort import CountingSort
from src.sort.HeapSort import HeapSort
from src.sort.QuickSort import QuickSort
from src.sort.RadixSort import RadixSort


class Generator:
    @staticmethod
    def generate_test_cases() -> None:
        const_for_testing_math_block: int = 8
        print(Factorial.factorial(const_for_testing_math_block))
        print(Factorial.factorial_recursive_timed(const_for_testing_math_block))
        print(Fibo.fibo(const_for_testing_math_block))
        print(Fibo.fibo_recursive_timed(const_for_testing_math_block))

        random_array_int = [random.randint(-1000, 1000) for _ in range(4000)]
        random_array_int_for_radix = [random.randint(0, 2000) for _ in range(4000)]
        random_array_float = [random.uniform(0.0, 1) for _ in range(4000)]

        print(BubbleSort.bubble_sort(random_array_int))
        print(CountingSort.counting_sort(random_array_int))
        print(HeapSort.heap_sort(random_array_int))
        print(QuickSort.quick_sort_timed(random_array_int))
        print(RadixSort.radix_sort(random_array_int_for_radix))
        print(BucketSort.bucket_sort(random_array_float))
