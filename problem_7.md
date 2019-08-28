## Request Routing in a Web Server with Trie ##

We use a Trie for routing in a web server. This Trie is different from the one that we saw in class, because it has some specific methods for remove additional slash at the end to find a route, add not found handler.

The time complexity is O(n), which n is the lenght of path_list.
The space complexity is O(n), because we need to store the entire path on a map.