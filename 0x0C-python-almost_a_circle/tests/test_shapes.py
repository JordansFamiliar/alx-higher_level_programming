import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseMethods(unittest.TestCase):
    def test_create_base(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_create_base_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        json_str = Base.to_json_string([{'id': 1, 'name': 'test'}])
        self.assertEqual(json_str, '[{"id": 1, "name": "test"}]')

class TestRectangleMethods(unittest.TestCase):
    def test_create_rectangle(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)


class TestSquareMethods(unittest.TestCase):
    def test_create_square(self):
        s = Square(5)
        self.assertEqual(s.size, 5)


if __name__ == '__main__':
    unittest.main()
