import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    color = (255, 255, 255)  # Default color
    mode = 'draw_line'  # Default mode is drawing lines
    points = []
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    color = (255, 0, 0)  # Change color to red
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # Change color to green
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # Change color to blue
                elif event.key == pygame.K_d:
                    mode = 'draw_rect'  # Change mode to draw rectangle
                elif event.key == pygame.K_c:
                    mode = 'draw_circle'  # Change mode to draw circle
                elif event.key == pygame.K_e:
                    mode = 'erase'  # Change mode to erase
                elif event.key == pygame.K_s:
                    mode = 'draw_square'  # Change mode to draw square
                elif event.key == pygame.K_t:
                    mode = 'draw_right_triangle'  # Change mode to draw right triangle
                elif event.key == pygame.K_u:
                    mode = 'draw_equilateral_triangle'  # Change mode to draw equilateral triangle
                elif event.key == pygame.K_h:
                    mode = 'draw_rhombus'  # Change mode to draw rhombus
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            if mode == 'draw_rect':
                pygame.draw.rect(screen, color, (points[i], (50, 50)))  # Draw rectangle
            elif mode == 'draw_circle':
                pygame.draw.circle(screen, color, points[i], radius)  # Draw circle
            elif mode == 'erase':
                pygame.draw.circle(screen, (0, 0, 0), points[i], radius)  # Erase
            elif mode == 'draw_square':
                drawSquare(screen, points[i], points[i+1], radius, color)  # Draw square
            elif mode == 'draw_right_triangle':
                drawRightTriangle(screen, points[i], points[i+1], radius, color)  # Draw right triangle
            elif mode == 'draw_equilateral_triangle':
                drawEquilateralTriangle(screen, points[i], points[i+1], radius, color)  # Draw equilateral triangle
            elif mode == 'draw_rhombus':
                drawRhombus(screen, points[i], points[i+1], radius, color)  # Draw rhombus
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, color)
            i += 1
        
        pygame.display.flip()
        clock.tick(60)

# Function to draw lines between points
def drawLineBetween(screen, index, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Function to draw a square
def drawSquare(screen, start, end, width, color):
    side = min(abs(start[0] - end[0]), abs(start[1] - end[1]))
    if start[0] < end[0]:
        x = start[0]
    else:
        x = start[0] - side
    if start[1] < end[1]:
        y = start[1]
    else:
        y = start[1] - side
    pygame.draw.rect(screen, color, (x, y, side, side), width)

# Function to draw a right triangle
def drawRightTriangle(screen, start, end, width, color):
    pygame.draw.polygon(screen, color, [(start[0], start[1]), (start[0], end[1]), (end[0], end[1])], width)

# Function to draw an equilateral triangle
def drawEquilateralTriangle(screen, start, end, width, color):
    side = min(abs(start[0] - end[0]), abs(start[1] - end[1]))
    if start[0] < end[0]:
        x = start[0]
    else:
        x = start[0] - side
    if start[1] < end[1]:
        y = start[1]
    else:
        y = start[1] - side
    pygame.draw.polygon(screen, color, [(x, y + side), (x + side / 2, y), (x + side, y + side)], width)

# Function to draw a rhombus
def drawRhombus(screen, start, end, width, color):
    side = min(abs(start[0] - end[0]), abs(start[1] - end[1]))
    if start[0] < end[0]:
        x = start[0]
    else:
        x = start[0] - side
    if start[1] < end[1]:
        y = start[1]
    else:
        y = start[1] - side
    pygame.draw.polygon(screen, color, [(x, y + side / 2), (x + side / 2, y), (x + side, y + side / 2), (x + side / 2, y + side)], width)

main()

