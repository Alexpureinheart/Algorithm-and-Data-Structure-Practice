class Hash_map:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for element in range(array_size)]

    def hash(self, key, collision_counter = 0):
        encoded_key = key.encode()
        hash_code = sum(encoded_key)
        return hash_code + collision_counter

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            self.array[array_index] = [key, value]
            return
        
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        #if collisions occur 
        number_collisions = 1

        while current_array_value != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value == None:
                self.array[current_array_value] = [key, value]
                return 

            if current_array_value == key:
                self.array[current_array_value] = [key, value]
                return

            number_collision += 1


    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value == None:
            return None
        
        if possible_return_value[0] == key:
            return possible_return_value[1]

        if possible_return_value[0] != key:
            retrieval_collisions = 1

            while(possible_return_value != key):
                new_hash_code = self.hash(key, retrieval_collisions)
                retrieval_array_index = self.compressor(new_hash_code)
                possible_return_value = self.array[retrieval_array_index]

                if possible_return_value == None:
                    return None

                if possible_return_value != key:
                    retrieval_collisions += 1

                if possible_return_value[0] == key: 
                    return possible_return_value[1]


nice_hashmap = Hash_map(5)
nice_hashmap.assign("car", "Hyundai Voloster N")
print(nice_hashmap.retrieve("car"))

    