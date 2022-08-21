import pygame
import sys
from button import Button

pygame.init()
SCREEN = pygame.display.set_mode((1792,1120))
pygame.display.set_caption("Menu")

BG = pygame.image.load("")

def get_font(size):
    pygame.font.SysFont("Calibri")

def play():
    pygame.display.set_caption("Play")

    while True:

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        PLAY_TEXT = get_font(45).render("This is the play screen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(896,560))
        SCREEN.blit(PLAY_TEXT,PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(896,760),
                            text_input="BACK", font=get_font(75), base_color="", hovering_color="")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()   
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.upadte()

def rules():
    pygame.display.set_caption("Rules")

    while True:

        RULES_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        RULES_TEXT = get_font(45).render("This is the rules screen", True, "White")
        RULES_RECT = RULES_TEXT.get_rect(center=(896,560))
        SCREEN.blit(RULES_TEXT,RULES_RECT)

        RULES_BACK = Button(image=None, pos=(896,760),
                            text_input="BACK", font=get_font(75), base_color="", hovering_color="")
        
        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()   
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    main_menu()

        pygame.display.upadte()
     
def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "")
        MENU_RECT = MENU_TEXT.get_rect(center=(896,560))

        PLAY_BUTTON = Button(image=pygame.image.load(""), pos=(896,550),
                            text_input=get_font(75), base_color="", hovering_color="")
        RULES_BUTTON = Button(image=pygame.image.load(""), pos=(896,700),
                            text_input=get_font(75), base_color="", hovering_color="")
        QUIT_BUTTON = Button(image=pygame.image.load(""), pos=(896,850),
                            text_input=get_font(75), base_color="", hovering_color="")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                pygame.quit()
                sys.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rules()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.quit()
        pygame.display.update()

main_menu()