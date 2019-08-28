## Autocomplete with Tries ##

We have the Trie Class and the TrieNode Class. In the TrieNode class we have the insert methods which time complexity is O(n), which n is the length of the word.
Also in the TrieNode class we have the suffix method, which time complexity is O(n*m), which n is the length of the children and m is the recursion depth (the lenght of the word).

In conclusion we can say that the time complexity of the Triee autocomplete is O(n*m), and the space complexity is O(n) , which n is the number of words that have the same prefix.