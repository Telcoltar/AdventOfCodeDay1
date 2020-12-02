from commonUtils import getInputData


def find_number_in_set(numbers, goal):
    for n in numbers:
        if goal - n in numbers:
            return n, goal - n
    return -1, -1


def fasterSolution():
    numbers_set = set(getInputData())
    n, m = find_number_in_set(numbers_set, 2020)
    return n * m


if __name__ == "__main__":
    print(fasterSolution())
