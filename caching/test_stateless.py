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
        new_cache = blah.generate_ds(c_size)

        self.assertEqual(
            new_cache,
            [{-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}]
            )

        
    def test_check_if_in_cache_valid(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        cache = blah.generate_ds(c_size)

        res, pos = blah.check_if_in_ds(cache, -1)

        self.assertEqual(
            res,
            True
            )

        self.assertEqual(
            pos,
            0
            )


    def test_check_if_in_cache_invalid(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        cache = blah.generate_ds(c_size)

        res, _ = blah.check_if_in_ds(cache, 2109483289752)

        self.assertEqual(
            res,
            False
            )


    def test_prepend_to_cache(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        cache = blah.generate_ds(c_size)

        for x in range(20):

            cache, res = blah.delete_data_from_ds(cache, -1)

            if res == True:
                cache = blah.prepend_to_ds(cache, x, x)
            
        self.assertEqual(
            cache,
            [ {9: 9},
              {8: 8},
              {7: 7},
              {6: 6},
              {5: 5},
              {4: 4},
              {3: 3},
              {2: 2},
              {1: 1},
              {0: 0} ]
            )


if __name__ == '__main__':
    unittest.main()

