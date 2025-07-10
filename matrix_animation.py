import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Font setup
font_size = 20
font = pygame.font.SysFont('monospace', font_size, bold=True)

# Set initial window size (just a placeholder)
initial_width, initial_height = 800, 600

# Create fullscreen window
screen = pygame.display.set_mode((initial_width, initial_height), pygame.FULLSCREEN)
pygame.display.set_caption("Matrix Code Rain")

# Get actual fullscreen size (this is important!)
width, height = screen.get_size()

# Characters to use
chars = list("アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポキャキュキョシャシュショチャチュチョニャニュニョヒャヒュヒョミャミュミョリャリュリョギャギュギョジャジュジョヂャヂュヂョビャビュビョピャピュピョABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

# Calculate columns based on real width
columns = width // font_size

# Initialize drops and speeds for each column
drops = [random.randint(-20, 0) for _ in range(columns)]
speeds = [random.uniform(0.5, 1.5) for _ in range(columns)]

# Colors
black = (0, 0, 0)
bright_green = (180, 255, 180)
dim_green = (0, 100, 0)

# Clock for FPS
clock = pygame.time.Clock()

# Surface for fading trails (semi-transparent overlay)
overlay = pygame.Surface((width, height))
overlay.set_alpha(25)
overlay.fill(black)

# Main loop
running = True
while running:
    # Draw translucent overlay to fade old characters
    screen.blit(overlay, (0, 0))

    for i in range(columns):
        char = random.choice(chars)
        x = i * font_size
        y = drops[i] * font_size

        # Draw head character bright green
        char_surface = font.render(char, True, bright_green)
        screen.blit(char_surface, (x, y))

        # Draw dim trailing character for simple trail effect
        if y - font_size >= 0:
            trail_char = random.choice(chars)
            trail_surface = font.render(trail_char, True, dim_green)
            screen.blit(trail_surface, (x, y - font_size))

        drops[i] += speeds[i]

        # Reset drop with a small random chance when below screen
        if y > height and random.random() > 0.975:
            drops[i] = random.randint(-20, 0)

    pygame.display.flip()
    clock.tick(30)

    # Event handling (quit on close or ESC)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

pygame.quit()
sys.exit()
