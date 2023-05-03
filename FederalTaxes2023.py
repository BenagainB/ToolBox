# 2023FederalTaxes.py
""" contains Node class and SinglyLinkedList class """

class Node:
    """ simple Node class for Linked List Class """
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev = prev_node  # not used for singly linked list
        self.next = next_node

    def get_next(self):
        """ return the node after current node """
        return self.next

    def set_next(self, node):
        """ set the node to follow current node """
        self.next = node

    def get_value(self):
        """ return the value assigned to the current node """
        return self.value

    def set_value(self, value):
        """ set the value of the current node """
        if value is None:
            return
        self.value = value

class SinglyLinkedList:
    """ LinkedList class with only knowledge of head node """
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        """ return the number of nodes in the LinkedList """
        return self.size

    def add_first(self, node):
        """ add node at the beginning of the list """
        if node is None:
            return
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def add_last(self, node):
        """ add node at the end of the list """
        if self.size == 0:
            self.add_first(node)
        else:
            cur = self.head
            while cur.get_next() is not None:
                cur = cur.get_next()
            cur.set_next(node)
            self.size += 1

class SingleFiler():
    """ docstring """
    def __init__(self):
        self.tax_rate = 0
        self.tax_bracket = []
        self.tax_owed = 0

def main():
    """ main function """
    income = input("How much gross income did you make in the 2023 tax year? ")
    income = income.strip("$").strip(" ").strip(",").strip(".")
    income = float(income.replace(",",""))
    
    print(income)
    print(type(income))

if __name__ == "__main__":
    main()
