import pygame, sys
from node import *
from Variables import *
from button import Button


Tree = creat_tree()
pygame.init()
pygame.display.set_caption("Arbre")
window.fill(BG_Color)

Draw_Tree(Tree)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Roboto-Black.ttf", size)

def main_menu():
    while True:
        window.fill(BG_Color)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Algorithme de recherche", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 150))
        

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(Width/2, Hight/2), 
                                text_input="Select", font=get_font(70), base_color="#d7fcd4", hovering_color="White")


        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(Width/2, 2*Hight/3), 
                            text_input="QUIT", font=get_font(70), base_color="#d7fcd4", hovering_color="White")

        window.blit(MENU_TEXT, MENU_RECT)


        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def select():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        window.fill(BG_Color)

        PLAY_TEXT = get_font(45).render("Choisissez un Algorithme", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(Width/2, 100))


        MiniMax_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(Width/3, Hight/2), 
                                text_input="MiniMax", font=get_font(70), base_color="#d7fcd4", hovering_color="White")

        NegaMax_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(2 *Width/3, Hight/2), 
                                text_input="Negamax", font=get_font(70), base_color="#d7fcd4", hovering_color="White")

        AlphaBeta_BUTTON = Button(image=pygame.image.load("assets/Rect_l.png"), pos=(Width/2, 2* Hight/3), 
                                text_input="Negamax Alpha Beta", font=get_font(50), base_color="#d7fcd4", hovering_color="White")


        window.blit(PLAY_TEXT, PLAY_RECT)

        for button in [MiniMax_BUTTON, NegaMax_BUTTON, AlphaBeta_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MiniMax_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Display_MiniMax()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NegaMax_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Display_NegaMax()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AlphaBeta_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    Display_NegaMaxAlphaBetaPruning()

        pygame.display.update()

def Display_MiniMax():
    loop = True
    while loop :
        window.fill(BG_Color)
        Draw_Tree(Tree)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Mini Max", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))
        window.blit(MENU_TEXT, MENU_RECT)

        MiniMax(Tree, 1)
        loop = False
    loop = True
    while loop:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect_s.png"), pos=(100, Hight-100), 
                            text_input="Retour", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
        pygame.display.update()

def Display_NegaMax():
    loop = True
    while loop :
        window.fill(BG_Color)
        Draw_Tree(Tree)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("NegaMax", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))
        window.blit(MENU_TEXT, MENU_RECT)

        NegaMax(Tree, 1)
        loop = False
    loop = True
    while loop:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect_s.png"), pos=(100, Hight-100), 
                            text_input="Retour", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
        pygame.display.update()

def Display_NegaMaxAlphaBetaPruning():
    loop = True
    while loop :
        window.fill(BG_Color)
        Draw_Tree(Tree)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("NegaMax Alpha Beta Pruning", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))
        window.blit(MENU_TEXT, MENU_RECT)

        NegaMaxAlphaBetaPruning(Tree, 1)
        loop = False
    loop = True
    while loop:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect_s.png"), pos=(100, Hight-100), 
                            text_input="Retour", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
        pygame.display.update()

main_menu()