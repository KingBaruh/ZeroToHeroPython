
lst = [[]] * 3
lst[0].append(42)
lst[1] += [17]
print(lst[0][0] + lst[2][0])


x = [1, 2, 3]
y = []
for _ in range(2):
    x.append(4)
    y.append(x)
print(y)

s = "python"
t = s
s = s[:3] + "x" + s[3:]
print(t[4], s[5])

from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: 'Node' = None

def func(x, start=Node(0)):
    start.value += x
    start.next = Node(x)
    return start
a = func(3)
b = func(4)
print(a.value, b.next.value)



def collect(x, lst=[]):
    lst.append(x)
    if x > 0:
        collect(x - 1)
    return lst
result = collect(2)
print(result)



def func1(lst):
    d = {x: i for i, x in enumerate(lst)}
    keys = list(d.keys())
    d[keys[0]] = d[keys[1]]
    return d
print(func1([10, 20, 30])[10])

a = [1, 2, 3]
b = a
a = a + [4, 5]
print(a)
print(b)
