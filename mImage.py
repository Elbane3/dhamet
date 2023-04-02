import pygame as pg


class mImage:
    """
        mImage - moveable image
        wrapper for draggable images (of pieces)
    """

    def __init__(self, path, pos, size):
        self.path = path
        self.pos = pos
        self.currentPos = self.x, self.y = pos
        self.size = self.width, self.height = size
        image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(image, size)
        self.dragged = False

    def isClicked(self, coords):
        x = coords[0]
        y = coords[1]
        ix = self.pos[0]
        iy = self.pos[1]
        xInBox = x >= ix and x <= ix + self.width
        yInBox = y >= iy and y <= iy + self.height
        return xInBox and yInBox

    # checks if clicked and sets dragged field
    def isDragged(self, coords):
        assert self.dragged == False
        self.dragged = self.isClicked(coords)
        return self.dragged

    # called once user releases mouse click and image was being dragged
    def drop(self):
        assert self.dragged == True
        self.dragged = False

    def movePiece(self, newPos):
        self.pos = newPos
        assert self.currentPos == self.pos

    # updates location fields
    def move(self, newPos):
        self.currentPos = newPos
        self.x = newPos[0]
        self.y = newPos[1]

