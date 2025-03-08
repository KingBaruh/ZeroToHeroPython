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


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    sorted_arr = []
    i = 0
    j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1

    if i < len(left_arr):
        sorted_arr.extend(left_arr[i:])

    if j < len(right_arr):
        sorted_arr.extend(right_arr[j:])

    return sorted_arr

def foods_calories(foods):
    return {}

def daily_calories(calories_file, days_lst):
    dic = foods_calories(calories_file)
    result_lst = []

    for day in days_lst:
        day_calories = 0
        file = open(day, mode='r')
        lines = file.readlines()
        for line in lines:
            pair = line.strip().split('*') #['4', 'Apple']
            value_of_product = dic.get(pair[1], 100)
            day_calories += value_of_product * int(pair[0])

        result_lst.append(day_calories)
        file.close()

    return result_lst


def subset_sums(nums):
    if len(nums) == 0:
        return [0]

    else:
        result_lst = []
        #[1,2,3,4]
        # nums[:-1] = [1,2,3]
        lst2 = subset_sums(nums[:-1])

        result_lst = result_lst + lst2

        for item in lst2:
            item += nums[-1]
            result_lst.append(item)

        return result_lst

class Client:
    def __init__(self, name, salary, balance):
        if type(name) is not str:
            print('Name Error')
            self.name = 'error'
        else:
            self.name = name
        self.salary = salary
        self.balance = balance

    def salary_raise(self, amount):
        self.salary += amount
        self.balance += 0.3 * amount

    def __repr__(self):
        return f'Name: {self.name}, Salary: {self.salary}, Balance:{self.balance}'

class Bank:
    def __init__(self, name):
        self.name = name
        self.client_lst = []
        self.balance = 0

    def add_client(self, client):
        self.client_lst.append(client)
        self.balance += client.balance

    def __repr__(self):
        output = f'Name: {self.name}, Balance: {self.balance}\nBank Clients:\n'
        for client in self.client_lst:
            output += f'{client}\n'
            output += f'Client balance percent: {int(100 * client.balance/self.balance)}\n'

        return output

def mul_crit(client, alpha, beta):
    return alpha + beta * 2000 / client.salary

def max_salary(bank):
    r_max = float('-inf')
    for client in bank.client_lst:
        r_max = max(client.salary,r_max)
    return r_max

def approved_clients(bank):
    lst = sorted(bank.client_lst, key=lambda client: mul_crit(client, max_salary(bank) - client.salary, bank.balance))
    return lst[:len(lst)//2]

