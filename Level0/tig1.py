#########################################
# Question 1.a - do not delete this comment
#########################################
def fourbonacci_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    return fourbonacci_rec(n - 1) + fourbonacci_rec(n - 2) + fourbonacci_rec(n - 3) + fourbonacci_rec(n - 4)


#########################################
# Question 1.b - do not delete this comment
#########################################
def k_bonacci(n, k):
    if n <= 0:
        return 0
    elif 0 < n < k:
        return n
    sum_n_step = 0
    for i in range(1, k + 1):
        sum_n_step += k_bonacci(n - i, k)
    return sum_n_step


#########################################
# Question 2 - do not delete this comment
#########################################

def tower_of_hanoi(n, source, target, mid):
    # Base case: if there is only one disk, move it directly from source to target
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Recursive step: move n-1 disks from source to mid using target as auxiliary
    tower_of_hanoi(n - 1, source, mid, target)
    # Move the largest disk (nth disk) from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Recursive step: move n-1 disks from mid to target using source as auxiliary
    tower_of_hanoi(n - 1, mid, target, source)


#########################################
# Question 3 - do not delete this comment
#########################################

def find_missing_sorted(a, b):
    low, high = 0, len(a)

    while low < high:
        mid = (low + high) // 2

        if a[mid] == b[mid]:
            low = mid + 1
        else:
            high = mid

    return b[low]


#########################################
# Question 4 - do not delete this comment
#########################################

def closest(a, x):
    low, high = 0, len(a) - 1

    while low < high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            low = mid
        else:
            high = mid

    if abs(x - a[low]) < abs(x - a[high]):
        return low
    return high


#########################################
# Question 5 - do not delete this comment
#########################################


def find_string(matrix, target):
    hist = [0] * 256
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            hist[ord(matrix[i][j])] += 1

    for char in target:
        if hist[ord(char)] == 0:
            return False
        hist[char] -= 1
    return True
