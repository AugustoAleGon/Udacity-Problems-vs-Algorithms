## Rearrange Array Elements ##

In order to get the maximum numbers of an array we will need our input list sorted decreasingly, because we are asked that the expected time complexity is O(nlog(n)), we decided to use a merge sort algorithm to achieve this time complexity.

The time complexity of the algorithm is O(nlog(n))
The space complexity is O(n), because in each iteration we are using an auxiliary array.
