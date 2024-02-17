#!/usr/bin/python3
"""Defines Unittests for Class Base"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_save_to_file(unittest.TestCase):
    """Tests save_to_file method of class Base"""

    @classmethod
    def tearDown(self):
        """Deletes any created files"""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_save_to_file_one_rectangle(self):
        rec = Rectangle(5, 2, 7, 8, 10)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "rec") as x:
            self.assertTrue(len(x.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        rec1 = Rectangle(5, 2, 7, 8, 10)
        rec2 = Rectangle(4, 2, 3, 1, 2)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "rec") as x:
            self.assertTrue(len(x.read()) == 105)

    def test_save_to_file_one_square(self):
        sq = Square(7, 8, 10, 2)
        Square.save_to_file([sq])
        with open("Square.json", "rec") as x:
            self.assertTrue(len(x.read()) == 39)

    def test_save_to_file_two_squares(self):
        sq1 = Square(7, 8, 10, 2)
        sq2 = Square(3, 1, 2, 8)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "rec") as x:
            self.assertTrue(len(x.read()) == 77)

    def test_save_to_file_class_name(self):
        sq = Square(7, 8, 10, 2)
        Base.save_to_file([sq])
        with open("Base.json", "rec") as x:
            self.assertTrue(len(x.read()) == 39)

    def test_save_to_file_overwrite(self):
        sq = Square(39, 2, 9, 2)
        Square.save_to_file([sq])
        sq = Square(7, 8, 10, 2)
        Square.save_to_file([sq])
        with open("Square.json", "rec") as x:
            self.assertTrue(len(x.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "rec") as x:
            self.assertEqual("[]", x.read())

    def test_save_to_file_list_empty(self):
        Square.save_to_file([])
        with open("Square.json", "rec") as x:
            self.assertEqual("[]", x.read())


class TestBase_save_to_file_csv(unittest.TestCase):
    """Tests save_to_file_csv method of class Base"""

    @classmethod
    def tearDown(self):
        """Deletes any created files"""
    try:
        os.remove("Base.csv")
    except IOError:
        pass
    try:
        os.remove("Rectangle.csv")
    except IOError:
        pass
    try:
        os.remove("Square.csv")
    except IOError:
        pass

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_multiple_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    def test_save_to_file_csv_one_rectangle(self):
        rec = Rectangle(5, 2, 7, 8, 10)
        Rectangle.save_to_file_csv([rec])
        with open("Rectangle.csv", "rec") as x:
            self.assertTrue("8,10,7,5,2", x.read())

    def test_save_to_file_csv_two_rectangles(self):
        rec1 = Rectangle(5, 2, 7, 8, 10)
        rec2 = Rectangle(4, 2, 3, 1, 2)
        Rectangle.save_to_file_csv([rec1, rec2])
        with open("Rectangle.csv", "rec") as x:
            self.assertTrue("8,10,7,5,2\n4,2,3,1,2", x.read())

    def test_save_to_file_csv_one_square(self):
        sq = Square(7, 8, 10, 2)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "rec") as x:
            self.assertTrue("10,7,2,8", x.read())

    def test_save_to_file_csv_two_squares(self):
        sq1 = Square(7, 8, 10, 2)
        sq2 = Square(3, 1, 2, 8)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "rec") as x:
            self.assertTrue("10,7,2,8\n2,8,3,1", x.read())

    def test_save_to_file_csv_class_name(self):
        sq = Square(7, 8, 10, 2)
        Base.save_to_file_csv([sq])
        with open("Square.csv", "rec") as x:
            self.assertTrue("10,7,2,8\n2,8,3,1", x.read())

    def test_save_to_file_csv_overwrite(self):
        sq = Square(39, 2, 9, 2)
        Square.save_to_file_csv([sq])
        sq = Square(7, 8, 10, 2)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "rec") as x:
            self.assertTrue("10,7,2,8", x.read())

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "rec") as x:
            self.assertEqual("[]", x.read())

    def test_save_to_file_csv_list_empty(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "rec") as x:
            self.assertEqual("[]", x.read())


class TestBase_instantiation(unittest.TestCase):
    """Tests instantiation of the class Base"""

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_None(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_unique(self):
        self.assertEqual(20, Base(20).id)

    def test_instances_after_unique(self):
        base1 = Base()
        base2 = Base(20)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_public(self):
        base = Base(20)
        base.id = 15
        self.assertEqual(15, base.id)

    def test_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(20).__nb_instances)

    def test_str(self):
        self.assertEqual("Alx", Base("Alx").id)

    def test_float(self):
        self.assertEqual(2.5, Base(2.5).id)

    def test_complex(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict(self):
        self.assertEqual({"a": 2, "b": 3}, Base({"a": 2, "b": 3}).id)

    def test_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple(self):
        self.assertEqual((3, 4), Base((3, 4)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset(self):
        self.assertEqual(frozenset({3, 4, 5}), Base(frozenset({3, 4, 5})).id)

    def test_range(self):
        self.assertEqual(range(3), Base(range(3)).id)

    def test_bytes(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray(self):
        self.assertEqual(bytearray(b'abcdef'), Base(bytearray(b'abcdef')).id)

    def test_memoryview(self):
        self.assertEqual(memoryview(b'abcdef'), Base(memoryview(b'abcdef')).id)

    def test_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)


class TestBase_to_json_string(unittest.TestCase):
    """Testing to_json_string method of class Base"""

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_multiple_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_list_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_rectangle_type(self):
        rec = Rectangle(7, 8, 10, 2, 6)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        rec = Rectangle(7, 8, 10, 2, 6)
        self.assertTrue(len(Base.to_json_string([rec.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        rec1 = Rectangle(5, 19, 2, 3, 2)
        rec2 = Rectangle(1, 4, 2, 12, 4)
        list_dicts = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        sq = Square(4, 3, 10, 2)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        sq = Square(4, 3, 10, 2)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        sq1 = Rectangle(4, 3, 10, 2)
        sq2 = Rectangle(2, 4, 21, 5)
        list_dicts = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)


class TestBase_from_json_string(unittest.TestCase):
    """Testing from_json_string method of class Base"""

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_multiple_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_from_json_string_None(self):
        self.assertEqual("[]", Base.from_json_string(None))

    def test_from_json_string_list_empty(self):
        self.assertEqual("[]", Base.from_json_string("[]"))

    def test_from_json_string_type(self):
        list_input = [{"id": 90, "width": 15, "height": 6}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 90, "width": 15, "height": 6, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 90, "width": 15, "height": 6, "x": 7, "y": 8},
            {"id": 70, "width": 10, "height": 5, "x": 1, "y": 3}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 90, "size": 15, "height": 6}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 90, "size": 15, "height": 6},
            {"id": 8, "size": 2, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)


class TestBase_create(unittest.TestCase):
    """Tests create method of class Base"""

    def test_create_rectangle_original(self):
        rec1 = Rectangle(7, 5, 3, 1, 2)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec1))

    def test_create_rectangle_new(self):
        rec1 = Rectangle(7, 5, 3, 1, 2)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rec2))

    def test_create_rectangle_is(self):
        rec1 = Rectangle(7, 5, 3, 1, 2)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertIsNot(rec1, rec2)

    def test_create_rectangle_equals(self):
        rec1 = Rectangle(7, 5, 3, 1, 2)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertNotEqual(rec1, rec2)

    def test_create_square_original(self):
        sq1 = Square(7, 5, 3, 1)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq1))

    def test_create_square_new(self):
        sq1 = Square(7, 5, 3, 1)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq2))

    def test_create_square_is(self):
        sq1 = Square(7, 5, 3, 1)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertIsNot(sq1, sq2)

    def test_create_square_equals(self):
        sq1 = Square(7, 5, 3, 1)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertNotEqual(sq1, sq2)


class TestBase_load_from_file(unittest.TestCase):
    """Tests load_from_file method of class Base"""

    @classmethod
    def tearDown(self):
        """Deletes any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_several_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_rectangle_one(self):
        rec1 = Rectangle(9, 7, 2, 10, 5)
        rec2 = Rectangle(6, 2, 4, 7, 3)
        Rectangle.save_to_file([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(list_rectangles_output[0]))

    def test_load_from_file_rectangle_two(self):
        rec1 = Rectangle(9, 7, 2, 10, 5)
        rec2 = Rectangle(6, 2, 4, 7, 3)
        Rectangle.save_to_file([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rec2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rec1 = Rectangle(9, 7, 2, 10, 5)
        rec2 = Rectangle(6, 2, 4, 7, 3)
        Rectangle.save_to_file([rec1, rec2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_square_one(self):
        sq1 = Square(6, 1, 8, 5)
        sq2 = Square(7, 3, 4, 9)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_squares_output[0]))

    def test_load_from_file_square_two(self):
        sq1 = Square(6, 1, 8, 5)
        sq2 = Square(7, 3, 4, 9)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        sq1 = Square(6, 1, 8, 5)
        sq2 = Square(7, 3, 4, 9)
        Square.save_to_file([sq1, sq2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))


class TestBase_load_from_file_csv(unittest.TestCase):
    """Tests load_from_file_csv method of class Base"""

    @classmethod
    def tearDown(self):
        """Deletes any created files"""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_several_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_rectangle_one(self):
        rec1 = Rectangle(9, 7, 2, 10, 5)
        rec2 = Rectangle(6, 2, 4, 7, 3)
        Rectangle.save_to_file_csv([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_rectangle_two(self):
        rec1 = Rectangle(9, 7, 2, 10, 5)
        rec2 = Rectangle(6, 2, 4, 7, 3)
        Rectangle.save_to_file_csv([rec1, rec2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rec2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rec1 = Rectangle(9, 7, 2, 10, 5)
        rec2 = Rectangle(6, 2, 4, 7, 3)
        Rectangle.save_to_file_csv([rec1, rec2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_square_one(self):
        sq1 = Square(6, 1, 8, 5)
        sq2 = Square(7, 3, 4, 9)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq1), str(list_squares_output[0]))

    def test_load_from_file_csv_square_two(self):
        sq1 = Square(6, 1, 8, 5)
        sq2 = Square(7, 3, 4, 9)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq1), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        sq1 = Square(6, 1, 8, 5)
        sq2 = Square(7, 3, 4, 9)
        Square.save_to_file_csv([sq1, sq2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))


if __name__ == "__main__":
    unittest.main()
