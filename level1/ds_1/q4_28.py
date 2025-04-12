# ~~~ This is a template for question 4 (bonus)  ~~~

#implementation of selection sort



    
    
    
#this function gets a list and uses selection sort
def selection_sort_implementation(_input: list[int]):
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

    for i in range(len(_input)):
        min_index = i
        counter += 2
        for j in range(i+1, len(_input)):
            if _input[min_index] > _input[j]:
                min_index = j
                counter += 1
            counter += 2

        _input[i], _input[min_index] = _input[min_index], _input[i]
        counter += 2

    return _input, counter

print(selection_sort_implementation([4,5,646,5,3,6,7,8,9]))


