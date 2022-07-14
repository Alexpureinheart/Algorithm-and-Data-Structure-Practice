class HashMap:
    def __init__(self, array_length):
        self.array_length = array_length
        self.array = [None for x in range(array_length)]

    def hash(self, key):
        encoded_key = key.encode()
        hash_code = sum(encoded_key)
        return hash_code

    def compress(self, hash_code):
        return hash_code % self.array_length
        

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        if self.array[array_index] == None: 
            self.array[array_index] = [value]

        if self.array[array_index] == key:
            self.array[array_index] = [value]

            

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        if self.array[array_index] == None:
            return None

        if self.array[array_index] != None:
            return str(self.array[array_index][0])

my_hash_map = HashMap(15)
my_hash_map.assign("Panda Bear", "Norman")
print(my_hash_map.retrieve("Panda Bear"))

