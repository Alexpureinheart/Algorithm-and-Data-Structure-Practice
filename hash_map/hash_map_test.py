class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, head_node=None):
    self.head_node = head_node
  
  def insert(self, new_node):
    current_node = self.head_node

    if not current_node:
      self.head_node = new_node

    while(current_node):
      next_node = current_node.get_next_node()
      if not next_node:
        current_node.set_next_node(new_node)
      current_node = next_node

  def __iter__(self):
    current_node = self.head_node
    while(current_node):
      yield current_node.get_value()
      current_node = current_node.get_next_node()

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while(current_node):
      string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [LinkedList() for x in range(array_size)]

  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for node in list_at_array:
      if key == node[0]:
        node[1] = value
        return 
    list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]
    for node in list_at_index:
      if key == node[0]:
        return node[1]
    return None

nifty_map = HashMap(10)
nifty_map.assign("Person", "Man")
print(nifty_map.retrieve("Person"))
    



  