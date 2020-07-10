import pygame, sys
from pygame.locals import*

import random

# initialization for the GUI
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock Paper Scissors")

# initial uploads
background = pygame.image.load(r'assets\RPSbackground.png') 
rock = pygame.image.load(r'assets\rock.png')
paper = pygame.image.load(r'assets\paper.png')
scissors = pygame.image.load(r'assets\scissors.png')

# necessary transformations
smallRock = pygame.transform.scale(rock, (75, 75))
smallPaper = pygame.transform.scale(paper, (60, 80))
smallScissors = pygame.transform.scale(scissors, (54, 77))

largeRock = pygame.transform.scale(rock, (200, 200))
largePaper = pygame.transform.scale(paper, (200, 200))
largeScissors = pygame.transform.scale(scissors, (200, 200))

dec = 0

# logic for the game
def rock(player):
    if player == 1:
        print("playerRock")
    else:
        print("compRock")

def paper(player):
    if player == 2:
        print("playerPaper")
    else:
        print("compPaper")

def scissors(player):
    if player == 3:
        print("playerScissors")
    else:
        print("compScissors")

def compRockCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec):
    if compDec == 4:
        rock(compDec)
        compRockBlit = True
        compPaperBlit = False
        compScissorsBlit = False
        return compRockBlit
def compPaperCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec):
    if compDec == 5:
        paper(compDec)
        compRockBlit = False
        compPaperBlit = True
        compScissorsBlit = False
        return compPaperBlit
        
def compScissorsCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec):
    if compDec == 6:
        scissors(compDec)
        compRockBlit = False
        compPaperBlit = False
        compScissorsBlit = True
        return compScissorsBlit

def finalCalc(playerDec, compDec):
    if playerDec == 1:
        if compDec == 4:
            print("Tie!")
        elif compDec == 5:
            print("You Lose!")
        elif compDec == 6:
            print("You Win!")
    if playerDec == 2:
        if compDec == 4:
            print("You Win!")
        elif compDec == 5:
            print("Tie!")
        elif compDec == 6:
            print("You Lose!")
    if playerDec == 3:
        if compDec == 4:
            print("You Lose!")
        elif compDec == 5:
            print("You Win!")
        elif compDec == 6:
            print("Tie!")
    print()

# display setup
rockBlit = False
paperBlit = False
scissorsBlit = False

compRockBlit = False
compPaperBlit = False
compScissorsBlit = False
while True:
    # display GUI
    screen.blit(background, (0,0))
    screen.blit(smallRock, (40, 480))
    screen.blit(smallPaper, (184, 475))
    screen.blit(smallScissors, (321, 476))

    if(rockBlit):
        screen.blit(largeRock, (110, 115))
    elif(paperBlit):
        screen.blit(largePaper, (110, 115))
    elif(scissorsBlit):
        screen.blit(largeScissors, (110, 115))

    if(compRockBlit):
        screen.blit(largeRock, (470, 115))
    if(compPaperBlit):
        screen.blit(largePaper, (470, 115))
    if(compScissorsBlit):
        screen.blit(largeScissors, (470, 115))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] > 20 and pos[0] < 120:
                if pos[1] < 580 and pos[1] > 450:
                    dec = 1
                    print(dec)
                    rock(dec)
                    rockBlit = True
                    paperBlit = False
                    scissorsBlit = False
                    
                    compRockBlit = False
                    compPaperBlit = False
                    compScissorsBlit = False

                    
                    compDec = round(random.random() * 3) + 3

                    compRockBlit = compRockCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                    if(not compRockBlit):
                         compPaperBlit = compPaperCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                         if(not compPaperBlit):
                             compScissorsBlit = compScissorsCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                    
                    finalCalc(dec, compDec)

            elif pos[0] > 160 and pos[0] < 260:
                if pos[1] < 580 and pos[1] > 450:
                    dec = 2
                    print(dec)
                    paper(dec)
                    rockBlit = False
                    paperBlit = True
                    scissorsBlit = False

                    compRockBlit = False
                    compPaperBlit = False
                    compScissorsBlit = False
                    
                    compDec = round(random.random() * 3) + 3

                    compRockBlit = compRockCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                    if(not compRockBlit):
                         compPaperBlit = compPaperCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                         if(not compPaperBlit):
                             compScissorsBlit = compScissorsCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                    
                    finalCalc(dec, compDec)

            elif pos[0] > 300 and pos[0] < 390:
                if pos[1] < 580 and pos[1] > 450:
                    dec = 3
                    print(dec)
                    scissors(dec)
                    rockBlit = False
                    paperBlit = False
                    scissorsBlit = True
                    
                    compRockBlit = False
                    compPaperBlit = False
                    compScissorsBlit = False
                    
                    compDec = round(random.random() * 3) + 3

                    compRockBlit = compRockCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                    if(not compRockBlit):
                         compPaperBlit = compPaperCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                         if(not compPaperBlit):
                             compScissorsBlit = compScissorsCalc(compRockBlit, compPaperBlit, compScissorsBlit, compDec)
                    
                    finalCalc(dec, compDec)

    pygame.display.update()











