from enum import Enum

class HandlerType(Enum):
    NOT_FOUND = 1
    FOUND = 2

class Handler:
    def __init__(self, name = "", type = HandlerType.NOT_FOUND):
        self.type = type
        self.name = name

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, path, handler_name):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for segment in path:
            if segment not in current_node.children:
                current_node.insert(segment)                
            current_node = current_node.children[segment]

        current_node.handler = Handler(handler_name, HandlerType.FOUND)

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for segment in path:
            if segment in current_node.children:
                current_node = current_node.children[segment]
            else:
                return None
        return current_node

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = Handler()):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler = Handler()):
        self.children[path] = RouteTrieNode(handler)

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, no_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(Handler(handler, HandlerType.FOUND))
        self.not_found = Handler(no_handler, HandlerType.NOT_FOUND)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route.insert(self.split_path(path), handler)

    def lookup(self, path):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == '/':
            return self.route.root.handler.name

        path_list = self.split_path(path)
        node = self.route.find(path_list)

        if node == None or node.handler.type is HandlerType.NOT_FOUND:
            return self.not_found.name
        else:
            return node.handler.name

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler in loopup functions,
        # so it should be placed in a function here
        final = path
        if final.endswith('/'):
            final = final[:-1]

        return final.split('/')

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me/help", "help handler")

# some lookups with the expected output
print(router.lookup(""))  # should print "Please input an valid path!" message.
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me/help")) # should print 'help handler' or None if you did not implement one