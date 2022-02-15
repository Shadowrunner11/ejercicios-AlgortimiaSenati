import unittest

from romanizer2 import romanize

class Romanizer_test(unittest.TestCase):
    def test1 (self):
        self.assertEqual(romanize(5), "V")
    def test2 (self):
        self.assertEqual(romanize(2), "II")
    def test3 (self):
        self.assertEqual(romanize(14), "XIV")
    def test4 (self):
        self.assertEqual(romanize(4), "IV")
    def test5 (self):
        self.assertEqual(romanize(16), "XVI")
    def test6 (self):
        self.assertEqual(romanize(28), "XXVIII")
    def test7 (self):
        self.assertEqual(romanize(156), "CLVI")
    def test8 (self):
        self.assertEqual(romanize(532), "DXXXII")
    def test9 (self):
        self.assertEqual(romanize(1235), "MCCXXXV")

if __name__=="__main__":
    unittest.main()