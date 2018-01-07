"""
Data Structure for an unbalanced Binary Search Tree
"""


class BinarySearchTree:

    def __init__(self, data=None):
        """
        __init__() method if the BinarySearchTree Class.
        The value of data can only be an int
        """
        if data is not None:
            self.root = Node(data)
        else:
            self.root = None

    def is_empty(self):
        """
        This function checks checks if the Binary Search Tree
        instance is empty
        """
        return self.root is None

    def insert(self, data):
        """
        This function inserts a node into the Binary Search Tree
        instance. The value if data can only be an integer.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert(data, self.root)

    def search(self, data):
        """
        This function searches for a node with the given value
        and returns that node.
        """
        if self.root is not None:
            return self.__search(data, self.root)
        else:
            raise TreeIsEmpty

    def get_minimum(self):
        """
        This function returns the most minimum number in the Binary
        Search Tree Instance
        """
        if self.root is not None:
            return self.__get_minimum(self.root)
        else:
            raise TreeIsEmpty

    def get_maximum(self):
        """
        This function returns the most maximum number in the Binary
        Search Tree Instance
        """
        if self.root is not None:
            return self.__get_maximum(self.root)
        else:
            raise TreeIsEmpty

    def delete(self, data):
        """
        This function deletes the node containing that value given from
        the Binary Search Tree instance
        """
        if self.root is not None:
            self.__delete(data, self.root)
        else:
            raise TreeIsEmpty

    def inorder(self):
        """
        This function prints the nodes in the Binary Search Tree instance
        in inorder
        """
        if self.root is not None:
            self.__inorder(self.root)
        else:
            raise TreeIsEmpty

    def preorder(self):
        """
        This function prints the nodes in the Binary Search Tree instance
        in preorder
        """
        if self.root is not None:
            self.__preorder(self.root)
        else:
            raise TreeIsEmpty

    def postorder(self):
        """
        This function prints the nodes in the Binary Search Tree instance
        in postorder
        """
        if self.root is not None:
            self.__postorder(self.root)
        else:
            raise TreeIsEmpty

    # Private methods

    def __insert(self, data, node):
        """
        This function recursively goes through the Binary Search Tree
        and inserts the given node in the correct place
        """
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__insert(data, node.right)

    def __search(self, data, node):
        """
        This function recursively goes through the Binary Search Tree
        to search for the given node
        """
        if data == node.data:
            return node
        else:
            if data <= node.data:
                if node.left is None:
                    raise NodeNotFound(data)
                else:
                    return self.__search(data, node.left)
            else:
                if node.right is None:
                    raise NodeNotFound(data)
                else:
                    return self.__search(data, node.right)

    def __get_minimum(self, node):
        """
        This function recursively goes through the Binary Search Tree
        and returns the left most node
        """
        if node.left is not None:
            return self.__get_minimum(node.left)
        return node

    def __get_maximum(self, node):
        """
        This function recursively goes through the Binary Search Tree
        and returns the right most node
        """
        if node.right is not None:
            return self.__get_maximum(node.right)
        return node

    def __delete(self, data, node, parent=None, direction=True):
        """
        This function recursively goes through the Binary Search Tree
        and deletes the given node.

        1. If the node to be deleted has no children, the node is simply deleted.
        2. If the node to be deleted has one child, the node is replaced by it's child.
        3. If the node to be deleted has both the children, the next highest node (which
           can be found it the right subtree of the node) replaces that node.

        """
        if data == node.data:
            if node.left is None and node.right is None:
                self.__del_node(parent, direction)
            elif node.left is None:
                self.__del_node(parent, direction, node.right)
            elif node.right is None:
                self.__del_node(parent, direction, node.left)
            else:
                temp_node = node.right
                parent_of_temp_node = node
                temp_direction = False
                while temp_node.left is not None:
                    temp_direction = True
                    parent_of_temp_node = temp_node
                    temp_node = temp_node.left
                while temp_node.right is not None:
                    temp_direction = False
                    parent_of_temp_node = temp_node
                    temp_node = temp_node.right
                self.__del_node(parent_of_temp_node, temp_direction)
                replace_with_node = Node(temp_node.data)
                replace_with_node.left = node.left
                replace_with_node.right = node.right
                self.__del_node(parent, direction, replace_with_node)
        elif data < node.data:
            if node.left is not None:
                self.__delete(data, node.left, parent=node)
            else:
                raise NodeNotFound(data)
        else:
            if node.right is not None:
                self.__delete(data, node.right, parent=node, direction=False)
            else:
                raise NodeNotFound(data)

    def __del_node(self, parent, direction, node=None):
        """
        This functions performs the actual deletion
        """
        if parent is None:
            self.root = node
        else:
            if direction:
                parent.left = node
            else:
                parent.right = node

    def __inorder(self, node):
        """
        This function recursively goes through the Binary Search Tree
        and prints it in inorder.
        """
        if node.left is not None:
            self.__inorder(node.left)
        print node.data
        if node.right is not None:
            self.__inorder(node.right)

    def __preorder(self, node):
        """
        This function recursively goes through the Binary Search Tree
        and prints it in preorder.
        """
        print node.data
        if node.left is not None:
            self.__preorder(node.left)
        if node.right is not None:
            self.__preorder(node.right)

    def __postorder(self, node):
        """
        This function recursively goes through the Binary Search Tree
        and prints it in postorder.
        """
        if node.left is not None:
            self.__postorder(node.left)
        if node.right is not None:
            self.__postorder(node.right)
        print node.data


class Node:
    """
    Binary Search Tree Custom Node Class
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        left_value = None if self.left is None else self.left.data
        right_value = None if self.right is None else self.right.data
        return "Node Value: {0}. Left Node: {1}. Right Node: {2}".format(self.data, left_value, right_value)


class TreeIsEmpty(Exception):
    """
    Tree is empty Custom Exception Class
    """

    def __init__(self):
        pass

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "BinarySearchTree is empty."


class NodeNotFound(Exception):
    """
    Node Not Found Custom Exception Class
    """

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "{0} not found in BinarySearchTree".format(self.data)
