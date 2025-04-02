import pygame, sys
from pygame.locals import *
import random, time

# Получаем количество единиц еды от пользователя
food_count_input = int(input("Введите количество единиц еды: "))

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20  # Size of one cell
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Game speed and level settings
speed = 10
level = 1
score = 0

# Initial snake position
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (CELL_SIZE, 0)

# Функция для генерации еды в случайной позиции (не на змейке)
def generate_food():
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:  # чтобы еда не появилась на змейке
            return (x, y)

# Создаем список еды согласно введенному количеству
foods = [generate_food() for _ in range(food_count_input)]

# Шрифт для отображения счета и уровня
font = pygame.font.SysFont("Verdana", 20)

def pause():
    pause_text = font.render("Пауза. Нажмите любую клавишу...", True, (255, 255, 255))
    screen.blit(pause_text, (50, 300))
    pygame.display.update()
    
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # При нажатии любой клавиши продолжаем игру
                paused = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Game loop
t = 0
running = True
while running:
    pygame.time.delay(1000 // speed)  # Control snake speed
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()

    # Управление направлением змейки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, CELL_SIZE):
        snake_direction = (0, -CELL_SIZE / 2)
    if keys[pygame.K_DOWN] and snake_direction != (0, -CELL_SIZE):
        snake_direction = (0, CELL_SIZE / 2)
    if keys[pygame.K_LEFT] and snake_direction != (CELL_SIZE, 0):
        snake_direction = (-CELL_SIZE / 2, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-CELL_SIZE, 0):
        snake_direction = (CELL_SIZE / 2, 0)

    # Передвижение змейки
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # Проверка столкновения со стенами
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        time.sleep(1)
        screen.fill(RED)
        screen.blit(game_over, (110, 240))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка столкновения с самой собой
    if new_head in snake:
        time.sleep(1)
        screen.fill(RED)
        screen.blit(game_over, (110, 240))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Добавляем новую голову к змейке
    snake.insert(0, new_head)

    # Проверяем, съела ли змейка какую-либо еду
    ate_food = False
    for food in foods:
        if new_head == food:
            score += 1
            ate_food = True
            # Генерируем новую еду вместо съеденной
            foods[foods.index(food)] = generate_food()
            # Каждые 3 очка увеличиваем уровень и скорость
            if score % 3 == 0:
                level += 1
                speed += 2
            break

    if not ate_food:
        snake.pop()  # Если еда не съедена, удаляем последний сегмент змейки

    # Отрисовка элементов
    screen.fill(BACKGROUND_COLOR)
    
    # Рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Рисуем все единицы еды
    for food in foods:
        pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Отображаем счет и уровень
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    level_text = font.render(f"Level: {level}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Обновляем экран
    pygame.display.update()

    # Однократная пауза в начале игры (если необходимо)
    if t == 0:
        pause()
        t += 1

# Завершение игры
pygame.quit()