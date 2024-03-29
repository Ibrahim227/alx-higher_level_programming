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
        list_dictionaries = """
                        [
                        {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8},
                        <class 'dict'>,
                        [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}],
                        <class 'str'>
                ]"""
        result = Base.to_json_string([{}])
        expected = '[{}]'
        self.assertEqual(result, expected)

    def test_list_with_empty__dict(self):
        """Test empty list"""
        result = Base.to_json_string([{}])
        expected = '[{}]'
        self.assertEqual(result, expected)

    def test_no_input(self):
        """test no input"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")


class TestSaveToFile(unittest.TestCase):
    """Defines a test class for save_to_file"""
    pass


class TestFromJsonToString(unittest.TestCase):
    """Defines a test class for from_json_to_string"""
    pass


class TestCreate(unittest.TestCase):
    """Defines a test class for Create function"""
    pass


class TestLoadFromFile(unittest.TestCase):
    """Defines a test class for load_from_File"""
    pass


if __name__ == '__main__':
    unittest.main()
