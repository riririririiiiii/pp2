import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(len(block_list))]
unbreakable_indices = random.sample(range(len(block_list)), 10)  # Selecting 10 random bricks to be unbreakable

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

bonus_brick_indices = random.sample(range(len(block_list)), 5)  # Selecting 5 random bricks to be bonus bricks
bonus_active = False  # Flag to indicate if the bonus is active
bonus_paddle_width = paddleW  # Initial paddle width for bonus

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddleSpeed
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.x += paddleSpeed

    screen.fill(bg)

    # Drawing blocks
    for i, block in enumerate(block_list):
        color = color_list[i]
        if i in unbreakable_indices:
            pygame.draw.rect(screen, color, block)
        else:
            pygame.draw.rect(screen, color, block)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left and right
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx

    # Collision top
    if ball.centery < ballRadius + 50:
        dy = -dy

    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        if hitIndex in bonus_brick_indices and not bonus_active:
            bonus_active = True
            bonus_paddle_width += 50
        elif hitIndex not in unbreakable_indices:
            block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            game_score += 1
            collision_sound.play()

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Win condition
    if len(block_list) == 0:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(wintext, wintextRect)
        pygame.display.flip()
        pygame.time.delay(2000)  # Show the win screen for 2 seconds
        done = True  # End the game

    # Lose condition
    if ball.top > H:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(losetext, losetextRect)
        pygame.display.flip()
        pygame.time.delay(2000)  # Show the lose screen for 2 seconds
        done = True  # End the game

    pygame.display.flip()
    clock.tick(FPS)
