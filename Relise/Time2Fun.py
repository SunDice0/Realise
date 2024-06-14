import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Налаштування розміру екрану
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Хрестики-Нолики")

# Налаштування розміру клітинок
cell_size = width // 3

# Створення порожньої ігрової дошки
board = [["" for _ in range(3)] for _ in range(3)]

# Встановлення початкового гравця
current_player = "X"

# Функція для малювання дошки
def draw_board():
    screen.fill(WHITE)
    for row in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, row * cell_size), (width, row * cell_size), 3)
        pygame.draw.line(screen, BLACK, (row * cell_size, 0), (row * cell_size, height), 3)
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, RED, (col * cell_size + 20, row * cell_size + 20), 
                                ((col + 1) * cell_size - 20, (row + 1) * cell_size - 20), 2)
                pygame.draw.line(screen, RED, ((col + 1) * cell_size - 20, row * cell_size + 20), 
                                (col * cell_size + 20, (row + 1) * cell_size - 20), 2)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, BLUE, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), 
                                cell_size // 2 - 20, 2)

# Функція для перевірки перемоги
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            return board[row][0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    
    return None

# Основний ігровий цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // cell_size, y // cell_size
            if board[row][col] == "":
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print(f"Переміг гравець {winner}")
                    pygame.exit()
                    sys.exit()
                current_player = "O" if current_player == "X" else "X"
    
    draw_board()
    pygame.display.flip()