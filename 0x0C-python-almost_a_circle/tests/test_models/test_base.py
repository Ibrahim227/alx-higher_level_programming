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



if __name__ == '__main__':
    unittest.main()       
