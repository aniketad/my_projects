class linkedList(object):
    
    def __init__(self):
        self.head = None
        
    class Node(object):
        
        def __init__(self, data):
            self.data = data
            self.next = None
            
    def pushNode(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def appendNode(self, data):
        tail = self.head
        while tail.next != None:
            tail = tail.next
        new_node = self.Node(data)
        tail.next = new_node
        new_node.next = None
        
    def printList(self):
        head = self.head
        while head != None:
            print head.data
            head = head.next
            
    def swapNodes(self, d1, d2):
        #import pdb;pdb.set_trace()
        if d1 == d2:
            print "Same Node no swapping"
            return

        prevd1 = None
        currd1 = self.head
        while currd1 != None and currd1.data != d1:
            prevd1 = currd1
            currd1 = currd1.next
        prevd2 = None
        currd2 = self.head
        while currd2 != None and currd2.data != d2:
            prevd2 = currd2
            currd2 = currd2.next
            
        if currd1 == None or currd2 == None:
            print "One / both node not available."
            return
            
        if prevd1 != None:
            prevd1.next = currd2
        else:
            self.head = currd2
        
        if prevd2 != None:
            prevd2.next = currd1
        else:
            self.head = currd1
        
        tmp = currd1.next
        currd1.next = currd2.next
        currd2.next = tmp
            
    def length(self):
        head = self.head
        count = 0
        while(head):
            count += 1
            head = head.next
        return count
    
    def findmiddle(self):
        slow = self.head
        fast = self.head
        
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.data
                
if __name__ == '__main__':
    llist = linkedList()
    llist.pushNode(33)
    llist.pushNode(66)
    llist.pushNode(99)
    llist.appendNode(199)
    llist.appendNode(299)
    llist.printList()
    print "Middle=" + str(llist.findmiddle())
    #llist.swapNodes(66, 199)
    #llist.printList()