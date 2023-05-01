#!/usr/bin/env python3

"""test_utils.py"""

from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """test the access_nested_map functionality"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """test the access_nested_map funcion"""
        nested = access_nested_map(map, path)
        self.assertEqual(nested, expected)

    @parameterized.expand([
        ({}, ('a'), 'a'),
        ({"a": 1}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, expected):
        """test that a KeyError was raised"""
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """class for testing utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """test correct output"""
        mock_output = Mock()
        mock_output.json.return_value = test_payload

        with patch('requests.get', return_value=mock_output):
            true_output = get_json(url)
            # test output of get_json is = test_paylod
            self.assertEqual(true_output, test_payload)
            # test method was called exactly once
            mock_output.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """class for testing utils.memoize"""

    def test_memoize(self):
        """test correct output"""
        class TestClass:
            """test class for callable function"""

            def a_method(self):
                """callable function"""
                return 42

            @memoize
            def a_property(self):
                """function that returns the callable function"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:

            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)

            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
