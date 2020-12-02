from commonUtils import getInputData


def loopWithFixedNumber(fixed, numbers):
    for n in numbers:
        if fixed + n == 2020:
            return n
    return -1


def outerLoop(numbers):
    for m in numbers:
        res = loopWithFixedNumber(m, numbers)
        if res != -1:
            return m, res


def simpleSolution():
    n, m = outerLoop(getInputData())
    return n*m


if __name__ == "__main__":
    print(simpleSolution())
