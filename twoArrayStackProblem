# Implementing two stacks in an array
#
# push1(int x) –> pushes x to first stack
# push2(int x) –> pushes x to second stack
#
# pop1() –> pops an element from first stack and return the popped element
# pop2() –> pops an element from second stack and return the popped element
class twoStacks:

    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self,data):

        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = data
        else:
            print("Stack Overflow ")
            exit(1)

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = data
        else:
            print("Stack Overflow ")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)


# Driver program to test twoStacks class
ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(40)
print("Popped element from stack2 is " + str(ts.pop2()))
