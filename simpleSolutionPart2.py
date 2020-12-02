from commonUtils import getInputData
from simpleSolution import loopWithFixedNumber


def outer_loops(numbers):
    for n in numbers:
        for m in numbers:
            res = loopWithFixedNumber(n + m, numbers)
            if res != -1:
                return n, m, res


def simpleSolutionPart2():
    n, m, k = outer_loops(getInputData())
    return n * m * k


if __name__ == "__main__":
    print(simpleSolutionPart2())
