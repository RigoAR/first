from twenty_forty_eight import Board

if __name__ == "__main__":
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

    # test 1
    bb.set_number(1,3,7)
    if bb.board[1][3] == 7:
        print ("test 1 passed")
    else:
        print ("test 1 failed")

    # test 2
    dd = bb.get_board()
    test_failed = False
    for i in range(bb.width):
        for j in range(bb.height):
            if dd[i][j] != bb.board[i][j]:
                test_failed = True

    if test_failed == True:
        print ("test 2 failed")
    elif test_failed == False:
        print ("test 2 passed")