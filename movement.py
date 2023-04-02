position = [(u, v) for v in range(64, 700, 66) for u in range(13, 800, 93)]
listposition = []
k = 0
for i in range(9):
    listposition.append(position[k:k + 9])
    k += 9

diag1 = [listposition[2][0], listposition[1][1], listposition[0][2]]
diag2 = [listposition[0][4], listposition[1][3], listposition[2][2], listposition[3][1], listposition[4][0]]
diag3 = [listposition[0][6], listposition[1][5], listposition[2][4], listposition[3][3], listposition[4][2],
         listposition[5][1], listposition[6][0]]
diag4 = [listposition[0][8], listposition[1][7], listposition[2][6], listposition[3][5], listposition[4][4],
         listposition[5][3], listposition[6][2], listposition[7][1], listposition[8][0]]
diag5 = [listposition[2][8], listposition[3][7], listposition[4][6], listposition[5][5], listposition[6][4],
         listposition[7][3], listposition[8][2]]
diag6 = [listposition[4][8], listposition[5][7], listposition[6][6], listposition[7][5], listposition[8][4]]
diag7 = [listposition[6][8], listposition[7][7], listposition[8][6]]

diag01 = [listposition[6][0], listposition[7][1], listposition[8][2]]
diag02 = [listposition[4][0], listposition[5][1], listposition[6][2], listposition[7][3], listposition[8][4]]
diag03 = [listposition[2][0], listposition[3][1], listposition[4][2], listposition[5][3], listposition[6][4],
          listposition[7][5], listposition[8][6]]
diag04 = [listposition[0][0], listposition[1][1], listposition[2][2], listposition[3][3], listposition[4][4],
          listposition[5][5], listposition[6][6], listposition[7][7], listposition[8][8]]
diag05 = [listposition[0][2], listposition[1][3], listposition[2][4], listposition[3][5], listposition[4][6],
          listposition[5][7], listposition[6][8]]
diag06 = [listposition[0][4], listposition[1][5], listposition[2][6], listposition[3][7], listposition[4][8]]
diag07 = [listposition[0][6], listposition[1][7], listposition[2][8]]
diagonales = [diag1, diag2, diag3, diag4, diag5, diag6, diag7, diag07, diag06, diag05, diag04, diag03, diag02, diag01]
lignes = listposition + [[row[j] for row in listposition] for j in range(len(listposition))]


def posKill(posinit, posdesi):
    for ligne in diagonales:
        try:
            if posinit in ligne and posdesi == ligne[ligne.index(posinit) + 2]:
                return ligne[ligne.index(posinit) + 1]
            if posdesi in ligne and posinit == ligne[ligne.index(posdesi) + 2]:
                return ligne[ligne.index(posdesi) + 1]
        except IndexError:
            pass
    for ligne in lignes:
        try:
            if posinit in ligne and posdesi == ligne[ligne.index(posinit) + 2]:
                return ligne[ligne.index(posinit) + 1]
            if posdesi in ligne and posinit == ligne[ligne.index(posdesi) + 2]:
                return ligne[ligne.index(posdesi) + 1]
        except IndexError:
            pass
    return False


def Move_IsLegal(posinit, posdesi):
    for ligne in diagonales:
        try:
            if posinit in ligne and posdesi == ligne[ligne.index(posinit) + 1]:
                return True
        except IndexError:
            pass
    for ligne in [[row[j] for row in listposition] for j in range(len(listposition))]:
        try:
            if posinit in ligne and posdesi == ligne[ligne.index(posinit) + 1]:
                return True
        except IndexError:
            pass
    return False


def superMoves(posinit, posdesi):
    for ligne in lignes:
        if posinit in ligne and posdesi in ligne and posinit != posdesi:
            return ligne
    for ligne in diagonales:
        if posinit in ligne and posdesi in ligne and posinit != posdesi:
            return ligne
    return False
