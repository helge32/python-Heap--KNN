class maxHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    # ordering the heap by swapping upwards
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heapList[i][0] > self.heapList[i // 2][0]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp

            i = i // 2

    # inserting a node in the Heap and order it upwards
    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.perc_up(self.size)

    # del max and swap last element with root, then ordering downwards
    def del_max(self):
        root = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.perc_down(1)
        return root

    # swapping downwards
    def perc_down(self, i):
        while (i * 2) <= self.size:
            mc = self.max_child(i)

            if self.heapList[i][0] < self.heapList[mc][0]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # Building maxHeap from a List
    def build_heap(self, list):
        i = len(list) // 2
        self.size = len(list)
        self.heapList = [0] + list
        while (i > 0):
            self.perc_down(i)
            i = i - 1
