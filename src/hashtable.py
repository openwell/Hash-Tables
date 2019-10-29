# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)
    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass
    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        indexOfNum = self._hash_mod(key)
        node = self.storage[indexOfNum]
        if self.storage[indexOfNum] is None:
            self.storage[indexOfNum] = LinkedPair(key,value)
        else:
            prev = None
            while node and node.key != key:
                prev = node
                node = node.next
            if node:
                node.value = value
            else:
                prev.next = LinkedPair(key,value)
        # while doing for the current node the prev node need to be considered
        # just in case its none so we can have something to reference 
        #  if the value is the same we change the value

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)
        # current_node = self.storage[index]

        # prev = None
        # if not node:
        #     print('Not found')
        #     return
        # while node and node.key != key:
        #     prev = node
        #     node = node.next
        #     if prev.key == key:
        #         prev = None
        
        # get position
        # prev = None
        # while node:
        #     if 
        #     if node.key == key and prev:
        #         prev.next = node.next
        #     else:
        #         prev = node
        #         node = node.next

        # return None
        # tranverse the linked list 
        # compare the key to see if its a match
        # set prev
        # connect the prev next to node next
        # index = self._hash_mod(key)
    
        # if not self.storage[index]:
        #     print(f"Hash[{key}] cannot be deleted: It does not exist")
        #     return
        # current_node = self.storage[index]
        # prev_node = None
       
        # if current_node.key == key and not current_node.next:
        #     self.storage[index] = None
        # elif current_node.key == key:
        #     self.storage[index] = self.storage[index].next
        # else:
        #     while current_node:
        #         if current_node.key == key:
        #             prev_node.next = current_node.next
        #             return
        #         prev_node = current_node
        #         current_node = current_node.next

        # hashed_key = self._hash_mod(key)
        # if self.storage[hashed_key] is None:
        #     print('Key does not exist', key)
        # else:
        #     self.storage[hashed_key] = None
        
        #check for 1st if it has last then u end the loop
        # if 2nd or any has next... hold the previous
        # cut the node .... hold the next
        # take the prev and join it with the held next

        indexOfNum = self._hash_mod(key)
        node = self.storage[indexOfNum]

        prev = None
        # if node and node.key == key:
        #     if node.next:
        #         node = node.next
        #         return
        #     self.storage[indexOfNum] = None
        # return 'Key does not exist'
            # at this stage we have passed the 1st one
        while node and node.key != key:
            prev = node
            node = node.next
        if node:
            if node.next:
                prev2 = node.next
                prev = prev2
            self.storage[indexOfNum] = None
        else:
            return 'Key does not exist'

        
        
             

                
                  
            

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        indexOfNum = self._hash_mod(key)
        node = self.storage[indexOfNum]

        while node and node.key != key:
		        node = node.next
        if not node:
            return None
        else:
            return node.value
        # we don't have prev? what of if the last node.next is none
        # OR what of the case the node is not having next
        # but i get that the while will handle it

            
    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
