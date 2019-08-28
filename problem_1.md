## Finding the Square Root of an Integer ##

Taking advantage of the binary search tree, we are looking the root square of a number which is a value that multiply by itself results in a the number. In this case we are using the floor value. So our target in the binary search is gonna be the number, and then we are gonna iterate until we find it.

The time complexity is equals to the binary search, so is O(log(n)).
The space complexity is O(1), because we just store one single value and then return it.