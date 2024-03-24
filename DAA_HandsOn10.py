class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current == self.head:
                    self.head = self.head.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def retrieve(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def is_empty(self):
        return not self.head

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append((current.key, current.value))
            current = current.next
        return str(values)

class HashTable:
    def __init__(self):
        self.init_capacity = 8
        self.load_factor = 4
        self.capacity = self.init_capacity
        self.size = 0
        self.table = [DoublyLinkedList() for _ in range(self.capacity)]

    def hash(self, key):
        Golden_Ratio = 0.6180339887  
        scaled = key * Golden_Ratio
        fraction = scaled - int(scaled)  
        return int(self.capacity * fraction)

    def resize(self, new_capacity):
        new_table = [DoublyLinkedList() for _ in range(new_capacity)]
        for bucket in self.table:
            current = bucket.head
            while current:
                new_index = self.hash(current.key)
                new_table[new_index].add(current.key, current.value)
                current = current.next
        self.table = new_table
        self.capacity = new_capacity

    def add(self, key, value):
        if self.size >= self.capacity * self.load_factor:
            self.resize(self.capacity * 2)
        index = self.hash(key)
        self.table[index].add(key, value)
        self.size += 1

    def delete(self, key):
        index = self.hash(key)
        if self.table[index].delete(key):
            self.size -= 1
        if self.size < self.capacity // 4:
            self.resize(self.capacity // 2)

    def retrieve(self, key):
        index = self.hash(key)
        return self.table[index].retrieve(key)

    def is_empty(self):
        return self.size == 0
    
    def print_hash_table(self):
        return "\n".join([f"Bucket {i}: {bucket}" for i, bucket in enumerate(self.table)])
        
#Example
hash_table = HashTable()
hash_table.add(2,20 )
hash_table.add(3, 30)
hash_table.add(25, 100)
hash_table.add(35, 150)
print(hash_table.print_hash_table())
print("value for the key 3 is :", hash_table.retrieve(3))
hash_table.delete(3)
print("value for the key 3 after deletion is:", hash_table.retrieve(3))
print(hash_table.print_hash_table())
