#!/usr/bin/env python3

import unittest
import utilities

from memory import Memory
from cache import Cache, CyclicCache, LRUCache, MRUCache, LFUCache


data = utilities.sample_data(size=100)
    
class Test_stateless_methods(unittest.TestCase):

    def test_gen_cache(self):
        
        c_size = 10

        blah = Cache(data, c_size)

        new_cache = blah.generate_set(c_size)

        self.assertEqual(
            [{-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}],
            new_cache
            )

        
    def test_check_if_in_cache_valid(self):
        
        c_size = 10

        blah = Cache(data, c_size)

        cache = blah.generate_set(c_size)

        res, pos = blah.check_if_in_set(cache, -1)

        self.assertEqual(
            res,
            True
            )


        
        

if __name__ == '__main__':
    unittest.main()

