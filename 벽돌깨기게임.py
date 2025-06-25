import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 크기
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# 공
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [5, -5]

# 벽돌
BRICK_ROWS = 5
BRICK_COLS = 8
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

# 점수
score = 0
font = pygame.font.SysFont(None, 36)

def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)
    score_img = font.render(f"점수: {score}", True, WHITE)
    screen.blit(score_img, (10, 10))
    pygame.display.flip()

def reset_ball():
    ball.x = WIDTH // 2 - BALL_RADIUS
    ball.y = HEIGHT // 2 - BALL_RADIUS
    ball_speed[0] = random.choice([-5, 5])
    ball_speed[1] = -5

game_over = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # 패들 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += paddle_speed

        # 공 이동
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # 벽 충돌
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball.bottom >= HEIGHT:
            game_over = True

        # 패들 충돌
        if ball.colliderect(paddle):
            ball_speed[1] = -ball_speed[1]
            ball.y = paddle.y - BALL_RADIUS * 2

        # 벽돌 충돌
        hit_index = ball.collidelist(bricks)
        if hit_index != -1:
            hit_brick = bricks.pop(hit_index)
            ball_speed[1] = -ball_speed[1]
            score += 10

        # 게임 클리어
        if not bricks:
            game_over = True

    draw()

    if game_over:
        msg = "게임 오버!" if bricks else "클리어!"
        msg_img = font.render(msg, True, WHITE)
        screen.blit(msg_img, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2000)
        # 리셋
        bricks = []
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 50, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
                bricks.append(brick)
        score = 0
        reset_ball()
        paddle.x = WIDTH // 2 - PADDLE_WIDTH // 2
        game_over = False

    clock.tick(60)
