import pygame
import random
from copy import deepcopy

# Set winning score
WINNING_SCORE = 2048

# Color Definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 153, 76)
GREEN2 = pygame.Color('green2')
GREY = (96, 96, 96)

# Display color choices
TILE_COLOR = GREEN
TILE_TEXT_COLOR = WHITE
TILE_BORDER_COLOR = WHITE

BOARD_BACKGROUND_COLOR = WHITE
SCORE_TEXT_COLOR = BLACK
MENU_COLOR = GREY
MENU_TEXT_COLOR = WHITE
MESSAGE_OVER_SCREEN_COLOR = GREEN2

# Display dimensions
DISPLAY_WIDTH = 324
DISPLAY_HEIGHT = 324
DISPLAY_UPPER_PANEL_OFFSET = 80     # score panel
DISPLAY_MENU_SIZE = 30              # panel offset from the top for menu

MENU_FONT_SIZE = 20
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
        return deepcopy(self.board)

    def set_board(self, board):
        self.board = deepcopy(board)
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
        """fill a random (uniform) open spot on the board with num, if already occupied try again"""
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
        """prints the board to std out"""
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

    def top_tile_value(self):
        value_top_tile = 0
        for i in range(self.width):
            for j in range(self.height):
                if value_top_tile < self.board[i][j]:
                    value_top_tile = self.board[i][j]
        return value_top_tile

    def is_game_finished(self):
        """checks to see if the game is over, checks each element in board if spot to it's right and bottom are equal"""
        if self.top_tile_value() == WINNING_SCORE:
            return True
        for i in range(self.width):
            for j in range(self.height):
                if self.board[i][j] == 0:
                    return False
                if i + 1 < self.width and self.board[i][j] == self.board[i+1][j]:
                    return False
                if j + 1 < self.height and self.board[i][j] == self.board[i][j+1]:
                    return False
        return True

    def draw_tile_with_border(self, i, j):
        """draws a tile with a border"""
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

    def get_score(self):
        """
        rtype: int
        """
        return self.score

    def set_row(self, row_num, new_row):
        if len(new_row) != self.width or row_num < 0 or row_num >= self.width:
            return False
        self.board[row_num] = new_row
        return True
# end class Board

def draw_menu():
    number_of_buttons = 5
    button_size = DISPLAY_WIDTH / number_of_buttons
    menu = pygame.Surface((DISPLAY_WIDTH, DISPLAY_MENU_SIZE))
    menu.fill(MENU_COLOR)

    # add menu options
    menu_font = pygame.font.Font(None, MENU_FONT_SIZE)

    top_score_string = "Top Score"
    top_score_text = menu_font.render(top_score_string, True, MENU_TEXT_COLOR)
    top_score_pos = top_score_text.get_rect()
    top_score_pos.centery = menu.get_rect().centery
    top_score_pos.left = 5
    menu.blit(top_score_text, top_score_pos)

    save_string = "Save"
    save_text = menu_font.render(save_string, True, MENU_TEXT_COLOR)
    save_pos = save_text.get_rect()
    save_pos.centery = menu.get_rect().centery
    save_pos.left = 1.3 * button_size
    menu.blit(save_text, save_pos)

    load_string = "Load"
    load_text = menu_font.render(load_string, True, MENU_TEXT_COLOR)
    load_pos = load_text.get_rect()
    load_pos.centery = menu.get_rect().centery
    load_pos.left = 2 * button_size
    menu.blit(load_text, load_pos)

    undo_string = "Undo"
    undo_text = menu_font.render(undo_string, True, MENU_TEXT_COLOR)
    undo_pos = undo_text.get_rect()
    undo_pos.centery = menu.get_rect().centery
    undo_pos.left = 2.7 * button_size
    menu.blit(undo_text, undo_pos)

    exit_string = "Exit"
    exit_text = menu_font.render(exit_string, True, MENU_TEXT_COLOR)
    exit_pos = exit_text.get_rect()
    exit_pos.centery = menu.get_rect().centery
    exit_pos.left = 4 * button_size
    menu.blit(exit_text, exit_pos)

    # debug
    #print("{} {} {} {} {}".format(top_score_pos, save_pos, load_pos, undo_pos, exit_pos))

    return menu

def get_current_top_score():
    top_score_string = "top score: "
    try:
        ts_file = open("top_score.txt", "r")
        score = ts_file.readline().split()[0]
        top_score_string = top_score_string + str(score)
        ts_file.close()
    except IOError:
        top_score_string = ""
        print("No top score available")
        return -1
    # debug
    #print(top_score_string)
    return int(score)

def set_current_top_score(score):
    try:
        ts_file = open("top_score.txt", "w")
        ts_file.write(str(score) + "\n")
        ts_file.close()
    except IOError:
        print("Topscore save failed")
    return True

def save_score_on_exit(board):
    """check current top score, if current game score is larger then save"""
    score = board.get_score()
    top_score = get_current_top_score()
    if top_score == -1 or score > top_score:
        set_current_top_score(board.get_score())
    return

def draw_message_over_screen(screen, text):
    """draws message over current screen"""
    screen_rect = screen.get_rect()
    font = pygame.font.Font(None, 50)
    text_on_surface = font.render(text, True, MESSAGE_OVER_SCREEN_COLOR)
    blink_rect = text_on_surface.get_rect()
    blink_rect.center = screen_rect.center
    screen.blit(text_on_surface, blink_rect)
    pygame.display.flip()
    return

