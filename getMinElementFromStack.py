# Perform push(), pop(), isEmpty(), isPeek() and an addditional operation getMin() in O(1) time
# It is performed by using two stack where in one stack we store all the elements and in other stack we store only the minimum elements.

class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, data):

        if len(self.s1) == 0:
            self.s1.append(data)
            self.s2.append(data)

        else:
            if data <= self.s2[-1]:
                self.s1.append(data)
                self.s2.append(data)

            else:
                self.s1.append(data)

    def pop(self):
        if len(self.s1) != 0:
            print(self.s1[-1])
            x = self.s1.pop()
            if x == self.s2[-1]:
                self.s2.pop()

    def getMin(self):
        if len(self.s2) != 0:
            print(self.s2[-1])


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)

    q.getMin()
    q.pop()
    q.getMin()
    q.pop()
    q.getMin()
    q.pop()
    q.getMin()
    q.pop()
    q.getMin()
    q.pop()
    q.getMin()
    q.pop()
