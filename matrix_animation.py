import pygame
import random
import sys

pygame.init()

# Font setup (LOCKED to Hanazono)
font_size = 20
font = pygame.font.Font("/usr/share/fonts/TTF/HanaMinA.ttf", font_size)

# Initial window size (resizable)
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Matrix Code Rain")

chars = list(
    "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ"
    "キャキュキョシャシュショチャチュチョニャニュニョヒャヒュヒョミャミュミョリャリュリョ"
    "ギャギュギョジャジュジョヂャヂュヂョビャビュビョピャピュピョ"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
)

black = (0, 0, 0)
bright_green = (180, 255, 180)
dim_green = (0, 100, 0)

clock = pygame.time.Clock()

def rebuild_state(w, h):
    columns = max(1, w // font_size)
    drops = [random.randint(-20, 0) for _ in range(columns)]
    speeds = [random.uniform(0.5, 1.5) for _ in range(columns)]
    overlay = pygame.Surface((w, h))
    overlay.set_alpha(25)
    overlay.fill(black)
    return columns, drops, speeds, overlay

columns, drops, speeds, overlay = rebuild_state(width, height)

running = True
while running:
    screen.blit(overlay, (0, 0))

    for i in range(columns):
        x = i * font_size
        y = drops[i] * font_size

        char = random.choice(chars)
        screen.blit(font.render(char, True, bright_green), (x, y))

        if y - font_size >= 0:
            trail_char = random.choice(chars)
            screen.blit(font.render(trail_char, True, dim_green), (x, y - font_size))

        drops[i] += speeds[i]

        if y > height and random.random() > 0.975:
            drops[i] = random.randint(-20, 0)

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.WINDOWRESIZED:
            width, height = event.x, event.y
            columns, drops, speeds, overlay = rebuild_state(width, height)

        elif event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            columns, drops, speeds, overlay = rebuild_state(width, height)

pygame.quit()
sys.exit()
