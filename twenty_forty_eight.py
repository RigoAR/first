import pygame
import random

# Color Definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 153, 76)

# Display color choices
TILE_COLOR = GREEN
TILE_TEXT_COLOR = WHITE
TILE_BORDER_COLOR = WHITE

BOARD_BACKGROUND_COLOR = WHITE
SCORE_TEXT_COLOR = BLACK

# Display dimensions
DISPLAY_WIDTH = 324
DISPLAY_HEIGHT = 324
DISPLAY_UPPER_PANEL_OFFSET = 80

BORDER_SIZE = 2         # tile border size in pixels

# game object class
class Board:
    """4x4 grid of integers representing the game board"""
    def __init__(self):
        self.width = 4
        self.height = 4
        self.tile_pixel_size = 80               # size of side for square tile
        self.tile_font_size = 40                # pixels for tile fonts
        self.tile_border_size = BORDER_SIZE     # tile border size
        self.score = 0                          # current score
        self.board = [[0 for i in range(self.width)] for j in range(self.height)]   # create empty board of 0's

    def set_number(self, i, j, num):
        """set board position i,j with num greater or eq to 0"""
        if i > self.width or i < 0 or j > self.height or j < 0 or num < 0:
            return False
        else:
            self.board[i][j] = num
            return True

    def get_board(self):
        """deep copy and return board"""
        new_board = [[0 for i in range(self.width)] for j in range(self.height)]
        for i in range(self.width):
            for j in range(self.height):
                new_board[i][j] = self.board[i][j]
        return new_board

    def set_board(self, board):
        self.board = board
        return True

    def is_board_full(self):
        all_full = True
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == 0:
                    # empty spot is found
                    all_full = False
        return all_full

    def _update(self, num):
        """helper function for update, caller has to check that there is an empty spot"""
        i_rand = random.randint(0, self.width - 1)
        j_rand = random.randint(0, self.height - 1)
        if self.board[i_rand][j_rand] == 0:
            self.board[i_rand][j_rand] = num
            return True
        else:
            self._update(num)

    def update(self, num):
        """fill a random (uniform) open spot on the board with num"""
        # error checking
        if self.is_board_full() or num < 0:
            return False
        else:
            self._update(num)

    def update_board(self):
        """90% chance update board with 2, 10% change update board with a 4"""
        if random.randint(0, 10) == 0:
            self.update(4)
        else:
            self.update(2)
        return

    def print_stdout(self):
        string_line = ""
        for i in range(self.width):
            # print row number and all of that rows values
            string_line = string_line + str(i) + " "
            for j in range(self.height):
                string_line = string_line + str(self.board[i][j]) + " "
            print(string_line)
            string_line = ""
        # print column numbers at the bottom
        string_line += "  "
        for i in range(self.height):
            string_line += str(i) + " "
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
                    self.score += arr[n]
                    break
                elif arr[n] == 0 and arr[m] != 0:
                    # if current spot is 0 and next spot is occupied, put next spot into the current
                    # spot and check to see if the next next occupied spot can be combined
                    # i.e. we want (0, 0, 4, 4) -> (8, 0, 0, 0) not (4, 4, 0, 0)
                    arr[n] = arr[m]
                    arr[m] = 0
                elif arr[m] != 0:
                    break
        return arr

    def shift_board_left(self):
        """shifts the board left, combines same numbers"""
        for i in range(self.width):
            self.board[i] = self.shift_array(self.board[i], self.height)
        return

    def shift_board_right(self):
        """shifts the board right, combines same numbers"""
        for i in range(self.width):
            self.board[i][::-1] = self.shift_array(self.board[i][::-1], self.height)
        return

    def shift_board_up(self):
        """shifts the board up, combines same numbers"""
        for j in range(self.height):
            new_col_arr = self.shift_array([row[j] for row in self.board], self.width)
            for i in range(self.width):
                self.board[i][j] = new_col_arr[i]
        return

    def shift_board_down(self):
        """shifts the board down, combines same numbers"""
        for j in range(self.height):
            new_col_arr = [row[j] for row in self.board]
            new_col_arr = self.shift_array(new_col_arr[::-1], self.width)
            for i in range(self.width):
                self.board[i][j] = new_col_arr[self.width - 1 - i]
        return

    def is_game_finished(self):
        """checks each element in array if spot to it's right and bottom are equal"""
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == 0:
                    return False
                if i + 1 < self.width and self.board[i][j] == self.board[i+1][j]:
                    return False
                if j + 1 < self.height and self.board[i][j] == self.board[i][j+1]:
                    return False
        return True

    def draw_tile(self, i, j):
        if i < 0 or j < 0 or i >= self.width or j >= self.height:
            return False

        # create tile and fill in with color
        tile_object = pygame.Surface((self.tile_pixel_size, self.tile_pixel_size))
        tile_object.fill(TILE_COLOR)

        # add text
        tile_font = pygame.font.Font(None, self.tile_font_size)
        tile_text = tile_font.render(str(self.board[i][j]), True, TILE_TEXT_COLOR)
        text_pos = tile_text.get_rect()
        text_pos.center = tile_object.get_rect().center
        tile_object.blit(tile_text, text_pos)

        # draw border
        tile_with_border = pygame.Surface((self.tile_pixel_size + 2*self.tile_border_size, self.tile_pixel_size + 2*self.tile_border_size))
        tile_with_border.fill(TILE_BORDER_COLOR)
        tile_with_border.blit(tile_object, (self.tile_border_size, self.tile_border_size))

        return tile_with_border

    def draw_score(self):
        # create score tile
        score_panel = pygame.Surface((DISPLAY_WIDTH, DISPLAY_UPPER_PANEL_OFFSET))
        score_panel.fill(BOARD_BACKGROUND_COLOR)

        # add score text
        score_font = pygame.font.Font(None, self.tile_font_size)
        score_string = "Score: " + str(self.score)
        score_text = score_font.render(score_string, True, SCORE_TEXT_COLOR)
        text_pos = score_text.get_rect()
        text_pos.centery = score_panel.get_rect().centery
        score_panel.blit(score_text, text_pos)
        return score_panel

    def get_row(self, row_num):
        if row_num < 0 or row_num >= self.width:
            return False
        return self.board[row_num]

    def get_col(self, col_num):
        if col_num < 0 or col_num >= self.height:
            return False
        out_board = self.height * [0]
        for j in range(self.height):
            out_board[j] = self.board[col_num][j]
        return out_board

    def set_row(self, row_num, new_row):
        if len(new_row) != self.width or row_num < 0 or row_num >= self.width:
            return False
        self.board[row_num] = new_row
        return True


