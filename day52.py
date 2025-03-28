class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:  # Update existing key
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Key not found

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def display(self):
        for i, node in enumerate(self.table):
            if node:
                values = []
                current = node
                while current:
                    values.append(f"{current.key}: {current.value}")
                    current = current.next
                print(f"Bucket {i}: " + " -> ".join(values))
            else:
                print(f"Bucket {i}: Empty")

# Example Usage
ht = HashTable(5)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("grape", 30)
ht.insert("apple", 40)  # Update existing key
ht.display()
print("Get apple:", ht.get("apple"))  # 40
ht.remove("banana")
ht.display()
