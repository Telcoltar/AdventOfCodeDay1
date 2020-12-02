from timeit import timeit
from simpleSolutionPart2 import simpleSolutionPart2
from betterSolutionPart2 import betterSolutionPart2

repeats = 100


if __name__ == "__main__":
    print(timeit(simpleSolutionPart2, number=repeats))
    print(timeit(betterSolutionPart2, number=repeats))