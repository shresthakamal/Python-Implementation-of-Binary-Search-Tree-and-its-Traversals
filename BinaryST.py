# Binary search Tree with function to add, search, delete , find largest,
# find lowest, inoredr, preoredr and postorder.

class BST:
    def __init__(self):
        self.size = 0  # as the initial size of the tree is zero
        self._root = None  # no elememt means no root element

    class BSTnode:
        def __init__(self, key, value):  # key is the value of node
            self.left = None
            self.right = None
            self.value = value  # value value
            self.key = key  # id of the single value

    # Add a node to a BST
    def add(self, key, value):
        z = self.BSTnode(key, value)
        x = self._root
        y = None
        while (x != None):  # when there is a root value
            y = x
            if (key < x.key):
                x = x.left
            else:
                x = x.right
        if (y == None):
            self._root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z
        self.size += 1

    # Getting the size of the tree
    def size_(self):
        return self.size

    # Search BST for the requested key
    def search(self, key):
        found = []
        self._search(self._root, key, found)
        return found

    def _search(self, subtree, key, found):
        if (subtree):
            if (key == subtree.key):
                found.append(1)
            elif (key < subtree.key):
                self._search(subtree.left, key, found)
            elif (key > subtree.key):
                self._search(subtree.right, key, found)

    # Find the smallest key
    def SmallestKey(self):
        nodes = []
        self._SmallestKey(self._root, nodes)
        return nodes

    def _SmallestKey(self, subtree, nodes):
        if (subtree):
            if (subtree.left == None):
                nodes.append(subtree.key)
            self._SmallestKey(subtree.left, nodes)

    # Find the largest key
    def LargestKey(self):
        nodes = []
        self._LargestKey(self._root, nodes)
        return nodes

    def _LargestKey(self, subtree, nodes):
        if (subtree):
            if (subtree.right == None):
                nodes.append(subtree.key)
            self._LargestKey(subtree.right, nodes)

    # Delete a key from a BST
    # Given a binary search tree and a key, this function
    # delete the key and returns the new root
    def delete(self, key):
        found = []
        self._delete(self._root, key)
        return found

    def _delete(self, subtree, key):

        if subtree is None:
            return subtree

        # If the key to be deleted is smaller than the subtree's
        if key < subtree.key:
            subtree.left = self._delete(subtree.left, key)

        # If the kye to be delete is greater than the subtree's key
        elif (key > subtree.key):
            subtree.right = self._delete(subtree.right, key)

        # If key is same as subtree's key, then this is the node
        else:
            # Node with only one child or no child
            if subtree.left is None:
                temp = subtree.right
                subtree = None
                return temp

            elif subtree.right is None:
                temp = subtree.left
                subtree = None
                return temp

            # Node with two children: Get the inorder successor
            temp = self.SmallestKey(subtree.right)
            # Copy the inorder successor's content to this node
            subtree.key = temp
            # Delete the inorder successor
            subtree.right = self._delete(subtree.right, temp)

        return subtree

    # In-order traversal
    def inorder(self):
        node = []
        self.inorder_walk(self._root, node)
        return node

    def inorder_walk(self, subtree, node):
        if subtree:
            self.inorder_walk(subtree.left, node)
            node.append(subtree.key)
            self.inorder_walk(subtree.right, node)

    # Pre-order traversal
    def preorder(self):
        node = []
        self.preorder_walk(self._root, node)
        return node

    def preorder_walk(self, subtree, node):
        if subtree:
            node.append(subtree.key)
            self.preorder_walk(subtree.left, node)
            self.preorder_walk(subtree.right, node)

    # Post-order traversal
    def postorder(self):
        node = []
        self.postorder_walk(self._root, node)
        return node

    def postorder_walk(self, subtree, node):
        if subtree:
            self.postorder_walk(subtree.left, node)
            self.postorder_walk(subtree.right, node)
            node.append(subtree.key)


if __name__ == "__main__":
    B = BST()
    n = int(input("Enter the no. of element in Search Tree: "))
    for x in range(n):
        value = int(input("Enter your elememt "))
        print('Adding ', value)
        B.add(value, "A value")

    print("Final Size is ", str(B.size))
    print()

    print("Largest Key", B.LargestKey())
    print("Smallest Key", B.SmallestKey())
    print()

    print("Inorder Sequence : ", B.inorder())
    print("Postorder Sequence : ", B.postorder())
    print("Preorder Sequence : ", B.preorder())
    print()

    _search = int(input("Enter the element to search Search Tree: "))
    print("Key Found in index: ", B.search(_search))
    print()

    _delete = int(input("Enter the element to delete Search Tree: "))
    print("Deleting key ", _delete, str(B.delete(_delete)))
    print("Inorder after deletion", B.inorder())
    print("Final Size is ", str(B.size))
