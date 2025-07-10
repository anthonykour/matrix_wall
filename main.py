import sys, os

# Check for Android
andr = None
try:
    import android
    andr = True
except ImportError:
    andr = False

# Try importing needed modules
try:
    import sys
    import random
    import pygame
except ImportError as e:
    print("Import failed:", e)
    sys.exit(1)

# Initialize Pygame
pygame.init()

# Font setup (use default if monospace fails)
font_size = 20
try:
    font = pygame.font.SysFont('monospace', font_size, bold=True)
except:
    font = pygame.font.Font(None, font_size)

# Set fixed window size (Android fullscreen workaround)
info = pygame.display.Info()
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.display.set_caption("Matrix Code Rain")

# Characters to use
chars = list("アイウエオカキクケコサシスセソABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

# Calculate columns
columns = width // font_size

# Drops and speeds
drops = [random.randint(-20, 0) for _ in range(columns)]
speeds = [random.uniform(0.5, 1.5) for _ in range(columns)]

# Colors
black = (0, 0, 0)
bright_green = (180, 255, 180)
dim_green = (0, 100, 0)

# Setup overlay for trails
overlay = pygame.Surface((width, height))
overlay.set_alpha(25)
overlay.fill(black)

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.blit(overlay, (0, 0))

    for i in range(columns):
        char = random.choice(chars)
        x = i * font_size
        y = int(drops[i] * font_size)

        char_surface = font.render(char, True, bright_green)
        screen.blit(char_surface, (x, y))

        if y - font_size >= 0:
            trail_char = random.choice(chars)
            trail_surface = font.render(trail_char, True, dim_green)
            screen.blit(trail_surface, (x, y - font_size))

        drops[i] += speeds[i]

        if y > height and random.random() > 0.975:
            drops[i] = random.randint(-20, 0)

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

pygame.quit()
sys.exit()
