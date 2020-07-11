import random

# Clases base


class Borracho:
    def __init__(self, name):
        self.name = name


class BorrachoStandard(Borracho):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Coordinate(self.x + delta_x, self.y + delta_y)

    def distance(self, coord):
        delta_x = self.x - coord.x
        delta_y = self.y - coord.y

        return (delta_x**2 + delta_y**2)**0.5


class Board:
    def __init__(self):
        self.coordinates_borrachos = {}

    def add(self, borracho, coord):
        self.coordinates_borrachos[borracho] = coord

    def move(self, borracho):
        delta_x, delta_y = borracho.walk()
        current_coord = self.coordinates_borrachos[borracho]
        new_coord = current_coord.move(delta_x, delta_y)

        self.coordinates_borrachos[borracho] = new_coord

    def get(self, borracho):
        return self.coordinates_borrachos[borracho]

# Camino aleatorio


def walk(board, borracho, steps):
    origin = board.get(borracho)

    for _ in range(steps):
        board.move(borracho)

    return origin.distance(board.get(borracho))


def simulate_walk(steps, number_of_attempts, type_of_borracho):
    borracho = type_of_borracho(name='Lalo')
    origin = Coordinate(0, 0)
    distances = []

    for _ in range(number_of_attempts):
        board = Board()
        board.add(borracho, origin)
        simulate = walk(board, borracho, steps)
        distances.append(round(simulate, 1))

    return distances


def main(distances_of_walk, number_of_attempts, type_of_borracho):

    for steps in distances_of_walk:
        distances = simulate_walk(steps, number_of_attempts, type_of_borracho)

        mean_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        print(f'{type_of_borracho.__name__} walk {steps}')
        print(f'Mean= {mean_distance}')
        print(f'Max= {max_distance}')
        print(f'Min= {min_distance}')


if __name__ == '__main__':
    distances_of_walk = [10, 100, 1000, 10000]
    number_of_attempts = 100

    main(distances_of_walk, number_of_attempts, BorrachoStandard)
