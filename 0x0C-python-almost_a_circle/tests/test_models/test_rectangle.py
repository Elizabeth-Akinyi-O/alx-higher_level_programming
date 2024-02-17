#!/usr/bin/python3
"""Defines Unittests for Class Rectangle"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Tests instantiation of the class Rectangle"""

    def test_rectangle_isbase(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_equalto_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_equalto_two_args(self):
        rec1 = Rectangle(20, 4)
        rec2 = Rectangle(4, 20)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_equalto_three_args(self):
        rec1 = Rectangle(20, 4, 2)
        rec2 = Rectangle(2, 20, 4)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_equalto_four_args(self):
        rec1 = Rectangle(20, 4, 2, 8)
        rec2 = Rectangle(8, 2, 20, 4)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_equalto_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_greater_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(15, 3, 6, 9, 2, 7, 8)

    def test_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(15, 3, 6, 9, 2, 7, 8).__width)

    def test_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(15, 3, 6, 9, 2, 7, 8).__height)

    def test_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(15, 3, 6, 9, 2, 7, 8).__x)

    def test_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(15, 3, 6, 9, 2, 7, 8).__y)

    def test_width_getter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        self.assertEqual(5, rec.width)

    def test_width_setter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_height_getter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        self.assertEqual(7, rec.height)

    def test_height_setter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_x_getter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        self.assertEqual(7, rec.x)

    def test_x_setter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_y_getter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        rec = Rectangle(7, 5, 1, 5, 7)
        rec.y = 10
        self.assertEqual(10, rec.y)


class TestRectangle_width(unittest.TestCase):
    """Tests Rectangle width initialization"""

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("noninteger", 4)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(9.2, 1)

    def test_width_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 2, "b": 3}, 3)

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 4, 6], 4)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2, 4, 6}, 4)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 4, 6), 4)

    def test_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({2, 5, 8, 2, 1}), 4)

    def test_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_width_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 4)

    def test_width_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefgh'), 4)

    def test_width_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcdefgh'), 4)

    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 4)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 4)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)


class TestRectangle_height(unittest.TestCase):
    """Tests Rectangle height initialization"""

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, "noninteger")

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 11.5)

    def test_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, complex(7))

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {"a": 2, "b": 3})

    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, [2, 4, 6])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {2, 4, 6})

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (2, 4, 6))

    def test_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, frozenset({2, 5, 8, 2, 1}))

    def test_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(5))

    def test_height_bytes(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, b'Python')

    def test_height_bytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, bytearray(b'abcdefgh'))

    def test_height_memoryview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, memoryview(b'abcdefgh'))

    def test_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'))

    def test_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('nan'))

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -9)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, 0)


class TestRectangle_x(unittest.TestCase):
    """Tests Rectangle x attribute  initialization"""

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, None)

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "noninteger", 2)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, 11.5, 7)

    def test_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, complex(7))

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {"a": 2, "b": 3}, 2)

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 10, True, 2)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 7, [2, 4, 6], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {2, 4, 6}, 2)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, (2, 4, 6), 2)

    def test_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, frozenset({2, 5, 8, 2, 1}))

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, range(5))

    def test_x_bytes(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, b'Python')

    def test_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 2, bytearray(b'abcdefgh'))

    def test_x_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, memoryview(b'abcdefgh'))

    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('inf'), 2)

    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 4, float('nan'), 2)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(4, 6, -9, 0)


class TestRectangle_y(unittest.TestCase):
    """Tests Rectangle y attribute  initialization"""

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 4, None)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 3, "noninteger")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 7, 11.5)

    def test_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 9, complex(7))

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 8, {"a": 2, "b": 3})

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 10, 4, True)

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 7, 9, [2, 4, 6])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 2, {2, 4, 6})

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 7, (2, 4, 6))

    def test_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 1, frozenset({2, 5, 8, 2, 1}))

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 2, range(5))

    def test_y_bytes(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 2, b'Python')

    def test_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 4, bytearray(b'abcdefgh'))

    def test_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 2, memoryview(b'abcdefgh'))

    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 4, float('inf'))

    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 4, float('nan'))

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 6, 0, -9)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Tests Rectangle order of initialization"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("not width", "not height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("not width", 4, "not x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("not width", 4, 2, "not y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "not height", "not x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "not height", 5, "not y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "not x", "not y")


