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



class Test_MRU_cache(unittest.TestCase):


    def test_mru_1(self):

        mru = MRUCache(data)

        for i in range(5):
            mru.lookup(i)

        # print("\n\n", mru.output_cache(), "\n\n")
                
        for i in range(4, -1, -1):
            # print("looking up", i)
            for _ in range(10):
                mru.lookup(i)

        self.assertEqual(
            mru.get_cache_hit_flag(),
            True
            )

        self.assertEqual(
            mru.get_memory_request_count(),
            5
            )
        
        self.assertEqual(
            mru.get_cache_hit_count(),
            50
            )
                
        mru.lookup(5)

        # print("\nPOST LOOKUP\n", mru.output_cache(), "\n\n")
                
        self.assertEqual(
            ds_keys(mru.output_cache()),
            [ 5, 1, 2, 3, 4 ]
            )
        
        self.assertEqual(
            mru.get_cache_hit_flag(),
            False
            )

        self.assertEqual(
            mru.get_memory_request_count(),
            6
            )
        
        self.assertEqual(
            mru.get_cache_hit_count(),
            50
            )
                

    def test_mru_2(self):

        mru = MRUCache(data)

        for i in range(10):
            mru.lookup(i)

        self.assertEqual(
            ds_keys(mru.output_cache()),
            [ 9, 3, 2, 1, 0 ]
            )

        self.assertEqual(
            mru.get_cache_hit_flag(),
            False
            )

        self.assertEqual(
            mru.get_memory_request_count(),
            10
            )
        
        mru.lookup(0)
        mru.lookup(0)
        mru.lookup(0)

        self.assertEqual(
            mru.get_cache_hit_flag(),
            True
            )

        self.assertEqual(
            ds_keys(mru.output_cache()),
            [ 0, 9, 3, 2, 1 ]
            )
        
        self.assertEqual(
            mru.get_memory_request_count(),
            10
            )
        
        self.assertEqual(
            mru.get_cache_hit_count(),
            3
            )


        
if __name__ == '__main__':
    unittest.main()

