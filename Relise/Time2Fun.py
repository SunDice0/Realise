import pygame
import sys


# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Створення вікна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Хрестики-нулики')
game_over=False

# Ігрова дошка
board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]

# Малювання ліній
def draw_lines():
    # Горизонтальні лінії
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)

    # Вертикальні лінії
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Малювання фігур
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE//4, row * SQUARE_SIZE + SQUARE_SIZE//4),
                                 (col * SQUARE_SIZE + 3*SQUARE_SIZE//4, row * SQUARE_SIZE + 3*SQUARE_SIZE//4), LINE_WIDTH)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + 3*SQUARE_SIZE//4, row * SQUARE_SIZE + SQUARE_SIZE//4),
                                 (col * SQUARE_SIZE + SQUARE_SIZE//4, row * SQUARE_SIZE + 3*SQUARE_SIZE//4), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), SQUARE_SIZE//3, LINE_WIDTH)

# Перевірка на перемогу
def check_win(player):
    # Перевірка рядків
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Перевірка стовпців
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[2][0] == board[1][1] == board[0][2] == player:
        return True

    return False

# Основна ігрова функція
def display_message(content):
    font = pygame.font.Font(None, 80)
    text = font.render(content, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

# Оновлена функція main
def main():
    screen.fill(WHITE)
    draw_lines()

    player = 'X'
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0] // SQUARE_SIZE
                mouseY = event.pos[1] // SQUARE_SIZE
                
                if board[mouseY][mouseX] is None:
                    board[mouseY][mouseX] = player
                    if check_win(player):
                        game_over = True
                        screen.fill(WHITE)
                        display_message(f"Гравець {player} виграв!")
                    player = 'O' if player == 'X' else 'X'
                else:
                    screen.fill(WHITE)
                    display_message("Нічия!")

        screen.fill(WHITE)
        draw_lines()
        draw_figures()
        pygame.display.update()

if __name__ == '__main__':
    main()
        draw_figures()
        pygame.display.update()

if __name__ == '__main__':
    main()