class TestRectangle_area(unittest.TestCase):
    """Tests the area method of class Rectangle"""

    def test_area_small(self):
        rec = Rectangle(0, 5, 0, 10, 0)
        self.assertEqual(50, rec.area())

    def test_area_large(self):
        rec = Rectangle(999999999999999999, 999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, rec.area())

    def test_area_changed_attributes(self):
        rec = Rectangle(1, 5, 1, 10, 1)
        rec.width = 8
        rec.height = 12
        self.assertEqual(96, rec.area())

    def test_area_one_arg(self):
        rec = Rectangle(1, 5, 1, 10, 1)
        with self.assertRaises(TypeError):
            rec.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Tests __str__ and display methods of class Rectangle"""

    @staticmethod
    def capture_stdout(rec, method):
        """Returns text printed to the stdout

        Args:
            rec (Rectangle): To be printed
            method (str): Method to run on rectangle

        Returns:
            Text printed to stdout
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        rec = Rectangle(2, 4)
        capture = TestRectangle_stdout.capture_stdout(rec, "print")
        correct = "[Rectangle] ({}) 0/0 - 2/4\n".format(rec.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        rec = Rectangle(1, 5, 5)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(rec.id)
        self.assertEqual(correct, rec.__str__())

    def test_str_method_width_height_x_y(self):
        rec = Rectangle(1, 6, 4, 8)
        correct = "[Rectangle] ({}) 4/8 - 1/6".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_str_method_width_height_x_y_id(self):
        rec = Rectangle(11, 19, 2, 4, 5)
        self.assertEqual("[Rectangle] (5) 2/4 - 11/19", str(rec))

    def test_str_method_changed_attributes(self):
        rec = Rectangle(5, 5, 0, 0, [4])
        rec.width = 13
        rec.height = 1
        rec.x = 6
        rec.y = 8
        self.assertEqual("[Rectangle] ([4]) 6/8 - 13/1", str(rec))

    def test_str_method_one_arg(self):
        rec = Rectangle(1, 2, 6, 4, 8)
        with self.assertRaises(TypeError):
            rec.__str__(1)

    def test_display_one_arg(self):
        rec = Rectangle(1, 2, 6, 4, 8)
        with self.assertRaises(TypeError):
            rec.display(1)

    def test_display_width_height(self):
        rec = Rectangle(4, 5, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        rec = Rectangle(5, 4, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        rec = Rectangle(2, 3, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        rec = Rectangle(2, 5, 3, 4, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        display = "\n\n  ##\n   ##\n  ##\n  ##\n"
        self.assertEqual(display, capture.getvalue())


class TestRectangle_update_args(unittest.TestCase):
    """Tests the update args method of class Rectangle"""

    def test_update_args_zero(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update()
        self.assertEqual("[Rectangle] (20) 20/20 - 20/20", str(rec))

    def test_update_args_one(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78)
        self.assertEqual("[Rectangle] (78) 20/20 - 20/20", str(rec))

    def test_update_args_two(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78, 2)
        self.assertEqual("[Rectangle] (78) 20/20 - 2/20", str(rec))

    def test_update_args_three(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78, 2, 3)
        self.assertEqual("[Rectangle] (78) 20/20 - 2/3", str(rec))

    def test_update_args_four(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78, 2, 3, 4)
        self.assertEqual("[Rectangle] (78) 4/20 - 2/3", str(rec))

    def test_update_args_five(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (78) 4/5 - 2/3", str(rec))

    def test_update_args_more_than_five(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (78) 4/5 - 2/3", str(rec))

    def test_update_args_None(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(None)
        correct = "[Rectangle] ({}) 20/20 - 20/20".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_args_None_and_more(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/20 - 4/5".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_args_twice(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78, 2, 3, 4, 5, 6)
        rec.update(6, 5, 4, 3, 2, 78)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rec))

    def test_update_args_invalid_width_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(78, "invalid")

    def test_update_args_width_zero(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(78, 0)

    def test_update_args_width_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(78, -9)

    def test_update_args_invalid_height_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(78, 2, "invalid")

    def test_update_args_height_zero(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(78, 1, 0)

    def test_update_args_height_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(78, 1, -9)

    def test_update_args_invalid_x_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(78, 2, 3, "invalid")

    def test_update_args_x_zero(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(78, 1, 2, 0)

    def test_update_args_x_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(78, 1, 2, -9)

    def test_update_args_invalid_y_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(78, 2, 3, 4,  "invalid")

    def test_update_args_y_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(78, 1, 2, 3, -9)

    def test_update_args_width_before_height(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(78, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(78, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(78, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(78, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(78, 1, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(78, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Tests the update kwargs method of class Rectangle"""

    def test_update_kwargs_one(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(id=1)
        self.assertEqual("[Rectangle] (1) 20/20 - 20/20", str(rec))

    def test_update_kwargs_two(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 20/20 - 2/20", str(rec))

    def test_update_kwargs_three(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(id=78, width=2, height=3)
        self.assertEqual("[Rectangle] (78) 20/20 - 2/3", str(rec))

    def test_update_kwargs_four(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(id=78, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (78) 1/3 - 4/2", str(rec))

    def test_update_kwargs_five(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(id=85, x=8, height=2, y=5, width=1)
        self.assertEqual("[Rectangle] (85) 8/5 - 1/2", str(rec))

    def test_update_kwargs_None(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(id=None)
        correct = "[Rectangle] ({}) 20/20 - 20/20".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_kwargs_None_and_more(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(id=None, height=8, y=9)
        correct = "[Rectangle] ({}) 20/9 - 20/8".format(rec.id)
        self.assertEqual(correct, str(rec))

    def test_update_kwargs_twice(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(id=78, x=2, height=2)
        rec.update(y=4, height=12, width=2)
        self.assertEqual("[Rectangle] (78) 2/4 - 2/12", str(rec))

    def test_update_kwargs_invalid_width_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=0)

    def test_update_kwargs_width_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=-9)

    def test_update_kwargs_invalid_height_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=0)

    def test_update_kwargs_height_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height-8)

    def test_update_kwargs_invalid_x_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(x="invalid")

    def test_update_kwargs_x_zero(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(x=0)

    def test_update_kwargs_x_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(x=-9)

    def test_update_kwargs_invalid_y_type(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(y=-7)

    def test_update_args_and_kwargs(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(78, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (78) 20/20 - 2/20", str(rec))

    def test_update_kwargs_wrong_keys(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(a=4, b=10)
        self.assertEqual("[Rectangle] (10) 20/20 - 20/20", str(rec))

    def test_update_kwargs_some_wrong_keys(self):
        rec = Rectangle(20, 20, 20, 20, 20)
        rec.update(height=4, id=79, a=1, b=65, x=19, y=7)
        self.assertEqual("[Rectangle] (79) 19/7 - 20/4", str(rec))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests to_dictionary method of class Rectangle"""

    def test_to_dictionary_output(self):
        rec = Rectangle(20, 2, 5, 7, 1)
        correct = {'x': 1, 'y': 7, 'id': 5, 'height': 2, 'width': 20}
        self.assertDictEqual(correct, rec.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rec1 = Rectangle(20, 2, 5, 7, 4)
        rec2 = Rectangle(6, 7, 2, 10, 5)
        rec2.update(**rec1.to_dictionary())
        self.assertNotEqual(rec1, rec2)

    def test_to_dictionary_arg(self):
        rec = Rectangle(20, 2, 5, 7, 4)
        with self.assertRaises(TypeError):
            rec.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
