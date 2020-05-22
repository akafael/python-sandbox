import unittest


def solution(A):
    """
    Solution
    :type A: object
    """
    return A


class TestSolution(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(5, solution(5))


if __name__ == '__main__':
    unittest.main()
    solution(1)