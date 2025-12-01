from src.Benchmark import timeit_once


class Fibo:
    @staticmethod
    @timeit_once
    def fibo(number:int) -> int:
        a, b = 0, 1
        if number <= 1:
            return number
        else:
            for _ in range(2, number + 1):
                a, b = b, a + b
            return b

    @staticmethod
    def fibo_recursive(number:int) -> int:
        if number <= 1:
            return number
        else:
            return Fibo.fibo_recursive(number - 1) + Fibo.fibo_recursive(number - 2)

    @staticmethod
    @timeit_once
    def fibo_recursive_timed(number:int) -> int:
        return Fibo.fibo_recursive(number)