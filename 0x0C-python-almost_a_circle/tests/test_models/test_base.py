#!/usr/bin/python3
"""Define Documentation"""
import unittest


class TestBase(unittet.TestCase):
    """Define class for Test"""
    def test_to_json_string(list_dictionaries):
        """Defines test for function to_json_string"""
        self.assertIsNotNone(if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, sort_keys=True))





if __name__ == '__main__':
    unittest.main()       
