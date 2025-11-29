import unittest
from mspack import msmath
from mspack import msstrings

class TestCase(unittest.TestCase):    #(unittest.Testcase is inharating the TestCase class
    def test_sum(self):
        sum = msmath.sum(8,12)
        self.assertEqual(sum,20)

    def test_subtract(self):
        result = msmath.subtract(109,9)
        self.assertTrue(result == 100)



if __name__ == '__main__':       # whithout this code the class will not run
    unittest.main()