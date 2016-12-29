import unittest
import TESTMODULE
class TestStringMethods(unittest.TestCase):
    
    def test_func(self):
        s1 = 1992
        s2 = 1979
        s3 = "ololo"
        self.assertEqual(is_year_leap(s1), "Год является високосным")
        self.assertEqual(is_year_leap(s2), "Год не является високосным")
        with self.assertRaises(TypeError):
              is_year_leap(s3)

if __name__ == "__main__":
    unittest.main()
