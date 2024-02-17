from memory import Memory
import utilities


# This class does not provide any actual caching and is used as a
# superclass that is extended for the various strategie. It defines
# two variables that should keep track of cache hits and accessors for
# statistics and testing.
#
# cache_hit_count: should be incremented whenever the cache is hit,
# i.e. if the requested element is already in the cache.
#
# cache_hit_flag: should be set to True if the cache was hit on the
# last request and set to False otherwise
#
# Definitions of lookup in subclasses should update these variables as
# appropriate.
class Cache():

    def name(self):
        return "Cache"

    # Takes two parameters. Parameter memory is the "memory". Size is
    # a non-negative integer that indicates the size of the cache.
    def __init__(self, data, size=5):
        self.memory = Memory(data)
        self.cache_hit_count = 0
        self.cache_hit_flag = False

    # Returns information on the number of cache hit counts
    def get_cache_hit_count(self):
        return self.cache_hit_count

    def get_memory_request_count(self):
        return self.memory.get_request_count()

    # Returns the cache hit flag
    def get_cache_hit_flag(self):
        return self.cache_hit_flag

    # Look up an address. Uses caching if appropriate.
    def lookup(self, address):
        return self.memory.lookup(address)


class CyclicCache(Cache):
    def name(self):
        return "Cyclic"

    # TODO: Edit the code below to provide an implementation of a
    # cache that uses a cyclic caching strategy with the given cache
    # size. You can use additional methods and variables as you see
    # fit as long as you provide a suitable overridding of the lookup
    # method.

    def __init__(self, data, size=5):
        super().__init__(data) 

    # Look up an address. Uses caching if appropriate.

    ##  Check through whole queue, looking for 
    
    def lookup(self, address):
        
        return None


class LRUCache(Cache):
    def name(self):
        return "LRU"

    # TODO: Edit the code below to provide an implementation of a
    # cache that uses a least recently used caching strategy with the
    # given cache size.  You can use additional methods and variables
    # as you see fit as long as you provide a suitable overridding of
    # the lookup method.

    def __init__(self, data, size=5):
        super().__init__(data)

    # Look up an address. Uses caching if appropriate.
    def lookup(self, address):
        return None


class MRUCache(Cache):
    def name(self):
        return "MRU"

    # TODO: Edit the code below to provide an implementation of a
    # cache that uses a most recently used eviction strategy with the
    # given cache size.  You can use additional methods and variables
    # as you see fit as long as you provide a suitable overridding of
    # the lookup method.

    def __init__(self, data, size=5):
        super().__init__(data)

    # Look up an address. Uses caching if appropriate.
    def lookup(self, address):
        return None


class LFUCache(Cache):
    def name(self):
        return "LFU"

    # TODO: Edit the code below to provide an implementation of a
    # cache that uses a least frequently used eviction strategy with
    # the given cache size. For this strategy, the cache should keep a
    # count of the number of times an item has been requested. When
    # evicting, the item that is used least frequently should be
    # removed. If there are two items that have the same frequency,
    # then the item that was added *first*, i.e. the item that has
    # been in the cache for the longest time, should be removed. You
    # can use additional methods and variables as you see fit as long
    # as you provide a suitable overridding of the lookup method.

    def __init__(self, data, size=5):
        super().__init__(data)

    # Look up an address. Uses caching if appropriate.
    def lookup(self, address):
        return None
