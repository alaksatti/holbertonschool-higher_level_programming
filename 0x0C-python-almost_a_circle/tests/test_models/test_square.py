#!/usr/bin/python3

"""unittest"""

import unittest
import sys
import os
import io
import contextlib
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """test square"""

    def test_instance(self):
        """test instance"""
        s_1 = Square(1, 2, 3, 4)

        self.assertIsInstance(s_1, Square)
        self.assertIsInstance(s_1, Square)
        self.assertIsInstance(s_1, Base)

    def test_args_0_1(self):
        """test args"""
        with self.assertRaises(TypeError) as x:
            s_0 = Square()

        txt = "__init__() missing 1 required positional argument: 'size'"

        self.assertEqual(txt, str(x.exception))

    def test_args_1(self):
        """test args"""
        s_2 = Square(1)

        self.assertIsInstance(s_2, Square)
        self.assertEqual(s_2.id, 39)
        self.assertEqual(s_2.size, 1)
        self.assertEqual(s_2.width, 1)
        self.assertEqual(s_2.height, 1)
        self.assertEqual(s_2.x, 0)
        self.assertEqual(s_2.y, 0)

    def test_args_2(self):
        """test args"""
        s_22 = Square(1, 2)

        self.assertIsInstance(s_22, Square)
        self.assertEqual(s_22.id, 40)
        self.assertEqual(s_22.size, 1)
        self.assertEqual(s_22.width, 1)
        self.assertEqual(s_22.height, 1)
        self.assertEqual(s_22.x, 2)
        self.assertEqual(s_22.y, 0)

    def test_args_3(self):
        """test args"""
        s_3 = Square(1, 2, 3)

        self.assertIsInstance(s_3, Square)
        self.assertEqual(s_3.id, 41)
        self.assertEqual(s_3.width, 1)
        self.assertEqual(s_3.height, 1)
        self.assertEqual(s_3.x, 2)
        self.assertEqual(s_3.y, 3)

    def test_args_4(self):
        """test args"""
        s_4 = Square(1, 2, 3, 55)

        self.assertIsInstance(s_4, Square)
        self.assertEqual(s_4.id, 55)
        self.assertEqual(s_4.size, 1)
        self.assertEqual(s_4.width, 1)
        self.assertEqual(s_4.height, 1)
        self.assertEqual(s_4.x, 2)
        self.assertEqual(s_4.y, 3)

    def test_exceptions_int_width(self):
        """test exceptions"""
        with self.assertRaises(TypeError) as x:
            r_6 = Square("A", 1, 2, 3)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(True, 1, 2, 3)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(float('inf'), 1, 2, 3)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(3.5, 1, 2, 3)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square({}, 1, 2, 3)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square([], 1, 2, 3)
        self.assertEqual('width must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square((), 1, 2, 3)
        self.assertEqual('width must be an integer', str(x.exception))

    def test_exceptions_value_size(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Square(0, 1, 2, 3)
        self.assertEqual('width must be > 0', str(x.exception))

        with self.assertRaises(ValueError) as x:
            r_6 = Square(-5, 1, 2, 3)
        self.assertEqual('width must be > 0', str(x.exception))

    def test_exceptions_value_x(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Square(1, -5, 4, 6)
            self.assertEqual('x must be >= 0', str(x.exception))

    def test_exceptions_value_y(self):
        """test exceptions"""
        with self.assertRaises(ValueError) as x:
            r_6 = Square(1, 5, -5, 6)
        self.assertEqual('y must be >= 0', str(x.exception))

    def test_exceptions_int_x(self):
        """test exceptions"""
        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, "A", 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, True, 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, float('inf'), 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, 3.5, 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, {}, 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, [], 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, (), 3, 4)
        self.assertEqual('x must be an integer', str(x.exception))

    def test_exceptions_int_y(self):
        """test exceptions"""
        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, 2, "A", 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, 2, True, 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, 2, float('inf'), 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, 2, 3.5, 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, 2, {}, 4)
        self.assertEqual('y must be an integer', str(x.exception))

        with self.assertRaises(TypeError) as x:
            r_6 = Square(1, 2, [],  4)
        self.assertEqual('y must be an integer', str(x.exception))

    def test_area(self):
        """test area"""
        r_7 = Square(10, 2, 0, 0)
        self.assertEqual(r_7.area(), 10 ** 2)
        r_8 = Square(5)
        self.assertEqual(r_8.area(), 5 ** 2)

    def test_str(self):
        """test string"""
        r_8 = Square(1, 2, 3, 1)
        self.assertEqual(r_8.__str__(), '[Square] (1) 2/3 - 1')

        r_9 = Square(9, 1, 2)
        self.assertEqual(r_9.__str__(), '[Square] (44) 1/2 - 9')

        r_10 = Square(4, 5)
        self.assertEqual(r_10.__str__(), '[Square] (45) 5/0 - 4')

        r_11 = Square(3)
        self.assertEqual(r_11.__str__(), '[Square] (46) 0/0 - 3')

    def test_update(self):
        """test update"""
        r_12 = Square(2, 2, 3, 4)
        self.assertEqual(r_12.__str__(), '[Square] (4) 2/3 - 2')

        r_12.update(size=2)
        self.assertEqual(r_12.__str__(), '[Square] (4) 2/3 - 2')

        r_12.update(x=1)
        self.assertEqual(r_12.__str__(), '[Square] (4) 1/3 - 2')

        r_12.update(y=1)
        self.assertEqual(r_12.__str__(), '[Square] (4) 1/1 - 2')

        r_12.update(id=1)
        self.assertEqual(r_12.__str__(), '[Square] (1) 1/1 - 2')

        r_12.update(banana=1)
        self.assertEqual(r_12.__str__(), '[Square] (1) 1/1 - 2')

        r_12.update()
        self.assertEqual(r_12.__str__(), '[Square] (1) 1/1 - 2')

        r_12.update(3)
        self.assertEqual(r_12.__str__(), '[Square] (3) 1/1 - 2')

        r_12.update(3, 4)
        self.assertEqual(r_12.__str__(), '[Square] (3) 1/1 - 4')

        r_12.update(3, 4, 5)
        self.assertEqual(r_12.__str__(), '[Square] (3) 5/1 - 4')

        r_12.update(3, 4, 5, 6)
        self.assertEqual(r_12.__str__(), '[Square] (3) 5/6 - 4')

    def test_to_dictionary(self):
        """test dictionary"""
        r_13 = Square(2, 2, 3, 4)
        r_13_dictionary = r_13.to_dictionary()
        true_dictionary = {'size': 2, 'id': 4, 'x': 2, 'y': 3}

        self.assertIsInstance(r_13_dictionary, dict)
        self.assertEqual(r_13_dictionary, true_dictionary)

        r_14 = Square(2)
        r_14_dictionary = r_14.to_dictionary()
        true_dictionary = {'size': 2, 'id': 47, 'x': 0, 'y': 0}

        self.assertIsInstance(r_14_dictionary, dict)
        self.assertEqual(r_14_dictionary, true_dictionary)

        r_15 = Square(2, 2)
        r_15_dictionary = r_15.to_dictionary()
        true_dictionary = {'size': 2, 'x': 2, 'y': 0, 'id': 48}

        self.assertIsInstance(r_15_dictionary, dict)
        self.assertEqual(r_15_dictionary, true_dictionary)

        r_16 = Square(2, 2, 3)
        r_16_dictionary = r_16.to_dictionary()
        true_dictionary = {'size': 2, 'id': 49, 'x': 2, 'y': 3}
        self.assertIsInstance(r_16_dictionary, dict)
        self.assertEqual(r_16_dictionary, true_dictionary)

    def test_display(self):
        """test display"""
        rectangle = Square(2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            rectangle.display()
        x = f.getvalue()

        final = "##\n##\n"

        self.assertEqual(x, final)

        rectangle = Square(3, 2, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            rectangle.display()
        x = f.getvalue()

        final = "  ###\n  ###\n  ###\n"

        self.assertEqual(x, final)

        rectangle = Square(1, 2, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            rectangle.display()
        x = f.getvalue()

        final = "\n  #\n"

        self.assertEqual(x, final)

    def test_none(self):
        """test none"""
        with self.assertRaises(TypeError) as x:
            r_0 = Square(None)
        txt = "__init__() missing 1 required positional arguments: 'size'"
        self.assertEqual("width must be an integer", str(x.exception))

if __name__ == '__main__':
    unittest.main()
