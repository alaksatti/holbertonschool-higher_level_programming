#!/usr/bin/python3

"""unittest"""

import unittest
from os import path, remove
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """test square"""

    def test_instance(self):
        """test instance"""

        b1 = Base()
        b2 = Base(2)
        b3 = Base(None)
        b4 = Base(2.5)
        b5 = Base("ok")
        b6 = Base(float('inf'))
        b7 = Base([1, 2, 'a', 'b'])

        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 11)
        self.assertEqual(Base._Base__nb_objects, 12)

        self.assertIsInstance(b2, Base)
        self.assertEqual(b2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 12)

        self.assertIsInstance(b3, Base)
        self.assertEqual(b3.id, 12)
        self.assertEqual(Base._Base__nb_objects, 12)

        self.assertIsInstance(b4, Base)
        self.assertEqual(b4.id, 2.5)
        self.assertEqual(Base._Base__nb_objects, 12)

        self.assertIsInstance(b5, Base)
        self.assertEqual(b5.id, 'ok')
        self.assertEqual(Base._Base__nb_objects, 12)

        self.assertIsInstance(b6, Base)
        self.assertNotEqual(b6.id, float('nan'))
        self.assertEqual(Base._Base__nb_objects, 12)

        self.assertIsInstance(b7, Base)
        self.assertEqual(b7.id, [1, 2, 'a', 'b'])
        self.assertEqual(Base._Base__nb_objects, 12)

    def test_to_json_string(self):
        """TEST TO JSON"""
        d1 = []
        d2 = [{'a': 'a'}]
        d3 = [{'a': 1, 'b': 2}]
        d4 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        self.assertEqual(Base.to_json_string(d1), '[]')
        self.assertEqual(Base.to_json_string(d2), '[{"a": "a"}]')

        d1 = None
        d2 = [[1, 2]]
        d3 = "Not a dictionary"
        d4 = 666
        self.assertEqual(Base.to_json_string(d1), '[]')
        self.assertEqual(Base.to_json_string(d2), '[[1, 2]]')
        self.assertEqual(Base.to_json_string(d3), '"Not a dictionary"')
        with self.assertRaises(TypeError):
            Base.to_json_string(d4)

    def test_from_json_string(self):
        """Test From Json String"""
        d1 = []
        d2 = [{'a': 'a'}]
        d3 = [{'a': 1, 'b': 2}]
        d4 = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        s1 = Base.to_json_string(d1)
        s2 = Base.to_json_string(d2)
        s3 = Base.to_json_string(d3)
        s4 = Base.to_json_string(d4)
        self.assertEqual(Base.from_json_string(s1), d1)
        self.assertEqual(Base.from_json_string(s2), d2)
        self.assertEqual(Base.from_json_string(s3), d3)
        self.assertEqual(Base.from_json_string(s4), d4)
        d1 = None
        d2 = [[1, 2]]
        d3 = "Not a dictionary"
        s1 = Base.to_json_string(d1)
        s2 = Base.to_json_string(d2)
        s3 = Base.to_json_string(d3)
        self.assertEqual(Base.from_json_string(s1), [])
        self.assertEqual(Base.from_json_string(s2), d2)
        self.assertEqual(Base.from_json_string(s3), d3)

    def test_create(self):
        """Test Create"""
        r1d = {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r2 = Rectangle.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())
        s1d = {'id': 1, 'size': 1, 'x': 2, 'y': 3}
        s2 = Square.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())
        r1 = Rectangle(1, 2)
        r1d = r1.to_dictionary()
        r2 = Rectangle.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())
        r1 = Rectangle(1, 2, 3, 4)
        r1d = r1.to_dictionary()
        r2 = Rectangle.create(**r1d)
        self.assertDictEqual(r1d, r2.to_dictionary())
        s1 = Square(1)
        s1d = s1.to_dictionary()
        s2 = Square.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())
        s1 = Square(1, 2, 3)
        s1d = s1.to_dictionary()
        s2 = Square.create(**s1d)
        self.assertDictEqual(s1d, s2.to_dictionary())

    def test_save_to_file(self):
        """Test Save To File"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        s1 = Square(6, 5, 3)
        s2 = Square(9)
        Square.save_to_file([s1, s2])
        self.assertTrue(path.isfile('Rectangle.json'))
        self.assertTrue(path.isfile('Square.json'))

    def test_load_from_file(self):
        """Test Load From File"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = Square(6, 5, 3)
        s2 = Square(9)
        rlist = Rectangle.load_from_file()
        slist = Square.load_from_file()
        self.assertIsInstance(rlist[0], Rectangle)
        self.assertIsInstance(rlist[1], Rectangle)
        self.assertIsInstance(slist[0], Square)
        self.assertIsInstance(slist[1], Square)

if __name__ == '__main__':
    unittest.main()
