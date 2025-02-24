class Rep:
    def __init__(self, name):
        self.name = name
        self.charisma = 3
        self.truthfulness = 4

    def __repr__(self):
        return f"{self.name}: charisma={self.charisma}, truthfulness={self.truthfulness}"

    def score(self, charisma_factor=1, truthfulness_factor=1):
        avg = ((charisma_factor * self.charisma) + (truthfulness_factor * self.truthfulness)) / (
                    charisma_factor + truthfulness_factor)
        return round(avg, 2)

    def __lt__(self, other):
        return self.score() < other.score()


class Party:
    def _init_(self, name, representatives, has_primaries):
        self.name = name
        self.has_primaries = has_primaries
        if has_primaries:
            self.representatives = sorted(representatives).reverse()
        else:
            self.representatives = representatives

    def __add__(self, other):
        new_name = self.name + " & " + other.name
        new_representatives_list = []

        for i in range(min(len(self.representatives), len(other.representatives))):
            new_representatives_list.append(self.representatives[i])
            new_representatives_list.append(other.representatives[i])

        new_representatives_list += self.representatives[len(other.representatives):] + other.representatives[len(self.representatives)]

        return Party(new_name, new_representatives_list, False)

    def __sub__(self, other):
        return Party(self.name, [rep for rep in self.representatives if rep not in other.representatives] ,self.has_primaries)


if __name__ == '__main__':
    rep1 = Rep('John')
    rep2 = Rep('Jack')
    print(Rep)





