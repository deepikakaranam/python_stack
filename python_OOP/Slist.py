class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Slist:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addnode(self, value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node

    def printValues(self, msg="---"):
        runner = self.head
        print(id(self.head))
        print("printing values in the list----", msg, "---")
        while runner != None:
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
            #print(id(runner), runner.value, id(runner.next))

    def removenode(self, value):
        runner = self.head
        print("Before remove")
        #print(id(runner), runner.value)
        list.printValues("--before remove")
        self.head = runner.next
        # This is sitaram code - Start
        # if runner.value == value:
        #     self.head = runner.next
        # elif runner.value != value:
        #     while runner != None:
        #         if runner.next.value == value:
        #             runner.next = runner.next.next
        #             break
        #         runner = runner.next
        # This is sitaram code - End
        #print(id(self.head), self.head.value)
        list.printValues("--After reomve")
        # while runner != None:
        #     previous.runner = runner
        #     runner = runner.next


list = Slist(3)
list.addnode(7)
list.addnode(8)
list.addnode(9)
list.addnode(3)
list.addnode(1)
list.addnode(4)
print(list.__dict__)
list.removenode(3)
