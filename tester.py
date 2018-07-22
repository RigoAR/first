from twenty_forty_eight import Board
import unittest

class TestBoard(unittest.TestCase):
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



if __name__ == "__main__":
    unittest.main()

    bb = Board()
    bb.print_stdout()
    bb.update(2)
    bb.print_stdout()
    bb.update(2)
    bb.print_stdout()
    bb.update(4)
    bb.print_stdout()
    bb.update(2)
    bb.update(4)
    bb.update(2)
    bb.update(2)
    bb.update(4)
    bb.update(2)
    bb.update(2)
    bb.update(4)
    bb.update(2)
    bb.update(2)
    bb.update(4)
    bb.update(2)
    bb.update(2)
    bb.update(4)
    bb.update(2)
    bb.print_stdout()


    # test 3
    bb.set_number(0,0,2)
    bb.set_number(0,1,0)
    bb.set_number(0,2,2)
    bb.set_number(0,3,4)
    bb.shift_board_left()
    if bb.board[0] == [4, 4, 0, 0]:
        print("test 3 passed")
    else:
        print("test 3 failed")