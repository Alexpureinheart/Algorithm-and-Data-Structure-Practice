#this is a HashMap using open adresing for collision handling 

from turtle import pos


class HashMap:
    def __init__(self, array_length):
        self.array_length = array_length
        self.array = [None for x in range(array_length)]

    def hash(self, key, collisions_counter = 0):
        encoded_key = key.encode()
        hash_code = sum(encoded_key)
        return hash_code + collisions_counter

    def compress(self, hash_code):
        return hash_code % self.array_length
        

    def assign(self, key, value, collisions = 0):
        array_index = self.compress(self.hash(key))
        if self.array[array_index] == None: 
            self.array[array_index] = [key, value]
            return

        if self.array[array_index] == key:
            self.array[array_index] = [key, value]
            return

        collisions = 1

        while(self.array[array_index] != key):
            new_array_index = self.compress(self.hash(key, collisions))
            
            if self.array[new_array_index] == key:
                self.array[new_array_index] = [key, value]
                return 

            if self.array[new_array_index] == None:
                self.array[new_array_index] = [key, value]
                return
            
            collisions += 1 

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value == None:
            return None

        if possible_return_value[0] == key:
            return str(possible_return_value[1])

        if possible_return_value[0] != key:
            retrieval_collisions = 1

        while possible_return_value != key:
            retrieval_array_index = self.compress(self.hash(key, retrieval_collisions))
            possible_return_value = self.array[retrieval_array_index]

            if possible_return_value == None:
                return None

            if possible_return_value != key:
                retrieval_collisions += 1

            if possible_return_value[0] == key:
                return possible_return_value[1] 

my_hash_map = HashMap(15)
my_hash_map.assign("Panda Bear", "Norman")
print(my_hash_map.retrieve("Panda Bear"))
my_hash_map.assign("Brown Bear", "Bobbins")
print(my_hash_map.retrieve("Brown Bear"))

