from insert_position import Solution
import unittest

class InsertTest(unittest.TestCase):

    def test_searchInsert(self):
        search = Solution()
        assert search.searchInsert([1,3,5,6], 5) is 2
        assert search.searchInsert([1,3,5,6], 0) is 0
        assert search.searchInsert([1,3,5,6], 7) is 4
        assert search.searchInsert([2,5,7,9,11], 1) is 0
        assert search.searchInsert([2,5,7,9,11], 12) is 5

if __name__ == '__main__':
    unittest.main()
