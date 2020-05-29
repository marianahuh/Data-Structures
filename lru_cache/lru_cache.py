from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dl_list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # check if key exists in dict storage
        if key not in self.storage:
            return None

        # iterate node through to find the key
        # set as the head node
        node = self.dl_list.head
        while node is not None:
            # if found, move node to the front
            if key == node.value[0]:
                self.dl_list.move_to_front(node)
                break
            node = node.next
        # return the key in storage/dict
        return self.storage[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, val):
        # if key is already stored
        if key in self.storage:
            # overwrite in storage
            self.storage[key] = val
            # overwrite in dll
            # iterate through and find node to update to front
            node = self.dl_list.head
            while node is not None:
                if key == node.value[0]:
                    # update value
                    node.value[1] = val
                    self.dl_list.move_to_front(node)
                    break
                node = node.next
        else:
            # if already full
            if self.size == self.limit:
                # remove the least recently used from tail on dll
                node = self.dl_list.tail
                old_key = node.value[0]
                self.dl_list.remove_from_tail()
                # then delete
                del self.storage[old_key]
                self.size -= 1

            # then add to cache
            self.storage[key] = val
            self.dl_list.add_to_head([key, val])
            self.size += 1
