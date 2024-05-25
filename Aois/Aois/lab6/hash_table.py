class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash_function(self, key):
        print("V:", ((let_num(key[0]) - 1) * 33 + (let_num(key[1]) - 1)))
        print("Hash:", ((let_num(key[0]) - 1) * 33 + (let_num(key[1]) - 1)) % 20)
        return ((let_num(key[0]) - 1) * 33 + (let_num(key[1]) - 1)) % 20

    def insert(self, key, value):
        index = self.hash_function(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            self.size += 1
        else:
            while node is not None:
                if node.key == key:
                    node.value = value  # Обновление значения, если ключ уже существует
                    return
                prev = node
                node = node.next
            prev.next = Node(key, value)
            self.size += 1

    def find(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result
def let_num(let):
    let = let.lower()
    if let == 'ё':
        return let_num('е') + 1
    return ord(let) - ord('а') + 1 + (ord(let) > (ord('е')))

