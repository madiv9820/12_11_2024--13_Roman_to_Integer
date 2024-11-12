from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ("III", 3), 2: ("LVIII", 58), 3: ("MCMXCIV", 1994)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        s, output = self.__testCases[1]
        result = self.__obj.romanToInt(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        s, output = self.__testCases[2]
        result = self.__obj.romanToInt(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        s, output = self.__testCases[3]
        result = self.__obj.romanToInt(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()