class Hash_map:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for element in range(array_size)]

    def hash(self, key):
        encoded_key = key.encode()
        hash_code = sum(encoded_key)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        self.array[array_index] = value

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]


nice_hashmap = Hash_map(5)
nice_hashmap.assign("car", "Hyundai Voloster N")
print(nice_hashmap.retrieve("car"))

    