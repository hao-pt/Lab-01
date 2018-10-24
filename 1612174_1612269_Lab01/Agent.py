import Prob
from DataStructure import Stack, PriorityQueue

def aStarSearch(prob): # A* search
    pq = PriorityQueue() # hang doi uu tien
    occ = {} # dung de kiem tra xem mot state co duoc expand chua
    dist = {} # so luong step can de di tu start den cac node
    traverse = {} # dung de truy vet
    startState = prob.getStartState() # trang thai ban dau
    start = startState.getPacmanPosition() # vi tri ban dau cua pacman, cung la vi tri cua S
    dist[start] = 0 # so luong step can de di tu start den goal la 0
    pq.push(start, prob.getScore(start))
    top = 0 # khai bao bien lay top cua priority queue
    while pq.isEmpty() is False: # lap cho den khi goal node duoc expand
        top = pq.pop()
        if prob.isGoalState(top): # kiem tra xem co phai la trang thai ket thuc
            break
        if occ.get(top, 0) != 0: # kiem tra mot trang thai co duoc expand chua
            continue
        occ[top] = 1
        successors = prob.getChilds(top)
        for s in successors:
            if (dist.get(s, -1) == -1) or (occ.get(s, 0) == 0 and dist[s] > dist[top] + 1): # Neu TH1) trang thai hien tai chua tung duoc explore ,
                dist[s] = dist[top] + 1                                                    # hay TH2) duoc explore roi nhung chua duoc expand va so step moi
                traverse[s] = top                                                           #          nho hon so step cu de di duoc den trang thai nay
                pq.push(s, dist[s] + prob.getScore(s))
    if prob.isGoalState(top) is False:
        return -1
    q = Stack() # Tu day cho den het function nay la de lay list cac step de di tu S den G
    node = top
    while traverse.get(node, -1) != -1:
        q.push(node)
        node = traverse[node]
    q.push(node)
    path = []
    while q.isEmpty() is False:
        top = q.pop()
        path.append(top)
    return path


class Agent: # Class giai quyet bai toan
    def __init__(self, prob, searchType=aStarSearch):
        self.prob = prob # Van de dau vao, type: Prob
        self.searchType = searchType # loai search, mac dinh la A*

    def solve(self): # giai quyet bai toan theo loai search duoc chon
        return self.searchType(self.prob)

    def getPath(self): # Lay cac thong so can thiet de in ra file output
        startState = self.prob.getStartState()
        output = startState.getMatrix()
        n = startState.getN()
        m = startState.getM()
        path = self.solve()
        if path == -1:
            return -1
        for i in range(m):
            for j in range(n):
                if output[i][j] == '0':
                    output[i][j] = '-'
                else:
                    output[i][j] = 'o'

        for i in range(len(path)):
            output[path[i][0]][path[i][1]] = 'x'
        start = startState.getStart()
        goal = startState.getGoal()
        output[start[0]][start[1]] = 'S'
        output[goal[0]][goal[1]] = 'G'
        return len(path), path, output
