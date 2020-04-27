from rotated_sorted_array import Solution
import unittest

class InsertTest(unittest.TestCase):

    def test_search(self):
        searched = Solution()
        assert searched.search([8, 9, 11, 14, 0, 1, 2, 5, 7], 1) == 5
        assert searched.search([8, 9, 11, 14, 0, 1, 2, 5, 7], 7) == 8
        assert searched.search([8, 9, 11, 14, 0, 1, 2, 5, 7], 8) == 0
        assert searched.search([8, 9, 11, 14, 0, 1, 2, 5, 7], 15) == -1
        assert searched.search([1, 3, 6, 7, 9, 11, 0], 0) == 6
        assert searched.search([1, 3, 6, 7, 9, 11, 0], 6) == 2
        assert searched.search([1, 3, 6, 7, 9, 11, 0], 5) == -1


if __name__ == '__main__':
    unittest.main()
