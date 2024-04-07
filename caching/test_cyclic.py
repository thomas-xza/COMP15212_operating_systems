#!/usr/bin/env python3

import unittest
import utilities

from memory import Memory
from cache import Cache, CyclicCache, LRUCache, MRUCache, LFUCache


data = utilities.sample_data(size=100)
    
class Test_Cyclic_cache(unittest.TestCase):

    
    def test_cyclic_1(self):

        cyclic = CyclicCache(data)

        for i in range(5):
            cyclic.lookup(i)

        self.assertEqual(
            cyclic.get_cache_hit_flag(),
            False
            )
        
        self.assertEqual(
            cyclic.get_memory_request_count(),
            5
            )
        
        self.assertEqual(
            cyclic.get_cache_hit_count(),
            0
            )
        
        self.assertEqual(
            cyclic.output_cache(),
            [{0: 'eccbc87e'},
             {1: 'c81e728d'},
             {2: 'c4ca4238'},
             {3: 'cfcd2084'},
             {4: '8f14e45f'}]
            )
        
        self.assertEqual(
            cyclic.output_cache_ptr(),
            0
            )

        ####  LOOKUP  ####
        
        cyclic.lookup(4)

        ####  LOOKUP  ####
        
        self.assertEqual(
            cyclic.get_cache_hit_flag(),
            True
            )
        
        self.assertEqual(
            cyclic.get_memory_request_count(),
            5
            )
        
        self.assertEqual(
            cyclic.get_cache_hit_count(),
            1
            )
        
        self.assertEqual(
            cyclic.output_cache(),
            [{0: 'eccbc87e'},
             {1: 'c81e728d'},
             {2: 'c4ca4238'},
             {3: 'cfcd2084'},
             {4: '8f14e45f'}]
            )
        
        self.assertEqual(
            cyclic.output_cache_ptr(),
            0
            )
        
        ####  LOOKUP  ####
        
        cyclic.lookup(5)

        ####  LOOKUP  ####
        
        self.assertEqual(
            cyclic.get_cache_hit_flag(),
            False
            )
        
        self.assertEqual(
            cyclic.get_memory_request_count(),
            6
            )
        
        self.assertEqual(
            cyclic.get_cache_hit_count(),
            1
            )
        
        self.assertEqual(
            cyclic.output_cache(),
            [{5: '1679091c'},
             {1: 'c81e728d'},
             {2: 'c4ca4238'},
             {3: 'cfcd2084'},
             {4: '8f14e45f'}]
            )
        
        self.assertEqual(
            cyclic.output_cache_ptr(),
            1
            )
        

        

if __name__ == '__main__':
    unittest.main()

