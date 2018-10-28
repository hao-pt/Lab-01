import MapState
import copy
from math import sqrt


def euclidDistance(a, b): # Tinh khoang cach euclid giua 2 diem a va b
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def modEuclidDistance(a, b): # Tinh khoang cach euclid giua 2 diem a va b, roi chia cho 2
    return (sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))/2

class Prob: # Van de va cac thao tac de giai quyet van de cho Project 1
    def __init__(self, mapState):
        self.mapState = mapState # type MapState, trang thai ban dau cua van de (tuc thong tin trong input file)
        start = self.mapState.getStart() # toa do cua vi tri bat dau
        mapState.setPacmanPosition(start[0], start[1]) # thiet lap vi tri cua pacman la vi tri ban dau

    def getStartState(self): # Lay trang thai ban dau
        return self.mapState

    def isGoalState(self, state): # Kiem tra mot trang thai co phai la goal khong
        return state == self.mapState.getGoal()

    def getChilds(self, curPacman): # Lay tat ca vi tri canh ben ma pacman co the den duoc, curPacman la vi tri hien tai cua pacman
        n = self.mapState.getN() # do dai chieu ngang
        m = self.mapState.getM() # do dai chieu doc
        adjList = [(curPacman[0] - 1, curPacman[1] - 1), # 8 vi tri canh ben cua vi tri hien tai
                   (curPacman[0] - 1, curPacman[1]),
                   (curPacman[0] - 1, curPacman[1] + 1),
                   (curPacman[0], curPacman[1] + 1),
                   (curPacman[0] + 1, curPacman[1] + 1),
                   (curPacman[0] + 1, curPacman[1]),
                   (curPacman[0] + 1, curPacman[1] - 1),
                   (curPacman[0], curPacman[1] - 1)]
        reachablePos = [] # dung de luu tru tat ca cac vi tri co the den duoc
        for a in adjList:
            if 0 <= a[0] < m and 0 <= a[1] < n and self.mapState.isObstacle(a[0], a[1]) is False:
                reachablePos.append(a)
        return reachablePos

    def getScore(self, curPacman, heuristic=euclidDistance): # tinh gia tri heuristic cua trang thai hien tai, default la theo khoang cach euclid
        return heuristic(curPacman, self.mapState.getGoal())
