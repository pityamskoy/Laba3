from math import factorial

from src.Benchmark import timeit_once


class Factorial:
    @staticmethod
    @timeit_once
    def factorial(number: int) -> int:
        if number < 0:
            raise ValueError("factorial is not determined for negative numbers")
        else:
            result = 1
            for i in range(1, number + 1):
                result *= i
            return result

    @staticmethod
    def factorial_recursive(number: int) -> int:
        if number < 0:
            raise ValueError("factorial is not determined for negative numbers")
        elif number <= 1:
            return 1
        else:
            return number * Factorial.factorial_recursive(number - 1)

    @staticmethod
    @timeit_once
    def factorial_recursive_timed(number:int) -> int:
        return Factorial.factorial_recursive(number)