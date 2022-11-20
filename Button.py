import pygame

class Button():
    # Colours 4 the Buttons
    button_no_hover_col = (150, 0, 0)
    button_hover_col = (255, 0, 0)
    button_clicked_col = (50, 150, 255)
    width = 120
    height = 60

    def __init__(self, bx, by, text,size):
        self.bx = bx
        self.by = by
        self.text = text
        self.size = size

    def collide_button(self):

        global clicked
        action = False

        # colours
        white = (255, 255, 255)

        # giving me Mousepos on screen
        pos = pygame.mouse.get_pos()
        # creating Rect. in Screen (my button)
        button_rect = pygame.Rect(self.bx, self.by, self.width, self.height)

        # checking if mouse is in buttons and clicked cond.
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.button_clicked_col, button_rect)
            elif pygame.mouse.get_pressed(0) == 0 and clicked == False:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.button.button_hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_no_hover_col, button_rect)

    def get_width(self):
        return self.width

Main_Deck = Button(0, 0, 'Main Deck')
Event_Deck = Button(150,140,'Event Deck')
