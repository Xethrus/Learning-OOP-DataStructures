class ArrayList:
    def __init__(self):
        self.my_array = []

    def get_at_index(self, index):
        return self.my_array[index]

    def add_at_end(self, value):
        self.my_array = [self.my_array[i] if i < len(self.my_array) else value for i in range(len(self.my_array)+1)]
        print(self.my_array)

    def remove_index(self, index):
        """Remove the element at the passed index"""
        self.my_array = self.my_array[:index] + self.my_array[index+1:]
        return self.my_array

    def count_list(self):
        count = 0
        for element in self.my_array:
            count += 1
        return count

class LinkListNode():
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
 
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
 
    def get_at_index(self, index):
        if(self.length <= index):
            return None
        current = self.head  #set to the beginning
        count = 0 #starting counter
        while(count < index): #going down list
            current = current.next_node #moving down list from node to node
            count+=1 #counter
        return current.value #returning the value that was reached.

    def add_to_end(self, value):
        node_to_add = LinkListNode(value) #creating a node thats not connected
        if(self.length == 0):
            self.head = self.tail = node_to_add #deciding where node goes (first = last) type thing
        else:
            self.tail.next_node = node_to_add #adding to end of list
            self.tail = node_to_add #setting it to be the tail
        self.length += 1 #updates the length of the list
