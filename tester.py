from twenty_forty_eight import Board
import unittest

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.b_full = Board()
        self.b_full.set_board([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        self.b = Board()
        self.b.set_board([[2, 2, 0, 4], [2, 0, 8, 8], [0, 2, 0, 2], [4, 0, 0, 0]])

    def tearDown(self):
        pass

    def test_set_number(self):
        b = Board()
        self.assertTrue(b.set_number(0,0,2))
        self.assertTrue(b.board[0][0] == 2)
        self.assertTrue(b.set_number(1, 3, 7))
        self.assertTrue(b.board[1][3] == 7)
        self.assertFalse(b.set_number(-1,0,1))
        self.assertFalse(b.set_number(5,0,1))
        self.assertFalse(b.set_number(0,-1,1))
        self.assertFalse(b.set_number(0,5,1))
        self.assertFalse(b.set_number(1,1,-1))


    def test_get_board(self):
        b = Board()
        i = 0
        for x in range(b.width):
            for y in range(b.height):
                b.set_number(x,y,i)
                i += 1

        d = b.get_board()
        test_failed = False
        for x in range(b.width):
            for y in range(b.height):
                if d[x][y] != b.board[x][y]:
                    test_failed = True
        self.assertFalse(test_failed)

    def test_is_board_full(self):
        b = Board()
        self.assertFalse(b.is_board_full())
        b.set_number(0,0,2)
        self.assertFalse(b.is_board_full())
        b.update(2)
        self.assertFalse(b.is_board_full())
        for x in range(14):
            b.update(2)
        self.assertTrue(b.is_board_full())

    def test_board_shift_left(self):
        b = Board()
        b.set_number(0, 0, 2)
        b.set_number(0, 1, 0)
        b.set_number(0, 2, 2)
        b.set_number(0, 3, 4)
        b.shift_board_left()
        self.assertTrue(b.board[0] == [4, 4, 0, 0])

    def test_board_shift_right(self):
        b = Board()
        b.set_number(0, 0, 2)
        b.set_number(0, 1, 0)
        b.set_number(0, 2, 2)
        b.set_number(0, 3, 4)
        b.shift_board_right()
        self.assertTrue(b.board[0] == [0, 0, 4, 4])

    def test_board_shift_up(self):
        b = Board()
        b.set_number(0, 0, 2)
        b.set_number(1, 0, 0)
        b.set_number(2, 0, 2)
        b.set_number(3, 0, 4)
        b.shift_board_up()
        self.assertTrue(b.board[0][0] == 4)
        self.assertTrue(b.board[1][0] == 4)
        self.assertTrue(b.board[2][0] == 0)
        self.assertTrue(b.board[3][0] == 0)

    def test_board_shift_down(self):
        b = Board()
        b.set_number(0, 0, 2)
        b.set_number(1, 0, 0)
        b.set_number(2, 0, 2)
        b.set_number(3, 0, 4)
        b.shift_board_down()
        self.assertTrue(b.board[0][0] == 0)
        self.assertTrue(b.board[1][0] == 0)
        self.assertTrue(b.board[2][0] == 4)
        self.assertTrue(b.board[3][0] == 4)
        b.set_number(1, 0, 2)
        b.shift_board_down()
        self.assertTrue(b.board[0][0] == 0)
        self.assertTrue(b.board[1][0] == 0)
        self.assertTrue(b.board[2][0] == 2)
        self.assertTrue(b.board[3][0] == 8)
        b.shift_board_down()
        self.assertTrue(b.board[0][0] == 0)
        self.assertTrue(b.board[1][0] == 0)
        self.assertTrue(b.board[2][0] == 2)
        self.assertTrue(b.board[3][0] == 8)

    def test_is_game_finished(self):
        self.assertTrue(self.b_full.is_game_finished())
        self.b_full.set_number(0, 0, 2)
        self.assertFalse(self.b_full.is_game_finished())



if __name__ == "__main__":
    unittest.main()
