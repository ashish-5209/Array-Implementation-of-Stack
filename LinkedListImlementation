# LinkedList implementation of the Stack
# Elements are inserted and deleted from the front node

class StackNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class StackList:

    def __init__(self):
        self.head = None

    def push(self, ele):

        temp = StackNode(ele)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Stack is empty.")

    def peek(self):
        if self.head:
            print(f"{self.head.data} is the Top Element.")
        else:
            print("Stack is Empty.")

    def isEmpty(self):
        if self.head:
            print("List has Elements.")
        else:
            print("Stack is Empty.")



    def printList(self):

        temp = self.head

        while temp:
            print(temp.data, end = " ")
            temp = temp.next

        print()


llist = StackList()

llist.isEmpty()
llist.peek()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.printList()
llist.isEmpty()
llist.peek()
llist.pop()
llist.printList()

