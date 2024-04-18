#!/usr/bin/env python3

import unittest
import utilities

from memory import Memory
from cache import Cache, CyclicCache, LRUCache, MRUCache, LFUCache


data = utilities.sample_data(size=100)


def ds_keys(ds):

    keys_l = []

    for entry in ds:

        print(entry)

        keys_l = keys_l + list(entry.keys())

    return keys_l



class Test_LRU_cache(unittest.TestCase):

    
    def test_lru_1(self):

        lru = LRUCache(data)

        for i in range(5):
            lru.lookup(i)
        
        for i in range(4, -1, -1):
            # print("looking up", i)
            for _ in range(10):
                lru.lookup(i)

        lru.lookup(5)

        self.assertEqual(
            lru.get_cache_hit_flag(),
            False
            )
        
        self.assertEqual(
            lru.get_memory_request_count(),
            6
            )
        
        self.assertEqual(
            lru.get_cache_hit_count(),
            50
            )
                
        self.assertEqual(
            ds_keys(lru.output_cache()),
            [ 5, 0, 1, 2, 3 ]
            )

        
    def test_lru_2(self):

        lru = LRUCache(data)

        for i in range(10):
            lru.lookup(i)
        
        self.assertEqual(
            ds_keys(lru.output_cache()),
            [ 9, 8, 7, 6, 5 ]
            )
        
        self.assertEqual(
            lru.get_cache_hit_flag(),
            False
            )

        print("break")
        
        print(lru.output_cache())

        print("break")
        
        lru.lookup(0)

        print(lru.output_cache())

        self.assertEqual(
            ds_keys(lru.output_cache()),
            [ 0, 9, 8, 7, 6 ]
            )
        
        self.assertEqual(
            lru.get_cache_hit_flag(),
            False
            )
        
        lru.lookup(8)

        self.assertEqual(
            lru.get_cache_hit_flag(),
            True
            )

        self.assertEqual(
            ds_keys(lru.output_cache()),
            [ 8, 0, 9, 7, 6 ]
            )
        
        self.assertEqual(
            lru.get_memory_request_count(),
            11
            )
        
        self.assertEqual(
            lru.get_cache_hit_count(),
            1
            )


        
if __name__ == '__main__':
    unittest.main()

