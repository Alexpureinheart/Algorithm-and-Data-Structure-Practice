import swap_nodes

#need nodes
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
              #self.print_list()
              #print("")
            current_node2 = current_node2.get_next_node()

    def print_list(self):
        current_node = self.head_node
        while current_node.next_node:
            print(current_node.get_value())
            current_node = current_node.get_next_node()
        print(current_node.get_value())


my_list = Linked_list("Toast")
my_list.add_at_head("Ham")
my_list.add_at_head("Eggs")
my_list.add_at_head("Ham")
my_list.add_at_head("Ham")
my_list.add_at_head("Eggs")

my_list.print_list()
print("")

swap_nodes("Eggs", "Toast", my_list)

my_list.print_list()

        
 