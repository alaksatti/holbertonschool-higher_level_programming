#!/usr/bin/python3
"""Test module"""


import unittest
import sys
import os
import io
import contextlib
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests the Base"""
    def test_instance(self):
        """test instance"""
        r_1 = Rectangle(1, 2, 3, 4)

        self.assertIsInstance(r_1, Rectangle)
        self.assertIsInstance(r_1, Base)

    def test_args_0_1(self):
        """test args"""
        with self.assertRaises(TypeError) as x:
            r_0 = Rectangle()
        txt = "__init__() missing 2 required positional arguments: 'width'"
        txt2 = " and 'height'"
        self.assertEqual(txt + txt2, str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_1 = Rectangle(1)
        txt3 = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(txt3, str(x.exception))

    def test_args_2(self):
        """test args"""
        r_2 = Rectangle(1, 2)

        self.assertIsInstance(r_2, Rectangle)
        self.assertEqual(r_2.id, 25)
        self.assertEqual(r_2.width, 1)
        self.assertEqual(r_2.height, 2)
        self.assertEqual(r_2.x, 0)
        self.assertEqual(r_2.y, 0)

    def test_args_3(self):
        """test args"""
        r_3 = Rectangle(1, 2, 3)

        self.assertIsInstance(r_3, Rectangle)
        self.assertEqual(r_3.id, 26)
        self.assertEqual(r_3.width, 1)
        self.assertEqual(r_3.height, 2)
        self.assertEqual(r_3.x, 3)
        self.assertEqual(r_3.y, 0)

    def test_args_4(self):
        """test args"""
        r_4 = Rectangle(1, 2, 3, 4)

        self.assertIsInstance(r_4, Rectangle)
        self.assertEqual(r_4.id, 27)
        self.assertEqual(r_4.width, 1)
        self.assertEqual(r_4.height, 2)
        self.assertEqual(r_4.x, 3)
        self.assertEqual(r_4.y, 4)

    def test_args_5(self):
        """test args"""
        r_5 = Rectangle(1, 2, 3, 4, 5)

        self.assertIsInstance(r_5, Rectangle)
        self.assertEqual(r_5.id, 5)
        self.assertEqual(r_5.width, 1)
        self.assertEqual(r_5.height, 2)
        self.assertEqual(r_5.x, 3)
        self.assertEqual(r_5.y, 4)

    def test_exceptions_int_width(self):
        """test exceptions"""
        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle("A", 1, 2, 3, 4)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(True, 1, 2, 3, 4)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(float('inf'), 1, 2, 3, 4)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(3.5, 1, 2, 3, 4)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle({}, 1, 2, 3, 4)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle([], 1, 2, 3, 4)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle((), 1, 2, 3, 4)
        self.assertEqual('width must be an integer', str(x.exception))

    def test_exceptions_value_width(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(0, 1, 2, 3, 4)
        self.assertEqual('width must be > 0', str(x.exception))

        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(-5, 1, 2, 3, 4)
        self.assertEqual('width must be > 0', str(x.exception))

    def test_exceptions_value_height(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(0, 1, 2, 3, 4)
        self.assertEqual('height must be > 0', str(x.exception))

        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(-5, 1, 2, 3, 4)
        self.assertEqual('height must be > 0', str(x.exception))

    def test_exceptions_value_height(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(1, 0, 2, 3, 4)
        self.assertEqual('height must be > 0', str(x.exception))

        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(1, -5, 2, 3, 4)
        self.assertEqual('height must be > 0', str(x.exception))

    def test_exceptions_value_x(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(1, 3, 3, -5, 4)
            self.assertEqual('y must be >= 0', str(x.exception))

    def test_exceptions_value_y(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Rectangle(1, 2, -5, 3, 4)
        self.assertEqual('x must be >= 0', str(x.exception))

    def test_exceptions_int_height(self):
        """test exceptions"""
        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, "A", 2, 3, 4)
        self.assertEqual('height must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, True, 2, 3, 4)
        self.assertEqual('height must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, float('inf'), 2, 3, 4)
        self.assertEqual('height must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 3.5, 2, 3, 4)
        self.assertEqual('height must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, {}, 2, 3, 4)
        self.assertEqual('height must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, [], 2, 3, 4)
        self.assertEqual('height must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, (), 2, 3, 4)
        self.assertEqual('height must be an integer', str(x.exception))

    def test_exceptions_int_x(self):
        """test exceptions"""
        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, "A",  3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, True, 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, float('inf'), 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, 3.5, 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, {}, 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, [], 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, (), 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

    def test_exceptions_int_y(self):
        """test exceptions"""
        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, 3, "A", 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, 3, True, 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, 3, float('inf'), 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, 3, 3.5, 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, 3, {}, 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Rectangle(1, 2, 3, [],  4)
        self.assertEqual('y must be an integer', str(x.exception))

    def test_area(self):
        """test area"""
        r_7 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(r_7.area(), 20)

    def test_str(self):
        """test string"""
        r_8 = Rectangle(1, 2, 3, 4, 8)
        self.assertEqual(r_8.__str__(), '[Rectangle] (8) 3/4 - 1/2')

        r_9 = Rectangle(9, 1, 2, 3)
        self.assertEqual(r_9.__str__(), '[Rectangle] (32) 2/3 - 9/1')

        r_10 = Rectangle(4, 5, 1)
        self.assertEqual(r_10.__str__(), '[Rectangle] (33) 1/0 - 4/5')

        r_11 = Rectangle(3, 4)
        self.assertEqual(r_11.__str__(), '[Rectangle] (34) 0/0 - 3/4')

    def test_update(self):
        """test update"""
        r_12 = Rectangle(2, 2, 3, 4, 8)
        self.assertEqual(r_12.__str__(), '[Rectangle] (8) 3/4 - 2/2')

        r_12.update(width=1)
        self.assertEqual(r_12.__str__(), '[Rectangle] (8) 3/4 - 1/2')

        r_12.update(height=1)
        self.assertEqual(r_12.__str__(), '[Rectangle] (8) 3/4 - 1/1')

        r_12.update(x=1)
        self.assertEqual(r_12.__str__(), '[Rectangle] (8) 1/4 - 1/1')

        r_12.update(y=1)
        self.assertEqual(r_12.__str__(), '[Rectangle] (8) 1/1 - 1/1')

        r_12.update(id=1)
        self.assertEqual(r_12.__str__(), '[Rectangle] (1) 1/1 - 1/1')

        r_12.update(banana=1)
        self.assertEqual(r_12.__str__(), '[Rectangle] (1) 1/1 - 1/1')

        r_12.update()
        self.assertEqual(r_12.__str__(), '[Rectangle] (1) 1/1 - 1/1')

        r_12.update(2)
        self.assertEqual(r_12.__str__(), '[Rectangle] (2) 1/1 - 1/1')

        r_12.update(2, 2)
        self.assertEqual(r_12.__str__(), '[Rectangle] (2) 1/1 - 2/1')

        r_12.update(2, 2, 2)
        self.assertEqual(r_12.__str__(), '[Rectangle] (2) 1/1 - 2/2')

        r_12.update(2, 2, 2, 2)
        self.assertEqual(r_12.__str__(), '[Rectangle] (2) 2/1 - 2/2')

        r_12.update(2, 2, 2, 2, 2)
        self.assertEqual(r_12.__str__(), '[Rectangle] (2) 2/2 - 2/2')

    def test_to_dictionary(self):
        """test dictionary"""
        r_13 = Rectangle(2, 2, 3, 4, 8)
        r_13_dictionary = r_13.to_dictionary()
        true_dictionary = {'width': 2, 'height': 2, 'id': 8, 'x': 3, 'y': 4}

        self.assertIsInstance(r_13_dictionary, dict)
        self.assertEqual(r_13_dictionary, true_dictionary)

        r_14 = Rectangle(2, 2)
        r_14_dictionary = r_14.to_dictionary()
        true_dictionary = {'width': 2, 'height': 2, 'id': 35, 'x': 0, 'y': 0}

        self.assertIsInstance(r_14_dictionary, dict)
        self.assertEqual(r_14_dictionary, true_dictionary)

        r_15 = Rectangle(2, 2, 3)
        r_15_dictionary = r_15.to_dictionary()
        true_dictionary = {'width': 2, 'height': 2, 'x': 3, 'y': 0, 'id': 36}

        self.assertIsInstance(r_15_dictionary, dict)
        self.assertEqual(r_15_dictionary, true_dictionary)

        r_16 = Rectangle(2, 2, 3, 4)
        r_16_dictionary = r_16.to_dictionary()
        true_dictionary = {'width': 2, 'height': 2, 'id': 37, 'x': 3, 'y': 4}
        self.assertIsInstance(r_16_dictionary, dict)
        self.assertEqual(r_16_dictionary, true_dictionary)

    def test_none(self):
        """test none"""
        with self.assertRaises(TypeError) as x:
            r_0 = Rectangle(None)
        txt4 = "__init__() missing 1 required positional argument: 'height'"
        txt5 = " and 'height'"
        self.assertEqual((txt4), str(x.exception))

    def test_display(self):
        """test display"""
        rectangle = Rectangle(3, 2, 3, 3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            rectangle.display()
        x = f.getvalue()

        final = "\n\n\n   ###\n   ###\n"

        self.assertEqual(x, final)

        rectangle = Rectangle(3, 2, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            rectangle.display()
        x = f.getvalue()

        final = "###\n###\n"

        self.assertEqual(x, final)

        rectangle = Rectangle(1, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            rectangle.display()
        x = f.getvalue()

        final = "#\n#\n"

        self.assertEqual(x, final)

if __name__ == '__main__':
    unittest.main()
