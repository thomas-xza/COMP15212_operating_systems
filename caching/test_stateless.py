#!/usr/bin/env python3

import unittest
import utilities

from memory import Memory
from cache import Cache, CyclicCache, LRUCache, MRUCache, LFUCache


data = utilities.sample_data(size=100)
    
class Test_stateless_methods(unittest.TestCase):

    
    def test_gen_ds(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        new_ds = blah.generate_ds(c_size)

        self.assertEqual(
            new_ds,
            [ {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1}, {-1: -1} ]
            )

        
    def test_check_if_in_ds_valid(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        ds = blah.generate_ds(c_size)

        res, pos = blah.check_if_in_ds(ds, -1)

        self.assertEqual(
            res,
            True
            )

        self.assertEqual(
            pos,
            0
            )


    def test_check_if_in_ds_invalid(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        ds = blah.generate_ds(c_size)

        res, _ = blah.check_if_in_ds(ds, 2109483289752)

        self.assertEqual(
            res,
            False
            )


    def test_prepend_to_ds(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        ds = blah.generate_ds(c_size)

        for x in range(c_size * 2):

            ds, res = blah.delete_data_from_ds(ds, -1)

            if res == True:
                ds = blah.prepend_to_ds(ds, x, x)
            
        self.assertEqual(
            ds,
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


    def test_delete_from_ds(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        ds = blah.generate_ds(c_size)

        for x in range(c_size):

            ds, res = blah.delete_data_from_ds(ds, -1)

            if res == True:
                ds = blah.prepend_to_ds(ds, x, x)

        ds, _ = blah.delete_data_from_ds(ds, 7)
        ds, _ = blah.delete_data_from_ds(ds, 5)
        ds, _ = blah.delete_data_from_ds(ds, 3)

        self.assertEqual(
            ds,
            [ {-1: -1},
              {-1: -1},
              {-1: -1},
              {9: 9},
              {8: 8},
              {6: 6},
              {4: 4},
              {2: 2},
              {1: 1},
              {0: 0} ]
            )


    def test_push_to_empty_ds(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        ds = blah.generate_ds(c_size)

        pos = 0

        for x in range(c_size):

            ds, pos = blah.push_to_ds(ds, pos, x, x)

        self.assertEqual(
            ds,
            [
                {0: 0},
                {1: 1},
                {2: 2},
                {3: 3},
                {4: 4},
                {5: 5},
                {6: 6},
                {7: 7},
                {8: 8},
                {9: 9}
            ]
            )

        self.assertEqual(
            pos, 0
            )


    def test_push_to_full_ds(self):
        
        c_size = 10
        blah = Cache(data, c_size)
        ds = [
                {0: 0},
                {1: 1},
                {2: 2},
                {3: 3},
                {4: 4},
                {5: 5},
                {6: 6},
                {7: 7},
                {8: 8},
                {9: 9}
            ]

        pos = 0

        ds, pos = blah.push_to_ds(ds, pos, 100, 100)
        ds, pos = blah.push_to_ds(ds, pos, 101, 101)
        ds, pos = blah.push_to_ds(ds, pos, 102, 102)

        self.assertEqual(
            ds,
            [
                {100: 100},
                {101: 101},
                {102: 102},
                {3: 3},
                {4: 4},
                {5: 5},
                {6: 6},
                {7: 7},
                {8: 8},
                {9: 9}
            ]
        )


if __name__ == '__main__':
    unittest.main()

