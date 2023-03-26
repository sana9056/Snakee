import pygame
import random

# Инициализация Pygame
pygame.init()

# Задание размеров игрового поля
WIDTH = 800
HEIGHT = 800

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Задание цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Загрузка текстур для змейки и фрукта
snake_texture = pygame.image.load("snake.png")
fruit_texture = pygame.image.load("fruit.png")

# Задание размеров текстур
snake_texture = pygame.transform.scale(snake_texture, (40, 40))
fruit_texture = pygame.transform.scale(fruit_texture, (20, 20))

# Задание начальных координат змейки и фрукта
x = WIDTH / 2
y = HEIGHT / 2
speed_x = 0
speed_y = 0
fruit_x = random.randint(0, WIDTH - 20)
fruit_y = random.randint(0, HEIGHT - 20)

# Задание начальной длины змейки
size = 1

# Создание списка для хранения координат змейки
snake_list = []

# Создание переменной для хранения количества съеденных фруктов
fruit_count = 0

# Загрузка звуковых эффектов
#eat_sound = pygame.mixer.Sound("eat_sound.wav")
#crash_sound = pygame.mixer.Sound("crash_sound.wav")
#game_over_sound = pygame.mixer.Sound("game_over_sound.wav")

# Функция для создания нового фрукта
def create_fruit():
    return random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)

# Функция для рисования текста
def draw_text(text, color, x, y, size):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

# Функция для рисования змейки и фрукта
def draw_sprites():
    # Рисуем змейку
    for snake in snake_list:
        screen.blit(snake_texture, (snake[0], snake[1]))

    # Рисуем фрукт
    screen.blit(fruit_texture, (fruit_x, fruit_y))

    # Рисуем количество съеденных фруктов
    draw_text(f"Счет: {fruit_count}", WHITE, 10, 10, 30)


# Функция для проверки столкновения змейки с фруктом
def check_collision(x1, y1, x2, y2):
    if x1 + 20 > x2 and x1 < x2 + 20 and y1 + 20 > y2 and y1 < y2 + 20:
        return True
    else:
        return False

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -0.5
                speed_y = 0
            elif event.key == pygame.K_RIGHT:
                speed_x = 0.5
                speed_y = 0
            elif event.key == pygame.K_UP:
                speed_x = 0
                speed_y = -0.5
            elif event.key == pygame.K_DOWN:
                speed_x = 0
                speed_y = 0.5

    # Добавление новой головы змейки
    x += speed_x
    y += speed_y
    snake_head = [x, y]
    snake_list.append(snake_head)

    # Удаление хвоста змейки, если она стала слишком длинной
    if len(snake_list) > size:
        del snake_list[0]

    # Проверка столкновения змейки с фруктом
    if check_collision(x, y, fruit_x, fruit_y):
        #eat_sound.play()
        size += 1
        fruit_count += 1
        fruit_x, fruit_y = create_fruit()

    # Очистка экрана
    screen.fill(BLACK)

    # Рисование змейки и фрукта
    for snake in snake_list:
        screen.blit(snake_texture, (snake[0], snake[1]))
    screen.blit(fruit_texture, (fruit_x, fruit_y))

    # Рисование счета
    draw_text(f"Счет: {fruit_count}", WHITE, 10, 10, 20)

    # Обновление экрана
    pygame.display.update()

# Выход из Pygame
pygame.quit()
