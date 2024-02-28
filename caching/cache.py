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


    ####################################
    ####  DO NOT TOUCH ABOVE LINES  ####
    ####################################
    
    
    def generate_ds(self, size):

        new_ds = []

        for x in range(size):

            new_ds.append(
                { -1: -1 }
                )

        return new_ds

    
    def check_if_in_ds(self, ds, key):

        ##  Searches though data-struct looking for given key.
        ##    Returns bool and position based on outcome.

        pos = 0

        for ds_dict in ds:

            if key in ds_dict.keys():

                return True, pos

            pos += 1

        return False, 0


    def prepend_to_ds(self, ds, key, data):

        ##  WARNING: will overwrite first entry in data struct.
        ##    Data-struct must therefore be primed by delete_data_from_ds().

        ds[0] = { key: data }

        return ds
    

    def delete_data_from_ds(self, ds, key):

        ##  Iterates through data-struct, in search of key.
        ##  Upon finding key, will delete entry in data-struct,
        ##    then prepend an empty entry to top of data-struct.

        pos = 0

        key_pos = -1

        res = False

        for ds_dict in ds:

            if key in ds_dict.keys():

                key_pos = pos

            pos += 1

        if key_pos != -1:

            del ds[key_pos]

            ds.insert(0, { -1: -1 })

            res = True

        return ds, res

    
    def push_to_ds(self, ds, pos, key, data):

        ##  Will hard overwrite data in data-struct at position given.

        ds[pos] = { key: data }

        if pos + 1 == len(ds):

            next_pos = 0

        else:

            next_pos = pos + 1

        return ds, next_pos

    ##############################################
    ##  GENERIC DATA STRUCTURE FUNCTIONS ABOVE  ##
    ##############################################    
    

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
        self.cache = super().generate_ds(size)
        self.cache_ptr = 0

    # Look up an address. Uses caching if appropriate.

    def lookup(self, address):

        hit, pos = super().check_if_in_ds(self.cache, address)

        if hit == True:

            ##  Set cache hit data.
            self.cache_hit_count += 1            
            self.cache_hit_flag = True

            data = self.cache[pos][address]

        else:
 
            ##  Set cache miss data.
            self.cache_hit_flag = False
            
            ##  Access memory.
            data = super().lookup(address)

            if data is not None:

                ##  Store to cache (if found)
                
                self.cache, self.cache_ptr = super().push_to_ds(
                    self.cache,
                    self.cache_ptr,
                    address,
                    data
                    )

        return data


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
        self.cache = super().generate_ds(size)


    def update_lru_cache(cache, mem_addr, data):

        ##  Check for empty slot in cache.
        
        empty_slot, _ = super().check_if_in_ds(cache, -1)

        res_del = False

        ##  If empty available, delete it and write to cache.
        
        if empty_slot == True:

            cache, res_del = super().delete_data_from_ds(cache, -1)

        else:

            cache, res_del = super().delete_data_from_ds(
                cache,
                len(self.cache) - 1
            )
            
        if res_del == True:

            cache = super().prepend_to_ds(cache, mem_addr, data)

        return cache
            

    # Look up an address. Uses caching if appropriate.
    def lookup(self, address):

        hit, pos_hit = super().check_if_in_ds(self.cache, address)

        if hit == True:

            ##  Set cache hit data.
            self.cache_hit_count += 1            
            self.cache_hit_flag = True

            data = self.cache[pos_hit][address]

        else:
 
            ##  Set cache miss data.
            self.cache_hit_flag = False
            
            ##  Access memory.
            data = super().lookup(address)

            if data is not None:

                ##  Update LRU cache.
                self.cache = super().write_to_lru_cache(
                    self.cache,
                    address,
                    data
                )
                
        return data


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
        self.cache = super().generate_ds(size)

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
        self.cache = super().generate_ds(size)

    # Look up an address. Uses caching if appropriate.
    def lookup(self, address):
        return None
