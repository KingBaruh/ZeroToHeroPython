class Man():
    def __init__(self, name, dick_size, age):
        self.name = name
        self.age = age
        self.dick_size = dick_size

    def go_to_gym(self):
        if self.age > 30:
            print('dont gym bro')
        else:
            print('only gym bro')

    def update_age(self, new_age):
        self.age = new_age


man = Man('<didi>', 5, 33)
baruh = Man('baruh', 5000000, 20)

#man.go_to_gym()

print(man.age)
man.update_age(100)
print(man.age)

x = 3
