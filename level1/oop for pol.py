def func(data: dict):
    my_dict = data["data flows"]["Rendering"]["participating actors"]["Update tree"]

    avg = 0
    for key in my_dict.keys():
        avg += my_dict[key]["average time"]

    avg = avg / len(my_dict.keys())
    print(f"{avg:.5f}")

    min_best_time = float("inf")
    min_key_best_time = None
    for key in my_dict.keys():
        if my_dict[key]["best time"] < min_best_time:
            min_best_time = my_dict[key]["best time"]
            min_key_best_time = key

    print(min_key_best_time)

    max_worst_time = float("-inf")
    max_key_worst_time = None
    for key in my_dict.keys():
        if my_dict[key]["worst time"] > max_worst_time:
            max_worst_time = my_dict[key]["worst time"]
            max_key_worst_time = key

    print(max_key_worst_time)

    for key in my_dict.keys():
        print(my_dict[key]["count"])

    # part 2

    print(f'average time={avg:.5f}')

    avg = 0
    for key in my_dict.keys():
        avg += my_dict[key]["best time"]

    avg = avg / len(my_dict.keys())
    print(f'best time={avg:.5f}')

    avg = 0
    for key in my_dict.keys():
        avg += my_dict[key]["count"]

    avg = avg / len(my_dict.keys())
    print(f'count={avg:.5f}')

    avg = 0
    for key in my_dict.keys():
        avg += my_dict[key]["success rate"]

    avg = avg / len(my_dict.keys())
    print(f'success rate={avg:.5f}')

    avg = 0
    for key in my_dict.keys():
        avg += my_dict[key]["worst time"]

    avg = avg / len(my_dict.keys())
    print(f'worst time={avg:.5f}')


class Animal:
    def __init__(self, color, num_of_legs, specie):
        self.color = color
        self.num_of_legs = num_of_legs
        self.specie = specie

    def __str__(self):
        return f"{self.color} {self.specie}, {self.num_of_legs} legs"


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4, "Wolf")


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4, "Sheep")


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0, "Snake")


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2, "Parrot")


class Cage:
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.num_animals = 0
        self.my_cage = []

    def add_animals(self, *args):
        for animal in args:
            if len(self.my_cage) < 5:
                self.my_cage.append(animal)
                self.num_animals += 1

    def __str__(self):

        my_str = "("
        for animal in self.my_cage:
            my_str += str(animal)
            my_str += '. '

        my_str += ')'

        return f'Cage Id: {self.cage_id}, Max size: 5, currently occupied: {self.num_animals} animals; ' + my_str

    def animals_by_color(self, color):
        res = []
        for animal in self.my_cage:
            if animal.color == color:
                res.append(str(animal))
        return res


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        for cage in args:
            self.cages.append(cage)

    def animals_by_color(self, color):
        res = []
        for cage in self.cages:
            res.append(cage.animals_by_color(color))

        return res

    def number_of_legs(self):
        res = 0
        for cage in self.cages:
            for animal in cage.my_cage:
                res += animal.num_of_legs

        return res


if __name__ == '__main__':
    wolf = Wolf('black')
    sheep1 = Sheep('white')
    sheep2 = Sheep('white')
    snake = Snake('brown')
    parrot = Parrot('black')

    c1 = Cage(1)
    c1.add_animals(wolf, sheep1, sheep2)

    print(c1)

    c2 = Cage(2)
    c2.add_animals(snake, parrot)

    z = Zoo()
    z.add_cages(c1, c2)

    print(z.number_of_legs())

    print(z.animals_by_color('black'))



