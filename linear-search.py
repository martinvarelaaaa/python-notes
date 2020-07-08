import random


def lineal_search(list, objective):
    match = False

    for element in list:
        if element == objective:
            match = True
            break
    return match


if __name__ == '__main__':
    size_of_list = int(input('De que tamano sera la lista?'))
    objective = int(input('Que numero quieres encontrar?'))

    list = [random.randint(0, 100) for i in range(size_of_list)]
    found = lineal_search(list, objective)

    print(list)
    print(
        f'El elemento objetivo {objective} {"esta" if found else "no esta"} en la lista')
