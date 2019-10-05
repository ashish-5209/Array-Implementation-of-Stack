#Stack is a Liner Data Structure which perform Insertion, Deletion in O(1) time.
# It works on the principle of Last In First Out, in which the element which is inserted first is the first one to delete.

# Below is the Array Implementaion of Stack Data Structute.

# Insert the element is the Array

def insertElement(lis, ele):

    # Here the element is inserted at the rear end
    lis.append(ele)

def deleteLast(lis):

    # The element is deleted from the rear end
    if lis:
        print(lis.pop())
    else:
        print("Stack OverFlow!")

# Check if the stack is empty or not
def isEmpty(lis):

    if len(lis) == 0:
        print("Stack is Empty.")
    else:
        print("Stack Length is: ", len(lis))

# Returning the Top Element
def isPeek(lis):
    if lis:
        print("Top Element is: ", lis[len(lis)-1])
    else:
        print("Stack is Empty.")

lis = []
isPeek(lis)
isEmpty(lis)
insertElement(lis,10)
insertElement(lis,30)
insertElement(lis,56)
insertElement(lis,78)
insertElement(lis,2)
isPeek(lis)
isEmpty(lis)
deleteLast(lis)
isPeek(lis)
isEmpty(lis)
