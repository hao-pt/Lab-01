from math import sqrt
import copy


class MapState: # luu tru trang thai hien tai
    def __init__(self, n=0, m=0, matrix=[], start=(0, 0), goal=(0, 0), pacman=(0, 0)):
        self.n = n # do dai chieu ngang
        self.m = m # do dai chieu doc
        self.matrix = copy.deepcopy(matrix) # ma tran the hien ban do di chuyen
        self.start = start # vi tri diem bat dau
        self.goal = goal # vi tri diem ket thuc
        self.pacman = pacman # vi tri cua pacman

    def getN(self): # Lay do dai chieu ngang
        return self.n

    def getM(self): # Lay do dai chieu doc
        return self.m

    def getMatrix(self): # Lay ma tran the hien ban do di chuyen
        return copy.deepcopy(self.matrix)

    def getStart(self): # Lay vi tri diem bat dau
        return self.start

    def getGoal(self): # Lay vi tri diem ket thuc
        return self.goal

    def getPacmanPosition(self): # Lay vi tri hien tai cua pacman
        return self.pacman

    def setPacmanPosition(self, x, y): # Thiet lap vi tri hien tai cua pacman
        self.pacman = (x, y)

    def isObstacle(self, x, y): # Kiem tra vi tri co toa do (x,y) co phai la chuong ngai vat khong
        return self.matrix[x][y] == '1'



