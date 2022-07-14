#this hash map uses difference chaining

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for x in range(array_size)]

    def hash(self, key):
        encoded_key = key.encode()
        hash_code = sum(encoded_key)
        return hash_code 

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        
        if self.array[array_index] == None:
            self.array[array_index] = [key, value]
            return 

        if self.array[array_index] == key:
            self.array[array_index] = [key, value]
            return

    def retrieve(self, key):
        retrieve_index = self.compress(self.hash(key))

        if self.array[retrieve_index] == None:
            return None

        if self.array[retrieve_index][0] == key:
            return str(self.array[retrieve_index][1])

nifty_map = HashMap(10)
nifty_map.assign("Person", "Man")
print(nifty_map.retrieve("Person"))
