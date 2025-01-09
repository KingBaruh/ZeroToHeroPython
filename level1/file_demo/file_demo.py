

#########################################
# Question 1 - do not delete this comment
#########################################


def count_words(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    output = open('q1_output.txt', 'w')
    for i, line in enumerate(lines):
        words = line.split()
        counter = 0
        for word in words:
            if len(word) > 2 and word.isalpha():
                counter += 1
        if i == len(lines) - 1:
            output.write(str(counter))
        else:
            output.write(str(counter) + '\n')

    output.close()
    f.close()
    pass


#########################################
# Question 2a - do not delete this comment
#########################################


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def twin_pricks(num):
    f = open('q2a_output_' + str(num) + '.txt', 'w')
    number = 2
    count = 1
    while num > 0:
        if isPrime(number) and isPrime(number + 2):
            f.write(str(count) + '. ' + str(number) + '-' + str(number + 2))
            num -= 1
            count += 1
            if num != 0:
                f.write('\n')
        number += 1
    f.close()
    pass


#########################################
# Question 2b - do not delete this comment
#########################################
def K_boom(n, k):
    f = open('q2b_output_' + str(k) + '_boom_' + str(n) + '.txt', 'w')
    for i in range(n + 1):
        if i % k == 0 and str(k) in str(i):
            f.write('boom-boom!\n')
        elif i % k == 0 or str(k) in str(i):
            f.write('boom!\n')
        else:
            f.write(str(i) + '\n')
    f.close()
    pass


#########################################
# Question 3 - do not delete this comment
#########################################
def decipher_rotate(in_file):
    f = open(in_file, 'r')
    lines = f.readlines()

    output_func_name = in_file[:-4] + '_decipherotate.txt'

    output = open(output_func_name, 'w')
    for line in lines:
        for i in range(0, len(line)):
            if ord('a') <= ord(line[i]) <= ord('z'):
                num = ord(line[i]) - ord('a')
                letter = ord('z') - num

                count = 5
                while count > 0:
                    letter -= 1
                    if letter < ord('a'):
                        letter = ord('z')
                    count -= 1
                output.write(chr(letter))

            elif ord('A') <= ord(line[i]) <= ord('Z'):
                num = ord(line[i]) - ord('A')
                letter = ord('Z') - num

                count = 5
                while count > 0:
                    letter -= 1
                    if letter < ord('A'):
                        letter = ord('Z')
                    count -= 1
                output.write(chr(letter))
            else:
                output.write(line[i])

    output.close()
    f.close()

    return output_func_name


#########################################
# Question 4 - do not delete this comment
#########################################
def analyze_student_scores(students_ids, students_scores):
    output = {}
    dict_ids = {}
    dict_scores = {}

    f_ids = open(students_ids, 'r')
    f_scores = open(students_scores, 'r')

    ids = f_ids.readlines()
    scores = f_scores.readlines()

    for i, line in enumerate(ids):
        if i == len(ids) - 1:
            tup = tuple(line.split(sep=','))
        else:
            tup = tuple(line[:-1].split(sep=','))
        output.update({tup: []})
        dict_ids.update({tup[0]: tup[1]})

    for i, line in enumerate(scores):
        if i == len(scores) - 1:
            tup = tuple(line.split(sep=','))
        else:
            tup = tuple(line[:-1].split(sep=','))

        if tup[0] not in dict_scores:
            dict_scores[tup[0]] = []
        dict_scores[tup[0]].append(int(tup[1]))

    for id_value in dict_scores:
        score = dict_scores[id_value]
        name = dict_ids[id_value]
        output[id_value, name] = score

    f_ids.close()
    f_scores.close()

    return output


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    def compare_files(file1, file2):
        # Open both files for reading
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            # Read lines from both files
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            # Check if the files have the same number of lines
            if len(lines1) != len(lines2):
                print("Files have different number of lines.")
                return

            # Compare line by line
            differences_found = False
            for i in range(len(lines1)):
                if lines1[i] != lines2[i]:
                    differences_found = True
                    print(f"Difference at line {i + 1}:")
                    print(f"File1: {lines1[i]}")
                    print(f"File2: {lines2[i]}")

            # If no differences were found, print that the files are equal
            if not differences_found:
                print("The files are identical.")


    print('==== Q1: Basic tests/output====')
    count_words("../../../../Users/baruh/Downloads/ex3-2425a/Winnie_the_Pooh.txt")
    compare_files("q1_output.txt", "q1_output_sol.txt")
    print("TBD: It is recommended to write here more tests of your own")

    print('==== Q2a: Basic tests/output====')
    twin_pricks(4)
    twin_pricks(10)
    compare_files("q2a_output_4.txt", "q2a_output_4_sol.txt")
    compare_files("q2a_output_10.txt", "q2a_output_10_sol.txt")
    print("TBD: It is recommended to write here more tests of your own")

    print('==== Q2b: Basic tests/output====')
    K_boom(15, 7)
    K_boom(6, 7)
    compare_files("q2b_output_7_boom_6.txt", "q2b_output_7_boom_6.txt")
    compare_files("q2b_output_7_boom_15_sol.txt", "q2b_output_7_boom_15_sol.txt")
    print("TBD: It is recommended to write here more tests of your own")

    print('==== Q3: Basic tests/output====')
    print("The output file has the right name?")
    print(decipher_rotate("q3_input.txt") == "q3_input_decipherotate.txt")
    compare_files("q3_input_decipherotate.txt", "q3_sol.txt")

    print('==== Q4: Basic tests/output====')
    print(analyze_student_scores("students_ids.txt", "students_scores.txt") ==
          {('102', 'Jane'): [50, 94], ('101', 'John'): [79], ('103', 'Emily'): [100, 85], ('104', 'Yossi'): [88, 82],
           ('105', 'Ruth'): [33], ('106', 'Bob'): []})

# ============================== END OF FILE =================================
