from movement import Move_IsLegal, listposition
import pygame

whiteCount = 0
blackCount = 0


class Piece:
    global whiteCount, blackCount

    def __init__(self, pos, color):
        self.super = False
        self.pos = pos
        self.color = color
        if self.color == 'white':
            self.wh = pygame.image.load("imgs/blanc.png")
        else:
            self.wh = pygame.image.load("imgs/noir.png")

    def set_imclic(self):
        if self.color == 'white':
            if self.super:
                self.wh = pygame.image.load("imgs/SWPS.png")
            else:
                self.wh = pygame.image.load("imgs/p_sel_b.png")
        else:
            if self.super:
                self.wh = pygame.image.load("imgs/SBPS.png")
            else:
                self.wh = pygame.image.load("imgs/p_sel_n.png")

    def set_imgpr(self):
        if self.color == 'white':
            if self.super:
                self.wh = pygame.image.load("imgs/SWP.png")
            else:
                self.wh = pygame.image.load("imgs/blanc.png")
        else:
            if self.super:
                self.wh = pygame.image.load("imgs/SBP.png")
            else:
                self.wh = pygame.image.load("imgs/noir.png")

    def getwh(self):
        return self.wh

    def move(self, newpos):
        if self.color == 'white':
            if Move_IsLegal(self.pos, newpos):
                self.pos = newpos
                self.set_imgpr()
                if newpos in listposition[-1]:
                    self.super = True
                return True

        else:
            if Move_IsLegal(newpos, self.pos):
                self.pos = newpos
                self.set_imgpr()
                if newpos in listposition[0]:
                    self.super = True
                return True
        return False

    def superMove(self, newpos):
        self.pos = newpos
        self.set_imgpr()

    def getcolor(self):
        return self.color

    def draw(self, screen):
        screen.blit(self.wh, self.pos)

    def getpos(self):
        return self.pos

    def setpos(self):
        global whiteCount, blackCount
        if self.color == "white":
            self.pos = (690, 655)
            whiteCount += 1
        else:
            self.pos = (64, 13)
            blackCount += 1

    def move_to_pos(self, pos):
        self.pos = pos
        if self.color == 'white' and pos in listposition[-1]:
            self.super = True
        if self.color == 'black' and pos in listposition[0]:
            self.super = True
        self.set_imgpr()
