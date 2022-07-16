#this hash map uses difference chaining
#this hash map seems to be saving lists as node
#values though I'm not entirely sure why
#it works though . . . 

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
        self.head_node = head_node

    def get_head_node(self):
        return self.head_node

    def add_head(self, value):
        if self.head_node == None:
            self.head_node = Node(value)
        else: 
            temp = self.head_node
            self.head_node = Node(value)
            self.head_node.next_node = temp

    def __iter__(self):
        current_node = self.head_node
        while(current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()

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

    def hash(self, key):
        hash_code = sum(key.encode()) 
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
        list_at_array.add_head(payload)        

    def retrieve(self, key):
        retrieve_index = self.compress(self.hash(key))
        list_at_index = self.array[retrieve_index]
        for node in list_at_index:
            if key == node.value[0]:
                return node.value[1]
        return None



nifty_map = HashMap(10)
nifty_map.assign("Person", "Francis")
nifty_map.assign("Cat", "William")
print(nifty_map.retrieve("Person"))
print(nifty_map.retrieve("Cat"))
