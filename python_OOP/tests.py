import unittest
from homework import reverselist, isPalindrome, coin, factorial, recur_fibo


class reverselistTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverselist([1, 3, 5]), [5, 3, 1])

    def test2(self):
        return self.assertEqual(reverselist([2, 4, -3]), [-3, 4, 2])


class isPalindromeTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(isPalindrome("racecar"), True)

    def test2(self):
        return self.assertEqual(isPalindrome("rabbit"), False)


class coinTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coin(87), [3, 1, 0, 2])

    def test2(self):
        return self.assertEqual(coin(92), [3, 1, 1, 2])


class factorialTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(factorial(5), 120)

    def test2(self):
        return self.assertEqual(factorial(8), 40320)


class recur_fiboTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(recur_fibo(7), 13)

    def test2(self):
        return self.assertEqual(recur_fibo(6), 8)


if __name__ == "__main__":
    unittest.main()
