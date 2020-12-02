from commonUtils import getInputData


def find_numbers_from_sorted_array(numbers):
    goal = 2020
    lower_index = 0
    higher_index = -1
    n = numbers[lower_index]
    m = numbers[higher_index]
    while n + m != goal:
        if n + m > goal:
            higher_index -= 1
        else:
            lower_index += 1
        n = numbers[lower_index]
        m = numbers[higher_index]
    return n, m


def mediateSolution():
    sorted_numbers = getInputData()
    sorted_numbers.sort()
    n, m = find_numbers_from_sorted_array(sorted_numbers)
    return n*m


if __name__ == "__main__":
    print(mediateSolution())
