# Fill the Python code in this file
<<<<<<< HEAD
=======
import unittest
from recursive_json_search import *
from test_data import *
class json_search_test(unittest.TestCase):
    def test_search(self):
        '''key should be found, return list that should not be empty'''
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        '''should return a list'''
        self.assertIsInstance(json_search(key1,data),list)
if __name__ == '__main__':
    unittest.main()
>>>>>>> 6e8073aea465f70004ac670cdca08f9cc4b5b32a
