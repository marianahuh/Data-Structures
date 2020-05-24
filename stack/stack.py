"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        # set to DLL
        self.storage = DoublyLinkedList()

    def __len__(self):
        # return length of what is stored in DLL
        return len(self.storage)

    def push(self, value):
        # increase and add end
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # check if empty
        if self.size == 0:
            return None
        # decrease and remove from end
        del_value = self.storage.remove_from_tail()
        self.size -= 1
        return del_value
