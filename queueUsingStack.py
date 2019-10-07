# Implmenting Queue using two Stacks
# enQueue(q, x):
#
# While stack1 is not empty, push everything from stack1 to stack2.
#       Push x to stack1 (assuming size of stacks is unlimited).
#       Push everything back to stack1.
# Here time complexity will be O(n)
#
# deQueue(q):
#
# If stack1 is empty then error
# Pop an item from stack1 and return it
# Here time complexity will be O(1)

class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, data):

        while len(self.s1):
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(data)

        while len(self.s2):
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):

        if len(self.s1) == 0:
            print("Queue is Empty")
        else:
            return self.s1.pop()


if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
