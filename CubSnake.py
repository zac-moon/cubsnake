import pygame
import random
import sys
import os
from pygame.locals import *
from time import time

print("Hello")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

pygame.init()
font = pygame.font.Font(None, 36)

points = 0

screenWIDTH = 800
screenHEIGHT = 600
screen = pygame.display.set_mode((screenWIDTH, screenHEIGHT))
pygame.display.set_caption("CubSnake")

coin_width = 25
coin_height = 25
ranX = random.randint(0, screenWIDTH - coin_width)
ranY = random.randint(0, screenHEIGHT - coin_height)

coin = pygame.Rect(ranX, ranY, coin_width, coin_height)
coin_color = (255, 255, 255)
coin_effect_duration = 0.5  
coin_effect_start_time = 0
teleport_delay = 0.2  
teleport_start_time = 0

player_up = pygame.image.load(resource_path("imgs/player/player_UP.png")).convert_alpha()
player_down = pygame.image.load(resource_path("imgs/player/player_DOWN.png")).convert_alpha()
player_left = pygame.image.load(resource_path("imgs/player/player_LEFT.png")).convert_alpha()
player_right = pygame.image.load(resource_path("imgs/player/player_RIGHT.png")).convert_alpha()

player_rect = player_right.get_rect()
player_rect.x = 50
player_rect.y = 275

player_direction = "right"

game_state = "home"

# Define the movement speed
movement_speed = 2

points_text = font.render("Points: " + str(points), True, (255, 255, 255))

run = True
while run:
    if game_state == "home":
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_state = "playing"

        screen.fill((0, 0, 0))

        home_text = font.render("Press SPACE to Start", True, (255, 255, 255))
        screen.blit(home_text, (screenWIDTH // 2 - home_text.get_width() // 2, 300))

        pygame.display.flip()

    elif game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_rect.y -= movement_speed
            player_direction = "up"
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player_rect.y += movement_speed
            player_direction = "down"
        elif keys[pygame.K_a]or keys[pygame.K_LEFT]:
            player_rect.x -= movement_speed
            player_direction = "left"
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_rect.x += movement_speed
            player_direction = "right"

        if player_rect.left > screenWIDTH:
            player_rect.right = 0
        elif player_rect.right < 0:
            player_rect.left = screenWIDTH
        elif player_rect.top > screenHEIGHT:
            player_rect.bottom = 0
        elif player_rect.bottom < 0:
            player_rect.top = screenHEIGHT

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        if player_rect.colliderect(coin):
            if time() - teleport_start_time > teleport_delay:
                # Check if the coin would overlap with the points text
                coin_rect = pygame.Rect(
                    random.randint(0, screenWIDTH - coin_width),
random.randint(0, screenHEIGHT - coin_height),
                    coin_width,
                    coin_height,
                )
                points_rect = points_text.get_rect(
                    topleft=(screenWIDTH - points_text.get_width() - 10, 10)
                )
                
                while coin_rect.colliderect(points_rect):
                    coin_rect.x = random.randint(0, screenWIDTH - coin_width)
                    coin_rect.y = random.randint(0, screenHEIGHT - coin_height)

                coin.x = coin_rect.x
                coin.y = coin_rect.y
                points += 1

                coin_color = (255, 215, 0)  # Set coin color to gold
                coin_effect_start_time = time()
                teleport_start_time = time()

        # Check if the gold effect has expired
        if time() - coin_effect_start_time > coin_effect_duration:
            coin_color = (255, 255, 255)  # Set coin color back to white

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, coin_color, coin)  # Draw the coin with the current color

        if player_direction == "up":
            screen.blit(player_up, player_rect)
        elif player_direction == "down":
            screen.blit(player_down, player_rect)
        elif player_direction == "left":
            screen.blit(player_left, player_rect)
        else:
            screen.blit(player_right, player_rect)

        points_text = font.render("Points: " + str(points), True, (255, 255, 255))

        screen.blit(points_text, (screenWIDTH - points_text.get_width() - 10, 10))

        pygame.display.flip()

pygame.quit()