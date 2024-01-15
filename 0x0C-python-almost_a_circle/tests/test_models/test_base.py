#!/usr/bin/python3
"""Define Documentation"""
import unittest
from .. .. models.base import Base
 

class TestBaseToString(unittet.TestCase):
    """Define class for Test"""
    def test_to_json_string(list_dictionaries):
        """Defines test for function to_json_string"""
        self.assertIsNotNone(list_dictionaries)




if __name__ == '__main__':
    unittest.main()       
