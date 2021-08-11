import unittest
 
 
class ArrayList:
    def __init__(self):
        self.my_array = []
 
    def get_at_index(self, index):
        return self.my_array[index]
 
    def add_at_end(self, value):
        self.my_array = [
            self.my_array[i] if i < len(self.my_array) else value
            for i in range(len(self.my_array) + 1)
        ]
        print(self.my_array)
 
    def remove_index(self, index):
        """Remove the element at the passed index"""
        self.my_array = self.my_array[:index] + self.my_array[index + 1 :]
        return self.my_array
 
    def count_list(self):
        count = 0
        for element in self.my_array:
            count += 1
        return count
 
 
class TestArrayList(unittest.TestCase):
    def test_init_gives_empty_array(self):
        self.assertEqual(ArrayList().my_array, [])
 
    def test_add_at_end_works_with_empty_array(self):
        array_list = ArrayList()
        array_list.add_at_end(42)
 
        self.assertEqual(array_list.my_array, [42])
 
    def test_multiple_additions(self):
        array_list = ArrayList()
        array_list.add_at_end(3)
        array_list.add_at_end(123)
 
        self.assertEqual(array_list.my_array, [3, 123])
 
    def test_length(self):
        array_list = ArrayList()
        array_list.add_at_end(3)
        array_list.add_at_end(123)
 
        self.assertEqual(array_list.count_list(), 2)
 
    def test_get_at_index_in_middle(self):
        array_list = ArrayList()
        array_list.add_at_end(3)
        array_list.add_at_end(123)
        array_list.add_at_end(8)
 
        self.assertEqual(array_list.get_at_index(1), 123)
 
    def test_remove_front_after_adding_multiple(self):
        array_list = ArrayList()
        array_list.add_at_end(3)
        array_list.add_at_end(123)
        array_list.add_at_end(8)
 
        array_list.remove_index(0)
 
        self.assertEqual(array_list.my_array, [123, 8])
 
 
if __name__ == "__main__":
    unittest.main()



import unittest
 
 
class LinkListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def get_at_index(self, index):
        if self.count_list() <= index:
            return None
        current = self.head  # set to the beginning
        count = 0  # starting counter
        while count < index:  # going down list
            current = current.next_node  # moving down list from node to node
            count += 1  # counter
        return current.value  # returning the value that was reached.
 
    def add_at_end(self, value):
        node_to_add = LinkListNode(value)  # creating a node thats not connected
        if self.head == None:
            self.head = (
                self.tail
            ) = node_to_add  # deciding where node goes (first = last) type thing
        else:
            self.tail.next_node = node_to_add  # adding to end of list
            self.tail = node_to_add  # setting it to be the tail
 
    def remove_index(self, index):
        prev = None
        current = self.head
        if(self.count_list() == 0 or index >= self.count_list()):
            return
        if(index == 0):
            self.head = self.head.next_node
            return
        count = 0
        while current is not None:
            if(count == index):
                if(self.count_list() == index - 1):
                    self.tail = prev
                    prev.next_node = None
                    return
                prev.next_node = current.next_node
                return
            count += 1
            prev = current
            current = current.next_node
    #first attempt (no good)
        '''moving_var = self.head

        if moving_var is not index:        << moving var is a node index is a number so it would be if index not 0
            if moving_var.value == index:  << index is not value its number in the list
                self.head = moving_var.next_node <<this is good
                moving_var = None                << not needed
                return
        while moving_var is not None:            << good but needs a count to track index
            if moving_var.value == index:        << value is not index
                break                            << can just do the work and return instead of breaking
            prev = moving_var                    << good
            moving_var = moving_var.next_node    << good
        if moving_var == None:                   << can just return if code below is moved up
            return
        prev.next_node = moving_var.next_node    << move up to break
        moving_var = None                        << not needed '''
    ##
    def count_list(self):                    #count works great
        count = 0
        current = self.head
        while current != None:
            current = current.next_node
            count += 1
        return count


 
 
class TestLinkedList(unittest.TestCase):
    def test_init_has_no_head(self):
        self.assertIsNone(LinkedList().head)
 
    def test_add_at_end_works_with_empty_array(self):
        linked_list = LinkedList()
        linked_list.add_at_end(42)
 
        self.assertEqual(linked_list.head.value, 42)
 
    def test_multiple_additions(self):
        linked_list = LinkedList()
        linked_list.add_at_end(3)
        linked_list.add_at_end(123)
 
        self.assertEqual(linked_list.get_at_index(0), 3)
        self.assertEqual(linked_list.get_at_index(1), 123)
 
    def test_length(self):
        linked_list = LinkedList()
        linked_list.add_at_end(3)
        linked_list.add_at_end(123)
 
        self.assertEqual(linked_list.count_list(), 2)
 
    def test_get_at_index_in_middle(self):
        linked_list = LinkedList()
        linked_list.add_at_end(3)
        linked_list.add_at_end(123)
        linked_list.add_at_end(8)
 
        self.assertEqual(linked_list.get_at_index(1), 123)
 
    def test_remove_front_after_adding_multiple(self):
        linked_list = LinkedList()
        linked_list.add_at_end(3)
        linked_list.add_at_end(123)
        linked_list.add_at_end(8)
 
        linked_list.remove_index(0)
 
        self.assertEqual(linked_list.my_array, [123, 8])
 
 
if __name__ == "__main__":
    unittest.main()
