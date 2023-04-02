import pygame as pg
from view import View


class Controller:
    def __init__(self):
        self.view = View()

    def select(self):
        # set  a piece to be dragged using dragging field in View
        coordinates = pg.mouse.get_pos()
        self.view.Clicked(coordinates)

    def move(self):
        pos = pg.mouse.get_pos()
        self.view.move(pos)

    def action(self):
        if self.view.isClicked:
            self.move()
        else:
            self.select()

    def getSurface(self):
        return self.view.display_surf
