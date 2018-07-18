import pygame

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

    def Board(self):
        __init__(self)

    #def update(self):

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



pygame.init()

display_width = 600
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('2048 Python')
#background = pygame.Surface(game_display.get_size())
#background = background.convert()
#background.fill((255, 255, 255))

clock = pygame.time.Clock()

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
        print("{} {} {} {}".format(left, right, up, down))



bb = Board()

game_loop()
pygame.quit()
quit()
