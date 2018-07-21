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

    def set_number(self, i, j, num):
        """set board position i,j with num greater or eq to 0"""
        if i > self.width or j > self.height or num < 0:
            return False
        else:
            self.board[i][j] = num
            return True

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
            for j in range(self.height):
                for m in range(j + 1, self.height, 1):
                    if self.board[i][j] == self.board[i][m] and self.board[i][j] != 0:
                        self.board[i][j] = self.board[i][j] + self.board[i][m]
                        self.board[i][m] = 0
                        break
                    elif self.board[i][j] == 0 and self.board[i][m] != 0:
                        self.board[i][j] = self.board[i][m]
                        self.board[i][m] = 0
                        break
                    elif self.board[i][m] != 0:
                        break
        return

    def get_board(self):
        return self.board

def game_loop():
    left, right, up, down = False, False, False, False
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                left, right, up, down = False, False, False, False
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    left, right, up, down = False, False, False, False

        pygame.display.update()
        clock.tick(60)
        #print("{} {} {} {}".format(left, right, up, down))

if __name__ == "__main__":
    pygame.init()

    display_width = 600
    display_height = 600

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('2048 Python')

    clock = pygame.time.Clock()

    # initialize board
    bb = Board()
    bb.update(2)
    bb.update(4)

    game_loop()
    pygame.quit()
    quit()