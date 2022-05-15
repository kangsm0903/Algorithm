import unittest
import Sudoku

class TestSudoku(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(Sudoku.solveSudoku2by2([[0,2,1,3], [0,0,0,0], [0,0,0,0], [2,1,3,0]]),[[4,2,1,3], [1,3,4,2], [3,4,2,1], [2,1,3,4]])

    def test_2(self):
        self.assertEqual(Sudoku.solveSudoku2by2([[2,3,1,4], [1,2,4,0], [3,4,0,2], [0,0,0,1]]),"Impossible")

    def test_3(self):
        self.assertEqual(Sudoku.solveSudoku2by2([[0,3,1,2], [0,0,0,0], [0,0,0,0], [2,1,3,0]]),[[4,3,1,2], [1,2,4,3], [3,4,2,1], [2,1,3,4]])


if __name__ == '__main__': 
    unittest.main()