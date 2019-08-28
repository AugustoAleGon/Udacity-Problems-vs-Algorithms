def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Handle edge case.
    if (len(input_list) == 0):
        return -1
    return search(input_list, number, 0, len(input_list) - 1)

def search(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    # Calculate the middle between the whole array
    mid_index = (start_index + end_index) // 2
    mid_value = array[mid_index]
    start_value = array[start_index]
    end_value = array[end_index]
    if start_value == target:
        return start_index
    if mid_value == target:
        return mid_index
    if end_value == target:
        return end_index
    if start_value > end_value:
        # That means that we have the greater numbers at the beginning
        if mid_value > target:
            # Compare the last value so we can choose between a binary search
            if target > end_index:
                return binary_search(array, target, start_index, mid_index -1)
            else:
                return search(array, target, mid_index + 1, end_index)
        else:
            # That means that we are close to the pivot point so we can call the same funcion
            if target > end_index:
                return search(array, target, start_index, mid_index - 1)
    else:
        # That means that we have the greater numbers at the end of the array so is a sorted array
        return binary_search(array, target, start_index, mid_value -1)

def binary_search(array, target, start_index, end_index):
    if(start_index > end_index):
        return -1
    # Calculate the middle index
    mid_index = (start_index + end_index) // 2
    mid_value = array[mid_index]

    if mid_value == target:
        return mid_index
    elif mid_value > target:
        return binary_search(array, target, start_index, mid_index - 1)
    else:
        return binary_search(array, target, mid_index + 1, end_index)
            

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 90])