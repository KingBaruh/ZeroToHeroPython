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

lst = [4, 5, 3,2,6,7,0,10]


print(lst[0::2])

d = {
    'baruh': 25,
    'adi' : 100,
    'bibi' : True
}

d['baruh'] = 100
d['anna'] = 'hi'

print(d['baruh'])
print(d['anna'])

d.get('dan',0)

for key in d:
    d[key] = '232'


lst = [4, 5, 3,2,6,7,0,10]
new_lst = {lst[i]: lst[i] + 1 for i in range(len(lst)) if i % 2 == 0}

print(new_lst)


def map_extensions(filename):
    file = open(filename, mode='r')
    lines = file.readlines()
    result = {}
    for line in lines:
        lst = line.split('.')
        file_name = lst[0]

        flag = result.get(file_name, False)
        if not flag:
            result[file_name] = []

        for i in range(1, len(lst)):
            if not lst[i] in result[file_name]:
                result[file_name].append(lst[i])

    for key in result:
        result[key] = sorted(result[key], reverse=True)

    file.close()
    return result



# >>> find_and_count(‘abc’, [‘abc’, ‘ghi’, (‘fol1’, [‘abc1’, ‘abc2’]), (‘abc2’, [‘hello’])])
# {‘files’: 3, ‘folders’: 1}
# >>> find_and_count(‘hello’, [‘data.csv’, (‘courses’, [‘pyprog’, ‘Calculus’])])
# {‘files’: 0, ‘folders’: 0}

def find_and_count(name, files_and_folders):
    result_d = {'files': 0, 'folders': 0}
    helper(name, files_and_folders, result_d)
    return result_d

def helper(name, files_and_folders, result_d):
    for item in files_and_folders:
        if type(item) is str:
            if name in item:
                result_d['files'] += 1
        else:
            folder_name, folder_files = item
            if name in folder_name:
                result_d['folders'] += 1
            helper(name, folder_files, result_d)



