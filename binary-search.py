import random


def binary_search(list, start, end, objective):
    if start > end:
        return False

    middle = (start + end) // 2

    if list[middle] == objective:
        return True
    elif list[middle] < objective:
        return binary_search(list, middle + 1, end, objective)
    elif list[middle] > objective:
        return binary_search(list, start, middle - 1, objective)


if __name__ == '__main__':
    size_of_list = int(input('De que tamano sera la lista?'))
    objective = int(input('Que numero quieres encontrar?'))

    list = sorted([random.randint(0, 100) for i in range(size_of_list)])
    found = binary_search(list, 0, len(list), objective)

    print(list)
    print(
        f'El elemento objetivo {objective} {"esta" if found else "no esta"} en la lista')
