import pygame
import random

# game object class
class Board:
    """4x4 grid of integers representing the game board"""
    def __init__(self):
        self.width = 4
        self.height = 4
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                self.board[x][y] = 0

    def set_number(self, i, j, num):
        """set board position i,j with num greater or eq to 0"""
        if i > self.width or i < 0 or j > self.height or j < 0 or num < 0:
            return False
        else:
            self.board[i][j] = num
            return True

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board
        return True

    def is_board_full(self):
        all_full = True
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] == 0:
                    # empty spot is found
                    all_full = False
        return all_full

    def _update(self, num):
        """helper function for update, caller has to check that there is an empty spot"""
        x_rand = random.randint(0, self.width - 1)
        y_rand = random.randint(0, self.height - 1)
        if self.board[x_rand][y_rand] == 0:
            self.board[x_rand][y_rand] = num
            return True
        else:
            self._update(num)

    def update(self, num):
        """fill a random (uniform) open spot on the board with num"""
        # error checking
        if self.is_board_full() == True or num < 0:
            return False
        else:
            self._update(num)

    def print_stdout(self):
        string_line = ""
        for x in range(self.width):
            # print row number and all of that rows values
            string_line = string_line + str(x) + " "
            for y in range(self.height):
                string_line = string_line + str(self.board[x][y]) + " "
            print(string_line)
            string_line = ""
        # print column numbers at the bottom
        string_line += "  "
        for y in range(self.height):
            string_line += str(y) + " "
        print(string_line)

    def shift_array(self, arr, length):
        """shift the values in the array such that equal and adjacent numbers combine
        and that the array has all its zeros at the higher index i.e. (2, 0, 4, 4, 8)
        will become (2, 8, 8, 0, 0)"""
        for n in range(length):
            for m in range(n+1, length, 1):
                if arr[n] == arr[m] and arr[n] != 0:
                    arr[n] = arr[n] + arr[m]
                    arr[m] = 0
                    break
                elif arr[n] == 0 and arr[m] != 0:
                    arr[n] = arr[m]
                    arr[m] = 0
                    break
                elif arr[m] != 0:
                    break
        return arr

    def shift_board_left(self):
        """shifts the board left, combines same numbers"""
        for i in range(self.width):
            self.board[i] = self.shift_array(self.board[i], self.height)
        return

    def shift_board_right(self):
        """shifts the board left, combines same numbers"""
        for i in range(self.width):
            self.board[i][::-1] = self.shift_array(self.board[i][::-1], self.height)
        return

    def shift_board_up(self):
        for j in range(self.height):
            new_col_arr = self.shift_array([row[j] for row in self.board], self.width)
            for i in range(self.width):
                self.board[i][j] = new_col_arr[i]
        return

    def shift_board_down(self):
        for j in range(self.height):
            new_col_arr = [row[j] for row in self.board]
            new_col_arr = self.shift_array(new_col_arr[::-1], self.width)
            for i in range(self.width):
                self.board[i][j] = new_col_arr[self.width - 1 - i]
        return

    def is_game_finished(self):
        game_finished = True
        for i in range(self.width - 1):
            for j in range(self.height - 1):
                if i + 1 < self.width and self.board[i][j] == self.board[i+1][j]:
                    game_finished = False
                if j + 1 < self.height and self.board[i][j] == self.board[i][j+1]:
                    game_finished = False
        return game_finished

def update_board(board):
    """90% chance update board with 2, 10% change update board with a 4"""
    if random.randint(0, 10) == 0:
        board.update(4)
    else:
        board.update(2)
    return

def display(board):
    #board.print_stdout()
    return

def game_loop(board):
    game_exit = False

    while not game_exit:

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.shift_board_left()
                    update_board(board)
                if event.key == pygame.K_RIGHT:
                    board.shift_board_right()
                    update_board(board)
                if event.key == pygame.K_UP:
                    board.shift_board_up()
                    update_board(board)
                if event.key == pygame.K_DOWN:
                    board.shift_board_down()
                    update_board(board)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pass

        # view board
        display(board)
        pygame.display.update()
        clock.tick(60)
        game_exit = board.is_game_finished()

if __name__ == "__main__":
    pygame.init()

    display_width = 600
    display_height = 600

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('2048')

    clock = pygame.time.Clock()

    # backgroud
    background = pygame.Surface(game_display.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    #table = pygame.load_tile_table("", 4, 4)

    #game_display.blit(background, (0, 0))


    # initialize board
    board = Board()
    board.update(2)
    board.update(4)

    game_loop(board)
    pygame.quit()
    quit()