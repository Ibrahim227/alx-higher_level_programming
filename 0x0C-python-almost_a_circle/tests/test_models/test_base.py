#!/usr/bin/python3
"""Define Documentation"""
import unittest
from models.base import Base
 

class TestBaseToString(unittest.TestCase):
    """Define class for Test"""
    def test_empty_list(self):
        """Defines test for class TestBaseToString"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_list_with_dictionaries(self):
        """test list with dict"""
        list_dictionaries = [
            


if __name__ == '__main__':
    unittest.main()       
