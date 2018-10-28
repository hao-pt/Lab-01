import heapq

class Stack:
    def __init__(self):
        self.list = []

    def push(self,item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


class PriorityQueue:
    def  __init__(self):
        self.heap = [] # Chua danh sach cac node
        self.count = 0 # Bien dem de danh dau thu tu cua phan tu duoc push vao

    def push(self, item, priority):
        node = (priority, self.count, item)
        heapq.heappush(self.heap, node)
        self.count += 1

    def pop(self):
        (tmpPriority, tmpCount, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self.heap): # Tim node co gia tri giong voi item
            if i == item: # Neu tim duoc node co i giong voi item
                if p <= priority: # Neu do uu tien moi cao hon do uu tien cu thi thoat
                    break
                # nguoc lai
                del self.heap[index] # xoa node cu
                self.heap.append((priority, c, item)) # them node voi do uu tien moi
                heapq.heapify(self.heap) # chay lai heapify
                break # thoat
        else: # khong tim duoc thi push vao nhu binh thuong
            self.push(item, priority)