def draw_display(display, board):
    """takes current display and draws the board"""
    bg = pygame.Surface(game_display.get_size())
    bg = bg.convert()
    bg.fill(BOARD_BACKGROUND_COLOR)
    display.blit(bg, (0, 0))
    # draws tiles
    for i in range(board.width):
        for j in range(board.height):
            # draw tile
            tile_object = board.draw_tile(i, j)
            display.blit(tile_object, (j * board.tile_pixel_size, i * board.tile_pixel_size + DISPLAY_UPPER_PANEL_OFFSET))
    # draws score panel
    score_panel = board.draw_score()
    display.blit(score_panel, (0, 0))
    # display
    pygame.display.flip()
    # debug
    #board.print_stdout()
    return

def game_loop(screen, board):
    game_exit = False

    while not game_exit:

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # store previous board
                prev_board = board.get_board()
                # check events
                if event.key == pygame.K_LEFT:
                    board.shift_board_left()
                    #board.update_board()
                if event.key == pygame.K_RIGHT:
                    board.shift_board_right()
                    #board.update_board()
                if event.key == pygame.K_UP:
                    board.shift_board_up()
                    #board.update_board()
                if event.key == pygame.K_DOWN:
                    board.shift_board_down()
                    #board.update_board()
                # check if board state changed, then update
                if prev_board != board.get_board():
                    board.update_board()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pass

        # view board
        draw_display(screen, board)
        #pygame.display.update()
        #clock.tick(60)
        game_exit = board.is_game_finished()

if __name__ == "__main__":
    pygame.init()

    # screen
    game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT + DISPLAY_UPPER_PANEL_OFFSET))
    pygame.display.set_caption('2048')

    #clock = pygame.time.Clock()

    # backgroud
    background = pygame.Surface(game_display.get_size())
    background = background.convert()
    background.fill(BOARD_BACKGROUND_COLOR)
    game_display.blit(background, (0, 0))
    pygame.display.flip()

    # initialize board
    board = Board()
    board.update(2)
    board.update(4)

    draw_display(game_display, board)

    game_loop(game_display, board)
    pygame.quit()
    quit()