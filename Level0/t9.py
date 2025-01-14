# %% Bubble Sort
from random import shuffle


def bubble_sort(lst):
    n = len(lst)
    for i in range(n, 0, -1):
        for j in range(i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(lst)
print(f"Non sorted lst is {lst}.")
bubble_sort(lst)
print(f"Bubble sorted lst is {lst}.")

# %% Merge Sort
from random import shuffle


def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    left = merge_sort(lst[:n // 2])
    right = merge_sort(lst[n // 2:])
    return merge(left, right)


def merge(lst1, lst2):
    merged_list = []
    lst1_idx, lst2_idx = 0, 0
    while lst1_idx < len(lst1) and lst2_idx < len(lst2):
        if lst1[lst1_idx] < lst2[lst2_idx]:
            merged_list.append(lst1[lst1_idx])
            lst1_idx += 1
        else:
            merged_list.append(lst2[lst2_idx])
            lst2_idx += 1
    merged_list += lst1[lst1_idx:] + lst2[lst2_idx:]
    return merged_list


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(lst)
print(f"Non sorted lst is {lst}.")
print(f"Merge sorted lst is {merge_sort(lst)}.")

# %% Bucket Sort
from random import shuffle


def bucket_sort(lst, max):
    buckets = [0] * (max + 1)
    for item in lst:
        buckets[item] += 1

    lst[:] = []
    for num, count in enumerate(buckets):
        # lst.extend(count * [num])
        lst += count * [num]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(lst)
print(f"Non sorted lst is {lst}.")
bucket_sort(lst, max(lst))
print(f"Bucket sorted lst is {lst}.")

# %% q1
from random import shuffle


def sort_strings(lst):
    n = len(lst)
    for i in range(n, 0, -1):
        for j in range(i - 1):
            if len(lst[j]) > len(lst[j + 1]):
                lst[j + 1], lst[j] = lst[j], lst[j + 1]


test_string = "This sentence will be separated into its words, and a list of strings is going to get sorted"
print(test_string + ".")
string_list = test_string.split()
shuffle(string_list)
print(f"Non sorted string_lst is {string_list}.")
sort_strings(string_list)
print(f"Sorted string_list is {string_list}.")

# %% q2

from random import randrange


def disjoint_lists(lst1, lst2):
    idx_1, idx_2 = 0, 0
    while idx_1 < len(lst1) and idx_2 < len(lst2):
        if lst1[idx_1] < lst2[idx_2]:
            idx_1 += 1
        elif lst1[idx_1] > lst2[idx_2]:
            idx_2 += 1
        else:
            return False
    return True


lst1 = sorted([randrange(30) for i in range(5)])
lst2 = sorted([randrange(30) for i in range(5)])
print(f"lst1 is {lst1} and lst2 is {lst2}.")
print("Are the two lists disjointed?", disjoint_lists(lst1, lst2))


# %% q3

def findMinArrowShots(points):
    points.sort(key=lambda x: x[0])

    count = 1
    start = points[0]
    top = start[1]

    for idx in range(1, len(points)):
        if points[idx][0] > top:
            count += 1
            start = points[idx]
            top = start[1]
        top = min(top, points[idx][1])
    return count


points1 = [[1, 6], [2, 8], [7, 12], [10, 16]]
points2 = [[1, 10], [6, 7], [8, 12]]
points3 = [[1, 2], [3, 4], [5, 6]]

print(f"points1 is {points1}.\nThe minimal number of points to achieve full coverage is {findMinArrowShots(points1)}.")
print(f"points2 is {points2}.\nThe minimal number of points to achieve full coverage is {findMinArrowShots(points2)}.")
print(f"points3 is {points3}.\nThe minimal number of points to achieve full coverage is {findMinArrowShots(points3)}.")


# %% q4

def non_overlapping_intervals(intervals):
    prev = 0
    cnt = 1
    intervals.sort(key=lambda x: x[1])
    n = len(intervals)
    for idx in range(1, n):
        if intervals[idx][0] >= intervals[prev][1]:
            prev = idx
            cnt += 1
    return n - cnt


points1 = [[1, 6], [2, 8], [7, 12], [10, 16]]
points2 = [[1, 10], [6, 7], [8, 12]]
points3 = [[1, 2], [3, 4], [5, 6]]

print(f"points1 is {points1}.\nThe minimal number of intervals to remove is {non_overlapping_intervals(points1)}.")
print(f"points2 is {points2}.\nThe minimal number of intervals to remove is {non_overlapping_intervals(points2)}.")
print(f"points3 is {points3}.\nThe minimal number of intervals to remove is {non_overlapping_intervals(points3)}.")

# %% Dictionary

students = [
    {"name": "Alon", "eng-grade": 90, "math-grade": 100},
    {"name": "Nir", "eng-grade": 80, "math-grade": 25},
    {"name": "Dana", "eng-grade": 85, "math-grade": 89}
]
print("Let's print Nir's entry in the dictionary:", students[1])

# %% Nested Dictionary

students = {
    "Alon": {"eng-grade": 90, "math-grade": 100},
    "Nir": {"eng-grade": 80, "math-grade": 25},
    "Dana": {"eng-grade": 85, "math-grade": 89}
}
print("Let's print Nir's entry in the dictionary:", students["Nir"])

# %% Dictionary extras

thisdict = {}
thisdict = {"brand": "Ford"}

print(thisdict['brand'])

try:
    print(thisdict['price'])
except:
    print("price is not a key that exists in thisdict.")

thisdict['model'] = "Mustang"
print(thisdict)

# %% Dictionary iteration

students = {
    "Alon": {"eng-grade": 90, "math-grade": 100},
    "Nir": {"eng-grade": 80, "math-grade": 25},
    "Dana": {"eng-grade": 85, "math-grade": 89}
}

print("Let's print the names of students in the dictionary:")
for name in students.keys():
    print(name)

print("\nLet's print the english grades of students in the dictionary:")
for data in students.values():
    print(data['eng-grade'])

print("\nLet's use enumerate to print this stuff in a more legible manner:")
for name, data in students.items():
    print(f"{name} got {data['eng-grade']} in English.")

# %% Dictionary mutability

students = {
    "Alon": {"eng-grade": 90, "math-grade": 100},
    "Nir": {"eng-grade": 80, "math-grade": 25},
    "Dana": {"eng-grade": 85, "math-grade": 89}
}

try:
    students += {"Ron": []}
except:
    print("Operator += doesn't work with dictionaries.")

print("the object id of students is", id(students))
students.update({"Ron": []})
print("After the .update command,\nthe object id of students is", id(students))
print("Here's the updated version of students:", students)


# %% q5

def popular_words(text):
    words = text.split()  # same as ' '
    counts = {}

    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    return list(counts.keys())[:10]


text = """
But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure? On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains. But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure? On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains.But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure? On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection:"""

print("The very, VERY long text we'll use is this:\n", text)
print("\nThe 10 most popular words in the above text were:", popular_words(text))


# %% q6

def combine(lst1, lst2):
    fruits = {}
    for fruit, price in zip(lst1, lst2):
        fruits[fruit] = price
    return fruits


def combine_short(lst1, lst2):
    return dict(zip(lst1, lst2))


lst1 = ["apple", "banana", "turkey"]
lst2 = [1, 2, 4]

fruits1 = combine(lst1, lst2)
fruits2 = combine_short(lst1, lst2)

print(fruits1)
print(fruits2)

# %% - Dataclass introduction

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    eng_grade: int
    math_grade: int = 80


student1 = Student("Alon", 95, 100)
student2 = Student("Nir", 100)

print(student2)
print(student1.math_grade)

# %% Dataclass is a bit too(?) flexible

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    eng_grade: int
    math_grade: int = 80


student1 = Student(1.1, 95, 100)
print(student1.name)

student2 = Student("Nir", 100)
student2.evil = True
print(student2)
# %% q7

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    eng_grade: int
    math_grade: int = 80


def above_avg_dict(students):
    for stud in students:
        avg = (stud['eng-grade'] + stud['math-grade']) / 2
        if avg > 85:
            print(stud['name'])


def above_avg_dataclass(students):
    for stud in students:
        avg = (stud.eng_grade + stud.math_grade) / 2
        if avg > 85:
            print(stud.name)


students_dict = [
    {"name": "Alon", "eng-grade": 90, "math-grade": 100},
    {"name": "Nir", "eng-grade": 80, "math-grade": 25},
    {"name": "Dana", "eng-grade": 85, "math-grade": 89}
]

students_dataclass = [
    Student("Sharon", 95, 100),
    Student("Yaron", 100),
    Student("Dov", 10, 20)
]

above_avg_dict(students_dict)
above_avg_dataclass(students_dataclass)

# %% q8

from dataclasses import dataclass


@dataclass
class Client:
    products: list


lst = ["Milk"]

c1 = Client(lst)
c1.products.append("Coffee")
print(lst)

print("Yes, that means that...")
print("lst id is", id(lst))
print("And also, c1.products id is", id(c1.products))


