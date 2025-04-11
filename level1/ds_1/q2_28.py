# ~~~ This is a template for question 2  ~~~

# implementation of insertion sort


# this function gets a list and uses insertion sort
def insertion_sort_implementation(_input=list):
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

    res, counter_of_insertion_sort = insertion_sort(_input)
    return res, counter + counter_of_insertion_sort

def insertion_sort(_input=list):
    counter = 0
    for i in range(1, len(_input)):
        val = _input[i]
        j = i - 1

        counter += 3  # assign to i ,val and j

        while j >= 0 and _input[j] > val:
            counter += 2

            _input[j + 1] = _input[j]
            j -= 1

            counter += 2

        _input[j + 1] = val

        counter += 3

    return _input, counter

