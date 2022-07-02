class Node():
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class Linked_list():

    def __init__(self, value):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def add_at_head(self, value):
        if self.get_head_node() == None:
            self.head_node = Node(value)
        else:
            old_head = self.head_node
            new_head = Node(value, old_head)
            self.head_node = new_head

    def remove_node(self, value_to_remove):
        if self.head_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()
        else:
            current_node = self.head_node
            while current_node.next_node:
                if current_node.next_node.get_value() == value_to_remove:
                    current_node.next_node = current_node.next_node.get_next_node() 
                current_node = current_node.get_next_node()

    def remove_nodes_of_value(self, value_to_remove):
        current_node = self.get_head_node()
        counter = 0
        while current_node.next_node:
            if current_node.get_value() == value_to_remove:
                counter += 1
            current_node = current_node.get_next_node()
        current_node2 = self.head_node
        while counter > 0:
            if current_node2.value == value_to_remove: 
              self.remove_node(value_to_remove)
              counter -= 1
              #print(counter)
              #self.stringify_list()
              #print("")
            current_node2 = current_node2.get_next_node()
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list


class Stack():
    def __init__(self, max_size = None):
        self.top_value = None
        self.size = 0
        self.max_size = max_size

    def push(self, value):
        if self.size == self.max_size:
            return(print("Stack full!"))
        else:
            new_node = Node(value)
            new_node.set_next_node(self.top_value)
            self.top_value = new_node
            self.size += 1
        
    def pop(self):
        if self.size == 0:
            return(print("Stack empty!"))
        elif self.size == 1: 
            to_be_removed = self.top_value
            self.top_value = None
            self.size -= 1
            return to_be_removed
        else:
            to_be_removed = self.top_value
            self.top_value = to_be_removed.get_next_node()
            to_be_removed.next_node = None
            self.size -= 1
            return to_be_removed
    

    def peek(self):
        if self.size == 0:
            return(print("Stack Empty!"))
        else:
            return self.top_value.get_value() + "\n"

my_stack = Stack(5)
my_stack.push("Green eggs and ham")
print(my_stack.peek())
my_stack.push("Hop on pop")
print(my_stack.peek())
my_stack.push("The Lorax")
print(my_stack.peek())
my_stack.push("The Bread and Butter Battle")
print(my_stack.peek())
my_stack.push("The letters after Z")
print(my_stack.peek())
my_stack.push("Yurtle the Turtle")
print(my_stack.peek())

my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())



            
            
        

        
        