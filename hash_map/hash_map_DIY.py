class HashMap:
    def __init__(self, array_length):
        self.array_length = array_length
        self.array = [None for x in range(array_length)]

    def hash(self, key):
        encoded_key = key.encode()
        hash_code = sum(encoded_key)
        return hash_code

    def compress(self, hash_code):
        array_index = hash_code % self.array_length
        return array_index

    def assign(self, key, value):
        pass

