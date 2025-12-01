import sys

from tests.Generator import Generator


class Main:
    @staticmethod
    def main() -> None:
        sys.setrecursionlimit(100000)

        Generator.generate_test_cases()

if __name__ == "__main__":
    Main.main()
