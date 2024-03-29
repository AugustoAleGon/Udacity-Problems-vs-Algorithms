def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return "Please add a valid input"
    min_value = ints[0]
    max_value = ints[0]
    for value in ints:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return min_value, max_value

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

test1 = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)

print ("Pass" if ((0, 999) == get_min_max(test1)) else "Fail")

test2 = [i for i in range(100)] # a list containing 0 - 99
random.shuffle(test2)

print("Pass" if ((0, 99) == get_min_max(test2)) else "Fail")

## Testing edge case (Empty Array)
test3 = []
print("Pass" if (get_min_max(test3)) == "Please add a valid input" else "Fail")