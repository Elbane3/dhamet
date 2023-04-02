from movement import listposition


def posKill(posinit, posdesi):
    for i in range(9):
        for j in range(9):
            try:
                if posinit == listposition[i][j] and posdesi == listposition[i + 2][j]:
                    return listposition[i + 1][j]
                if posinit == listposition[i + 2][j] and posdesi == listposition[i][j]:
                    return listposition[i + 1][j]
            except IndexError:
                pass
    for i in range(9):
        for j in range(9):
            try:
                if posinit == listposition[i][j] and posdesi == listposition[i][j+2]:
                    return listposition[i][j+1]
                if posinit == listposition[i][j+2] and posdesi == listposition[i][j]:
                    return listposition[i][j+1]
            except IndexError:
                pass
    for i in range(0, 9, 2):
        for j in range(0, 9, 2):
            try:
                if posinit == listposition[i][j] and posdesi == listposition[i + 2][j + 2]:
                    return listposition[i + 1][j + 1]
                if posinit == listposition[i + 2][j + 2] and posdesi == listposition[i][j]:
                    return listposition[i + 1][j + 1]
            except IndexError:
                pass
    for i in range(1, 10, 2):
        for j in range(1, 10, 2):
            try:
                if posinit == listposition[i][j] and posdesi == listposition[i + 2][j + 2]:
                    return listposition[i + 1][j + 1]
                if posinit == listposition[i + 2][j + 2] and posdesi == listposition[i][j]:
                    return listposition[i + 1][j + 1]
            except IndexError:
                pass
    for i in range(0, 9, 2):
        for j in range(0, 9, 2):
            try:
                if posinit == listposition[i][j] and posdesi == listposition[i + 2][j - 2]:
                    return listposition[i + 1][j - 1]
                if posinit == listposition[i+2][j-2] and posdesi == listposition[i][j]:
                    return listposition[i + 1][j - 1]
            except IndexError:
                pass
    for i in range(1, 10, 2):
        for j in range(1, 10, 2):
            try:
                if posinit == listposition[i][j] and posdesi == listposition[i + 2][j - 2]:
                    return listposition[i + 1][j - 1]
                if posinit == listposition[i+2][j-2] and posdesi == listposition[i][j]:
                    return listposition[i + 1][j - 1]
            except IndexError:
                pass
    return False

