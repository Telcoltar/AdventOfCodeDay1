from commonUtils import getInputData
from fasterSolution import find_number_in_set


def betterSolutionPart2():
    goal = 2020
    numbers = getInputData()
    for n in numbers:
        m, k = find_number_in_set(numbers, goal - n)
        if m != -1:
            return n*m*k


if __name__ == "__main__":
    print(betterSolutionPart2())
