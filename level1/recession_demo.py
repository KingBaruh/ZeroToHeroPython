

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
# Question 2.a - do not delete this comment
#########################################
def climb_combinations(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_combinations(n - 1) + climb_combinations(n - 2)


#########################################
# Question 2.b - do not delete this comment
#########################################
def tomer_climb_combinations(n, steps):
    if n <= 0:
        return 0

    total_ways = 0

    for step in steps:
        if n - step == 0:
            total_ways += 1
        else:
            total_ways += tomer_climb_combinations(n - step, steps)

    return total_ways


#########################################
# Question 3.a - do not delete this comment
#########################################
def weigh_str(input_str):
    if len(input_str) == 1 or len(input_str) == 0:
        return 0
    weigh = 0
    if input_str[0] > input_str[-1]:
        weigh = 1
    elif input_str[0] < input_str[-1]:
        weigh = -1
    else:
        weigh = 0
    return weigh + weigh_str(input_str[1:-1])


#########################################
# Question 3.b - do not delete this comment
#########################################
def weigh_str_efficient(input_str, index=0):
    if len(input_str) // 2 == index:
        return 0
    weigh = 0
    if input_str[index] > input_str[-(index + 1)]:
        weigh = 1
    elif input_str[index] < input_str[-(index + 1)]:
        weigh = -1
    else:
        weigh = 0
    return weigh + weigh_str_efficient(input_str, index + 1)


#########################################
# Question 4.a - do not delete this comment
#########################################
def sum_nested(lst):
    if len(lst) == 1:
        if type(lst[0]) is list:
            return sum_nested(lst[0])
        if type(lst[0]) is str:
            return 0
        return abs(lst[0])
    return sum_nested([(lst[0])]) + sum_nested(lst[1:])


#########################################
# Question 4.b - do not delete this comment
#########################################
def count_construct(target, word_bank):
    if target == '':
        return 0
    output = 0
    for word in word_bank:
        if target == word:
            output += 1
        elif target.startswith(word):
            output += count_construct(target[len(word):], word_bank)
    return output


#########################################
# Question 5 - do not delete this comment
#########################################
def gcd(a, b):
    if a > b:
        r = a % b
        if r == 0:
            return b
        else:
            return gcd(b, r)
    elif b > a:
        r = b % a
        if r == 0:
            return a
        else:
            return gcd(a, r)
    else:
        return a


##################################################################################
# For Testing:
##################################################################################
class CountedString(str):
    # Global variable to track the count of string objects
    created_count = 0

    def __init__(self, value):
        self.value = value

    def __getitem__(self, index):
        # Check if a slice operation is being performed
        if isinstance(index, slice):
            CountedString.created_count += 1

        return CountedString(self.value[index])


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    # Question 1.a tests - you can and should add more
    print("Question 1.a tests")
    print(fourbonacci_rec(0) == 0)
    print(fourbonacci_rec(12) == 1174)
    print(fourbonacci_rec(25) == 5953572)

    #Question 1.b tests - you can and should add more
    print("Question 1.b tests")
    print(k_bonacci(0, 2) == 0)
    print(k_bonacci(5, 2) == 5)
    print(k_bonacci(8, 2) == 21)

    print(k_bonacci(0, 3) == 0)
    print(k_bonacci(5, 3) == 11)
    print(k_bonacci(8, 3) == 68)

    print(k_bonacci(0, 5) == 0)
    print(k_bonacci(5, 5) == 10)
    print(k_bonacci(8, 5) == 76)

    #Question 2.a tests - you can and should add more
    print("Question 2.a tests")
    print(climb_combinations(1) == 1)
    print(climb_combinations(5) == 8)
    print(climb_combinations(6) == 13)
    print(climb_combinations(0) == 0)

    # Question 2.b tests - you can and should add more
    print("Question 2.b tests")
    print(tomer_climb_combinations(6, [2, 3]) == 2)
    print(tomer_climb_combinations(3, [2]) == 0)
    print(tomer_climb_combinations(10, [5, 2]) == 2)
    print(tomer_climb_combinations(5, [5, 2, 1]) == 9)
    print(tomer_climb_combinations(0, [5, 2, 1]) == 0)

    #Question 3a tests - you can and should add more
    print("Question 3a tests")
    print(weigh_str("a") == 0)
    print(weigh_str("aba") == 0)
    print(weigh_str("aa") == 0)
    print(weigh_str("AZ") == -1)
    print(weigh_str("cba") == 1)
    print(weigh_str("acsabdrZ") == 0)
    print(weigh_str("DDDDaaaa") == -4)

    #Question 3b tests - you can and should add more
    print("Question 3b tests")
    print(weigh_str_efficient("a") == 0)
    print(weigh_str_efficient("aba") == 0)
    print(weigh_str_efficient("aa") == 0)
    print(weigh_str_efficient("AZ") == -1)
    print(weigh_str_efficient("cba") == 1)
    CountedString.created_count = 0
    print(weigh_str_efficient(CountedString("acsabdrZ")) == 0)
    print(CountedString.created_count == 0)
    CountedString.created_count = 0
    print(weigh_str_efficient(CountedString("DDDDaaaa")) == -4)
    print(CountedString.created_count == 0)

    # Question 4.a tests - you can and should add more
    print("Question 4.a tests")
    print(sum_nested([1, 2, [3, 4], [5, [6, 7], 8], 9]) == 45)
    print(sum_nested([1, 2, [-3, -4.5]]) == 10.5)
    print(sum_nested([1, 2, [-3, -4.5], 'abc', [5, 'abc', [-4, 0.5]]]) == 20.)

    # Question 4.b tests - you can and should add more
    print("Question 4.b tests")
    print(count_construct('purple', ["purp", "p", "ur", "le", "purpl"]) == 2)
    print(count_construct('abcdef', ["ab", "abc", "cd", "def", "abcd"]) == 1)
    print(count_construct('aaaaaaaaaaaaaaaaaaaaaaaz', ["a", "aa", "aaa", "aaaa", "aaaaa"]) == 0)

    #Question 5 - you can and should add more
    print("Question 5 tests")
    print(gcd(98, 56) == 14)
    print(gcd(42, 56) == 14)
    print(gcd(3, 6) == 3)

    pass
# ============================== END OF FILE =================================
