#!/usr/bin/env python3

import unittest
import utilities

from memory import Memory
from cache import Cache, CyclicCache, LRUCache, MRUCache, LFUCache


data = utilities.sample_data(size=100)
    
class Test_LFU_cache(unittest.TestCase):

    
    def test_lfu_1(self):

        lfu = LFUCache(data)

        for i in range(5):
            lfu.lookup(i)
        
        for i in range(4, -1, -1):
            # print("looking up", i)
            for _ in range(10):
                lfu.lookup(i)

        # print(lfu.output_cache_hits())
        # print("Should get deleted next: ", lfu.output_cache_hits()[-1])

        lfu.lookup(5)

        self.assertEqual(
            lfu.get_cache_hit_flag(),
            False
            )
        
        self.assertEqual(
            lfu.get_memory_request_count(),
            6
            )
        
        self.assertEqual(
            lfu.get_cache_hit_count(),
            50
            )
        
        # print(lfu.output_cache_hits())

        self.assertEqual(
            lfu.output_cache_hits(),
            [{5: 0}, {0: 10}, {1: 10}, {2: 10}, {3: 10}]
            )

        
    def test_lfu_2(self):

        lfu = LFUCache(data)

        for i in range(5):
            lfu.lookup(i)
        
        self.assertEqual(
            lfu.get_cache_hit_flag(),
            False
            )
        
        for i in range(4, -1, -1):
            # print("looking up", i)
            for _ in range(10):
                lfu.lookup(i)

        self.assertEqual(
            lfu.get_cache_hit_flag(),
            True
            )
        
        self.assertEqual(
            lfu.get_memory_request_count(),
            5
            )
        
        self.assertEqual(
            lfu.get_cache_hit_count(),
            50
            )
        
        lfu.lookup(1)
        
        self.assertEqual(
            lfu.get_cache_hit_flag(),
            True
            )
        
        self.assertEqual(
            lfu.get_memory_request_count(),
            5
            )
        
        self.assertEqual(
            lfu.get_cache_hit_count(),
            51
            )
        
        self.assertEqual(
            lfu.output_cache_hits(),
            [{1: 11}, {0: 10}, {2: 10}, {3: 10}, {4: 10}]
            )
        

    def test_lfu_3(self):

        lfu = LFUCache(data, size=10)

        for i in range(10):
            for _ in range(3):
                lfu.lookup(i)

        self.assertEqual(
            lfu.get_memory_request_count(),
            10
            )

        self.assertEqual(
            lfu.get_cache_hit_count(),
            20
            )

        lfu.lookup(10)
        
        self.assertEqual(
            lfu.get_cache_hit_flag(),
            False
            )
        
        self.assertEqual(
            lfu.get_memory_request_count(),
            11
            )
        
        self.assertEqual(
            lfu.get_cache_hit_count(),
            20
            )

        lfu.lookup(5)
        
        self.assertEqual(
            lfu.get_cache_hit_flag(),
            True
            )
        
        self.assertEqual(
            lfu.get_memory_request_count(),
            11
            )
        
        self.assertEqual(
            lfu.get_cache_hit_count(),
            21
            )

        lfu.lookup(5)
        
        self.assertEqual(
            lfu.get_cache_hit_flag(),
            True
            )
        
        self.assertEqual(
            lfu.get_memory_request_count(),
            11
            )
        
        self.assertEqual(
            lfu.get_cache_hit_count(),
            22
            )

        lfu.lookup(0)
        
        self.assertEqual(
            lfu.get_cache_hit_flag(),
            False
            )
        
        self.assertEqual(
            lfu.get_memory_request_count(),
            12
            )

        self.assertEqual(
            lfu.get_cache_hit_count(),
            22
            )
        
        self.assertEqual(
            lfu.output_cache_hits(),
            [ {0: 0}, {5: 4},
              {9: 2}, {8: 2}, {7: 2}, {6: 2},
              {4: 2}, {3: 2}, {2: 2}, {1: 2} ]
            )
        
        
if __name__ == '__main__':
    unittest.main()

