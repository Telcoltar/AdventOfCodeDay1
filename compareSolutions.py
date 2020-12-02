import timeit
from simpleSolution import simpleSolution
from mediateSolution import mediateSolution
from fasterSolution import fasterSolution

if __name__ == "__main__":
    print(timeit.timeit(simpleSolution, number=10000))
    print(timeit.timeit(mediateSolution, number=10000))
    print(timeit.timeit(fasterSolution, number=10000))