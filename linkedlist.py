class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None

def printlist(head):
    while head != None:
        print head.data
        head = head.next

def insertathead(head, new_data):
    if head == None:
        print "Invalid no linked list"
        return
    new_node = Node(new_data)
    new_node.next = head
    llist.head = new_node

def insertafter(node, new_data):
    if node == None:
        print "Invalid no linked list"
        return
    new_node = Node(new_data)
    new_node.next = node.next
    node.next = new_node

def insertend(head, new_data):
    if head == None:
        print "Invalid no linked list"
        return
    while head.next != None:
        head = head.next
    
    new_node = Node(new_data)
    new_node.next = None
    head.next = new_node

def deletenode(llist, data):
    head = llist.head
    if head == None:
        print "Invalid no linked list"
        return
    
    if head.data == data:
        llist.head = head.next
    else:
        while head.next != None:
            previous = head
            head = head.next
            if head.data == data:
                if head.next == None:
                    previous.next = None
                else:
                    previous.next = head.next

def lengthoflist(head):
    count = 0
    while head != None:
        count = count + 1
        head = head.next
    return count

def lengthoflistrecursive(head):
    count = 0
    if head == None:
        return 0
    else:
        return 1 + lengthoflistrecursive(head.next)

def searchrecursive(head, data):
    if head == None:
        return "NO"
    if head.data == data:
        return "YES"
    
    searchrecursive(head.next, data)
    

if __name__=='__main__':
    llist = linkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    second.next = third
    '''printlist(llist.head)
    print "Insert at head"
    insertathead(llist.head, 67)
    printlist(llist.head)
    print "Insert in between"
    insertafter(llist.head.next, 99)
    printlist(llist.head)
    print "Insert at the end"
    insertend(llist.head, 87)
    printlist(llist.head)
    deletenode(llist, 1)
    print "###"
    printlist(llist.head)'''
    print "Length of list is:" + str(lengthoflistrecursive(llist.head))
    print searchrecursive(llist.head, 66)

    
    