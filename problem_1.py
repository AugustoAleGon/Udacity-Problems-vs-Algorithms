def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number < 0):
        print("The square root of a negative number is an imaginary number")
        return None
    if(number == 0):
        return 0
    if(number == 1):
        return 1

    # Using binary search taking advantage of the solution log(n)
    left = 0
    right = number
    result = 0
    while left <= right:
        result = (right + left) // 2
        target = result * result
        if target == number:
            return result
        elif target < number:
            left = result - 1
        else:
            lower_target = (result -1) * (result -1)
            if(lower_target < number):
                return (result - 1)
            right = result + 1
    return result


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if (2 == sqrt(5)) else "Fail")