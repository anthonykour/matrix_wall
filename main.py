import sys
import os
import random
import pygame

# Check for Android (optional; harmless if not present)
try:
    import android  # type: ignore
    andr = True
except ImportError:
    andr = False

# Initialize Pygame
pygame.init()

# Font setup (use default if monospace fails)
font_size = 20
try:
    font = pygame.font.SysFont("monospace", font_size, bold=True)
except Exception:
    font = pygame.font.Font(None, font_size)

# Initial window size
info = pygame.display.Info()
width, height = info.current_w, info.current_h

# ✅ PC: resizable window. Android: keep NOFRAME as you had it.
flags = pygame.NOFRAME if andr else pygame.RESIZABLE
screen = pygame.display.set_mode((width, height), flags)
pygame.display.set_caption("Matrix Code Rain")

# Characters to use
chars = list("アイウエオカキクケコサシスセソABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

def rebuild_state(w, h):
    cols = max(1, w // font_size)
    d = [random.randint(-20, 0) for _ in range(cols)]
    s = [random.uniform(0.5, 1.5) for _ in range(cols)]
    ov = pygame.Surface((w, h))
    ov.set_alpha(25)
    ov.fill((0, 0, 0))
    return cols, d, s, ov

columns, drops, speeds, overlay = rebuild_state(width, height)

# Colors
black = (0, 0, 0)
bright_green = (180, 255, 180)
dim_green = (0, 100, 0)

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # --- rotation / resize detection (Pydroid-friendly) ---
    if andr:
        new_info = pygame.display.Info()
        new_w, new_h = new_info.current_w, new_info.current_h

        if (new_w, new_h) != (width, height):
            width, height = new_w, new_h
            screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
            columns, drops, speeds, overlay = rebuild_state(width, height)
    # --- end detection ---

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

        # ✅ PC window resizing (Wayland-safe)
        elif (not andr) and event.type == pygame.WINDOWRESIZED:
            width, height = event.x, event.y
            # Important: do NOT call set_mode again on Wayland; just rebuild derived state
            columns, drops, speeds, overlay = rebuild_state(width, height)

        # Fallback for some platforms/drivers
        elif (not andr) and event.type == pygame.VIDEORESIZE:
            width, height = event.w, event.h
            columns, drops, speeds, overlay = rebuild_state(width, height)

pygame.quit()
sys.exit()
