import unittest
import Sudoku

class TestSudoku(unittest.TestCase):
    # unittest
    def test_1(self):
        a=[[0,2,1,3], [0,0,0,0], [0,0,0,0], [2,1,3,0]]
        last=[[4,2,1,3], [1,3,4,2], [3,4,2,1], [2,1,3,4]]
        self.assertListEqual(Sudoku.solveSudoku2by2(a),last)

    def test_2(self):
        a=[[0,3,1,2], [0,0,0,0], [0,0,0,0], [2,1,3,0]]
        last=[[4,3,1,2], [1,2,4,3], [3,4,2,1], [2,1,3,4]]
        self.assertListEqual(Sudoku.solveSudoku2by2(a),last)

    def test_3(self):
        a=[[2,3,1,4], [1,2,4,0], [3,4,0,2], [0,0,0,1]]
        last='Impossible'
        self.assertEqual(Sudoku.solveSudoku2by2(a),last)
    
if __name__ == '__main__': 
    unittest.main()