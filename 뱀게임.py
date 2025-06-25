import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# 색상 정의
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 화면 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('뱀 게임')
clock = pygame.time.Clock()

# 뱀 초기 설정
def init_snake():
    return [(WIDTH // 2, HEIGHT // 2)]

def random_food():
    x = random.randrange(0, WIDTH, CELL_SIZE)
    y = random.randrange(0, HEIGHT, CELL_SIZE)
    return (x, y)

def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def main():
    snake = init_snake()
    direction = (CELL_SIZE, 0)
    food = random_food()
    score = 0
    running = True

    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        # 뱀 이동
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # 음식 먹었는지 확인
        if new_head == food:
            score += 1
            food = random_food()
        else:
            snake.pop()

        # 충돌 확인
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake[1:]
        ):
            print(f'게임 오버! 점수: {score}')
            running = False

        # 화면 그리기
        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__422main__':
    main()
