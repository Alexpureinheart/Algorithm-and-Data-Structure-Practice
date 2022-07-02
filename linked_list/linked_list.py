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


def swap_nodes(val_1, val_2, input_list):
    node_1 = input_list.get_head_node()
    node_2 = input_list.get_head_node()

    node_1_prev = None
    node_2_prev = None

    while node_1.next_node:
        if node_1.get_value() == val_1:
            break
        node_1_prev = node_1
        node_1 = node_1.get_next_node()

    while node_2.next_node:
        if node_2.get_value() == val_2:
            break
        node_2_prev = node_2
        node_2 = node_2.get_next_node()

    if node_1_prev == None:
        input_list.head_node = node_2
    else:
        node_1_prev.set_next_node(node_2)

    if node_2_prev == None:
        input_list.head_node = node_1
    else:
        node_2_prev.set_next_node(node_1)

        temp = node_1.get_next_node()
        node_1.set_next_node(node_2.get_next_node())
        node_2.set_next_node(temp)


my_list = Linked_list("Toast")
my_list.add_at_head("Ham")
my_list.add_at_head("Eggs")
my_list.add_at_head("Ham")
my_list.add_at_head("Ham")
my_list.add_at_head("Eggs")
print(my_list.stringify_list())
swap_nodes("Eggs", "Toast", my_list)
print(my_list.stringify_list())




        
 