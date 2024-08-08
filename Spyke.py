import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition des constantes
WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20
SPEED = 10

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Création du serpent
snake = [(200, 200), (220, 200), (240, 200)]
direction = "RIGHT"

# Création de la nourriture
food = (400, 300)

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!= "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction!= "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction!= "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction!= "LEFT":
                direction = "RIGHT"

    # Déplacement du serpent
    head = snake[-1]
    if direction == "UP":
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == "DOWN":
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == "LEFT":
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == "RIGHT":
        new_head = (head[0] + BLOCK_SIZE, head[1])
    snake.append(new_head)

    # Vérification de la collision avec la nourriture
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)

    # Vérification de la collision avec le bord de l'écran
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Vérification de la collision avec le serpent lui-même
    if snake[-1] in snake[:-1]:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Affichage du serpent et de la nourriture
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()

    # Gestion du temps
    pygame.time.Clock().tick(SPEED)