# ~~~ This is a template for question 1  ~~~

# implementation of merge sort


# this function gets a list and uses merge sort
def merge_sort_implementation(_input=list):
    counter = 0
    if type(_input) is not list:
        raise TypeError("Invalid Input! needs to be a list")
    counter += 1

    for num in _input:
        counter += 1  # for each assign
        if not (isinstance(num, int) or isinstance(num, float)):
            counter += 2
            raise TypeError("Invalid type of at least one element in the list")
        counter += 2

    res, counter_of_merge_sort = merge_sort(_input)
    return res, counter + counter_of_merge_sort

# return sorted_array, number_of_basic_operations
def merge_sort(_input=list):
    counter = 0

    if len(_input) <= 1:
        counter += 1
        return _input, counter

    counter += 1

    new_lst1, counter_of_half1 = merge_sort_implementation(_input[:len(_input) // 2])
    new_lst2, counter_of_half2 = merge_sort_implementation(_input[len(_input) // 2:])

    counter += counter_of_half1 + counter_of_half2

    res, counter_of_merge = merge(new_lst1, new_lst2)
    return res, counter + counter_of_merge


# lst1 and lst2 are both sorted
def merge(lst1, lst2):
    counter = 0
    index1, index2 = 0, 0
    output_lst = []

    counter += 3  # assign new lst

    while index1 < len(lst1) and index2 < len(lst2):
        counter += 2  # there are two if in the while

        if lst1[index1] < lst2[index2]:
            output_lst.append(lst1[index1])
            index1 += 1
        else:
            output_lst.append(lst2[index2])
            index2 += 1

        counter += 3

    counter += 2

    while index1 < len(lst1):
        output_lst.append(lst1[index1])
        index1 += 1
        counter += 3

    counter += 1

    while index2 < len(lst2):
        output_lst.append(lst2[index2])
        index2 += 1
        counter += 3

    counter += 1

    return output_lst, counter


