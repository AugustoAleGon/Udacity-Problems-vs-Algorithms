## Request Routing in a Web Server with Trie ##

We use a Trie for routing in a web server. This Trie is different from the one that we saw in class, because it has some specific methods for remove additional slash at the end to find a route, add not found handler.

We are gonna proceed to describe the methods that we implemented.

add_handler method just called the insert method. The time and space complexity of this method is the same time complexity of the insert method.

lookup method is a search method on the trie, in the worst case the time complexity is O(n). The space complexity in this method is O(1) since we are just using and replace the same variable. In the look up method we are using the find method.

find method has the same complexity in terms of time and space than lookup method.

insert method just dive into the trie until we find an empty slot and then we add it. In terms of time complexity is O(n) and space complexity is O(1).

The time complexity is O(n), which n is the lenght of path_list.
The space complexity is O(n), because we need to store the entire path on a map.