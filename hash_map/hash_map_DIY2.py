#this hash map uses difference chaining

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

    def get_next_node(self):
        return self.next_node

    
class LinkedList:
    def __init__(self, head_node = None):
        self.head_node = None

    def get_head_node(self):
        return self.head_node

    def add_head(self, value):
        self.head_node = Node(value)

    def remove_node(self, value_to_remove):
        if self.head_node.get_value() == value_to_remove:
            if self.head_node.get_next_node() == None:
                self.head_node = None
            else:
                temp = self.get_head_node()
                self.head_node = self.head_node.get_next_node()
                temp.next_node = None

        else:
            current_node = self.get_head_node()
            while current_node:
                if current_node.next_node.get_value() == value_to_remove:
                    if current_node.next_node.next_node == None:
                        current_node.next_node = None
                    else:
                        current_node.next_node = current_node.next_node.get_next_node()
                current_node = current_node.get_next_node()

    def stringify_list(self):
        current_node = self.get_head_node()
        string_list = ""
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "/n"
            current_node = current_node.get_next_node()
        return string_list

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for x in range(array_size)]

    def hash(self, key, number_collisions = 0):
        encoded_key = key.encode()
        hash_code = sum(encoded_key + number_collisions)
        return hash_code 

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for node in list_at_array:
            if key == node[0]:
                node[1] = value
                return
        list_at_array.insert(payload)        

    def retrieve(self, key):
        retrieve_index = self.compress(self.hash(key))
        list_at_index = self.array(retrieve_index)
        for node in list_at_index:
            if key == node[0]:
                return node[1]
        return None

nifty_map = HashMap(10)
nifty_map.assign("Person", "Man")
print(nifty_map.retrieve("Person"))