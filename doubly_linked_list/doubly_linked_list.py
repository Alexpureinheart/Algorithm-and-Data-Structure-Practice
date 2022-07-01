class Node():
    def __init__(self, value, previous_node, next_node):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.get_next_node

    def get_previous_node(self):
        return self.previous_node

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

    def set_previous_node(self, new_previous_node):
        self.previous_node = new_previous_node

    