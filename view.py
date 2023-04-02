import pygame
from pygame.locals import *

import pieces
from pieces import Piece
from movement import superMoves, position
from Killing import posKill

position_b = []
position_n = []
for i in range(40):
    position_n.append(Piece(position[i + 41], "black"))
    position_b.append(Piece(position[i], "white"))
on_init = [position_b, position_n]


def is_inCercle(pos, pos_piece, r=13):
    if (pos_piece[0] - pos[0] + 12.5) ** 2 + (pos_piece[1] - pos[1] + 12.5) ** 2 <= 2 * r ** 2:
        return True
    return False


def pos_cl(pos):
    k = 400
    for i in range(81):
        if is_inCercle(pos, position[i]):
            k = i
    if k == 400:
        pass
    else:
        return position[k]


def WhiteP(pos: tuple) -> Piece:
    if type(pos) == tuple:
        if pos_cl(pos):
            for u in on_init[0]:
                if u.getpos() == pos_cl(pos):
                    return u


def BlackP(pos: tuple) -> Piece:
    if type(pos) == tuple:
        if pos_cl(pos):
            for u in on_init[1]:
                if u.getpos() == pos_cl(pos):
                    return u


def P_inPos(pos):
    if WhiteP(pos):
        return WhiteP(pos)
    return BlackP(pos)


class View:
    """
        Presents the surface (_display_suf) to be displayed by the App object
    """

    def __init__(self):
        self.Ptremp = None
        self.poscl = (0, 0)
        self.isClicked = False
        self.size = self.width, self.height = 800, 700
        self.psize = self.pwidth, self.pheight = int(self.width / 32), int(self.height / 28)
        self._display_surf = pygame.Surface(self.size)
        self.bo = pygame.image.load("dmh2.jpg")
        self.board = pygame.display.set_mode(self.size, RESIZABLE)
        self.w_turn = True
        self.b_turn = True

    # construct all board images (mImages) and define their initial locations
    def getposcl(self):
        return self.poscl

    def Clicked(self, pos):
        if WhiteP(pos):
            self.poscl = pos_cl(pos)
            WhiteP(pos).set_imclic()
            self.isClicked = True
        elif BlackP(pos):
            self.poscl = pos_cl(pos)
            BlackP(pos).set_imclic()
            self.isClicked = True
        else:
            pass

    def move(self, pos):
        if not P_inPos(pos):
            if WhiteP(self.poscl):
                piece = WhiteP(self.poscl)
                if not piece.super and self.w_turn:
                    if piece.move(pos_cl(pos)):
                        self.moved(pos_cl(pos))
                        self.Ptremp = None
                    elif BlackP(posKill(self.poscl, pos_cl(pos))):  # Can_kill(self.poscl,pos):
                        self.Ptremp = piece
                        BlackP(posKill(self.poscl, pos_cl(pos))).setpos()
                        piece.move_to_pos(pos_cl(pos))
                        self.moved(pos_cl(pos))
                elif not piece.super and piece == self.Ptremp and self.b_turn:
                    if BlackP(posKill(self.poscl, pos_cl(pos))):  # Can_kill(self.poscl,pos):
                        BlackP(posKill(self.poscl, pos_cl(pos))).setpos()
                        piece.move_to_pos(pos_cl(pos))
                elif piece.super and superMoves(self.poscl, pos_cl(pos)) and self.w_turn:
                    if not self.superMove(pos, piece):
                        self.superKill(pos, piece)
                elif piece.super and piece == self.Ptremp and piece is not None and superMoves(
                        self.poscl, pos_cl(pos)) and self.b_turn:
                    self.superKill(pos, piece)

            elif BlackP(self.poscl):
                piece = BlackP(self.poscl)
                if not piece.super and self.b_turn:
                    if piece.move(pos_cl(pos)):
                        self.moved(pos_cl(pos))
                        self.Ptremp = None
                    if WhiteP(posKill(self.poscl, pos_cl(pos))):  # Can_kill(self.poscl,pos):
                        self.Ptremp = piece
                        WhiteP(posKill(self.poscl, pos_cl(pos))).setpos()
                        piece.move_to_pos(pos_cl(pos))
                        self.moved(pos_cl(pos))
                elif not piece.super and piece == self.Ptremp and self.w_turn:
                    if WhiteP(posKill(self.poscl, pos_cl(pos))):  # Can_kill(self.poscl,pos):
                        WhiteP(posKill(self.poscl, pos_cl(pos))).setpos()
                        piece.move_to_pos(pos_cl(pos))
                elif piece.super and superMoves(self.poscl, pos_cl(pos)) and self.b_turn:
                    if not self.superMove(pos, piece):
                        self.superKill(pos, piece)
                elif piece.super and piece == self.Ptremp and piece is not None and superMoves(
                        self.poscl, pos_cl(pos)) and self.w_turn:
                    self.superKill(pos, piece)
            try:
                P_inPos(self.poscl).set_imgpr()
            except AttributeError:
                P_inPos(pos).set_imgpr()
            self.isClicked = False
        else:
            P_inPos(self.poscl).set_imgpr()
            self.isClicked = False
            pass

    def superMove(self, pos, piece):
        l = superMoves(self.poscl, pos_cl(pos))
        m = min(l.index(self.poscl), l.index(pos_cl(pos)))
        M = max(l.index(self.poscl), l.index(pos_cl(pos)))
        k, ptrm = 0, None
        if min(l.index(self.poscl), l.index(pos_cl(pos))) == l.index(self.poscl):
            m += 1
        for j in l[m:M]:
            if P_inPos(j):
                k = 10
        if k == 0:
            piece.superMove(pos_cl(pos))
            self.moved(pos_cl(pos))
            self.Ptremp = None
            return True
        return False

    def superKill(self, pos, piece):
        l = superMoves(self.poscl, pos_cl(pos))
        m = min(l.index(self.poscl), l.index(pos_cl(pos)))
        M = max(l.index(self.poscl), l.index(pos_cl(pos)))
        k, ptrm = 0, None
        if min(l.index(self.poscl), l.index(pos_cl(pos))) == l.index(self.poscl):
            m += 1
        for j in l[m:M]:
            if P_inPos(j):
                if P_inPos(j).color != piece.color:
                    k += 1
                    ptrm = P_inPos(j)
        if k == 1:
            piece.superMove(pos_cl(pos))
            self.moved(pos_cl(pos))
            ptrm.setpos()
            self.Ptremp = piece

    def moved(self, pos):
        if P_inPos(pos).getcolor() == 'white':
            self.b_turn = True
            self.w_turn = False
        else:
            self.b_turn = False
            self.w_turn = True

    # traçage
    def redrawGame(self):

        color_light = (120, 130, 130, 95)
        self.board.blit(self.bo, (0, 0))
        """
        self.pos = (690, 655)
        else:
        self.pos = (64, 13)"""
        pygame.draw.rect(self.board, color_light, [685, 650, 80, 40])
        pygame.draw.rect(self.board, color_light, [59, 8, 80, 40])
        buttonFont = pygame.font.SysFont('Arial', 26)
        wc = buttonFont.render(str(pieces.whiteCount), True, 0)
        bc = buttonFont.render(str(pieces.blackCount), True, 0)
        self.board.blit(wc, (732, 655))
        self.board.blit(bc, (106, 13))
        for i in range(40):
            on_init[0][i].draw(self.board)
        for i in range(40):
            on_init[1][i].draw(self.board)
        pygame.display.update()

    @property
    def display_surf(self):
        return self._display_surf