def check_menu(mouse_position, board):
    """
    :param mouse_position: (x, y) tuple of position of mouse on click event
    :param board: current board object to update
    :return: string explaining button pressed

    Options:
    top score: outputs the top score of this game
    save: saves the current game to a file, values separated by whitespace (saves over the file)
    load: loads save.txt and sets as the current game
    undo: reverts to last move
    exit: quits the game
    """
    x, y = mouse_position

    # debug
    #print("{} {}".format(x, y))

    # out of bounds of menu
    if x > 281 or y > 30:
        # No menu button pressed
        return ""

    if 83 > x >= 0:
        # display top score
        top_score = max(get_current_top_score(), board.get_score())
        # debug
        #print("Top Score: " + str(top_score))
        return "Top Score: " + str(top_score)
    elif 118 > x >= 83:
        # save current game
        save_file_name = "save.txt"
        save_file = open(save_file_name, "w")
        # write score to first line in save file
        write_score_to_file = str(board.score) + "\n"
        save_file.write(write_score_to_file)
        # write board to save file, whitespace delimiter
        write_to_file_string = ""
        for row in range(board.width):
            for col in range(board.height):
                write_to_file_string = write_to_file_string + str(board.board[row][col]) + " "
            write_to_file_string = write_to_file_string + "\n"
        save_file.write(write_to_file_string)
        save_file.close()
        # debug
        #print("Save Completed")
        return "Save Completed"
    elif 167 > x >= 128:
        # load save file
        load_file_name = "save.txt"
        load_file = open(load_file_name, "r")
        # load score
        score = load_file.readline()
        score = score.split()
        board.score = int(score[0])
        # load board
        for row in range(board.width):
            line = load_file.readline()
            line = line.split()
            for col in range(board.height):
                board.board[row][col] = int(line[col])
        # debug
        #print("Load Completed")
        return "Load Completed"
    elif 216 > x >= 172:
        # undo button
        # debug
        #print("Undo")
        return "Undo"
    elif 281 > x >= 256:
        # exit button
        # debug
        #print("Exit")
        save_score_on_exit(board)
        pygame.quit()
        quit()

    # No menu button pressed
    return ""

def check_menu_exit_only(mouse_position, board):
    x, y = mouse_position

    # debug
    #print("{} {}".format(x, y))

    if 281 > x >= 256:
        # exit button
        # debug
        #print("Exit")
        save_score_on_exit(board)
        pygame.quit()
        quit()

    return True

def draw_display(display, board):
    """takes current display and draws the menu, score, and board"""
    bg = pygame.Surface(game_display.get_size())
    bg = bg.convert()
    bg.fill(BOARD_BACKGROUND_COLOR)
    display.blit(bg, (0, 0))
    # draws tiles
    for i in range(board.width):
        for j in range(board.height):
            # draw tile
            tile_object = board.draw_tile_with_border(i, j)
            display.blit(tile_object, (j * board.tile_pixel_size, i * board.tile_pixel_size + DISPLAY_MENU_SIZE + DISPLAY_UPPER_PANEL_OFFSET))
    # draw drop down menu
    menu_panel = draw_menu()
    display.blit(menu_panel, (0, 0))
    # draws score panel
    score_panel = board.draw_score()
    display.blit(score_panel, (0, DISPLAY_MENU_SIZE))
    # display
    pygame.display.flip()
    # debug
    #board.print_stdout()
    return

def game_loop(screen, board):
    """main game loop"""

    # initial previous board state for undo
    prev_board = board.get_board()
    prev_score = board.get_score()

    # initialize game exit and over display message
    game_exit = False
    message_over_screen = ""

    while not game_exit:

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score_on_exit(board)
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # on mouse button down event, check if menu button is clicked then do action, finally display message
                message_over_screen = check_menu(pygame.mouse.get_pos(), board)
                if message_over_screen == "Undo":
                    board.set_board(prev_board)
                    board.score = prev_score
                    draw_display(screen, board)
            if event.type == pygame.MOUSEBUTTONUP:
                # have a string to display over screen that goes back to blank on the mouse up event
                message_over_screen = ""
            if event.type == pygame.KEYDOWN:
                # check left, right, up, down and aswd keys to play game
                # store previous board
                prev_board = board.get_board()
                prev_score = board.get_score()
                # check keys then board shift
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    board.shift_board_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    board.shift_board_right()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    board.shift_board_up()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    board.shift_board_down()
                # check if board state changed, then update
                if prev_board != board.get_board():
                    board.update_board()
            if event.type == pygame.KEYUP:
                # pass on key up
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP \
                        or event.key == pygame.K_DOWN or event.key == pygame.K_a or event.key == pygame.K_d \
                        or event.key == pygame.K_w or event.key == pygame.K_s:
                    pass

        # view board
        draw_display(screen, board)
        draw_message_over_screen(screen, message_over_screen)
        game_exit = board.is_game_finished()

def game_over(screen, board):
    draw_display(game_display, board)
    game_exit_message = ""
    if board.top_tile_value() == WINNING_SCORE:
        game_exit_message += "You Won!"
    else:
        game_exit_message += "You Lost :("
    draw_message_over_screen(screen, game_exit_message)
    save_score_on_exit(board)

    # exit option B, game auto exits after 15 seconds
    #pygame.quit()
    #pygame.time.delay(15000)
    #pygame.quit()
    #quit()

    # exit option A
    # manually have to exit game with X or "exit" button
    while True:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score_on_exit(board)
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # on mouse button down event, check if menu button is clicked then do action, finally display message
                check_menu_exit_only(pygame.mouse.get_pos(), board)
    return True

if __name__ == "__main__":
    pygame.init()

    # screen
    game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT + DISPLAY_MENU_SIZE + DISPLAY_UPPER_PANEL_OFFSET))
    pygame.display.set_caption('2048')

    # background
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

    # main game loop
    game_loop(game_display, board)

    # game over
    game_over(game_display, board)
    save_score_on_exit(board)
    pygame.quit()
    quit()