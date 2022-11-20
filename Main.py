import pygame
from Button import Button

#Fenster erstellen

pygame.init()

# Screen Width and Height
screen_height = 1024
screen_width = 640
screen = pygame.display.set_mode((screen_height, screen_width))

#Spiel background
background = pygame.image.load('Bilder/AnimeWP.jpg')

# Window name
pygame.display.set_caption("mein cooler Deckbuilder")
# Window Icon
icon = pygame.image.load('flash-card.png')
# Calling Icon
pygame.display.set_icon(icon)  # Fenstericon

start = Button(500,300)
run = True
while run:
    screen.fill((0, 0, 0)) # fill operation von screen mit dem RGB 3-Tupel für white
    # Background image
    screen.blit(background, (0, 0))
    screen.blit(start)

    Main_Deck = Button(0, 0, 'Main Deck')
    print(Main_Deck.get_width())

    #schließen des games
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()#ohne dies wird das Backgroundbild nicht auf den Screen geworfen