class linkedList(object):
    def __init__(self):
        self.head = None
        
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None
            
    def pushtostack(self, data):
        nn = self.Node(data)
        if self.head == None:
            nn.next = None
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn
            
    def printstack(self):
        head = self.head
        while (head):
            print head.data
            head = head.next
            
    def popfromstack(self):
        node = self.head
        self.head = node.next
        return node.data
    
    def insertatbottom(self, data):
        if self.head == None:
            self.pushtostack(data)
        else:
            tmp = self.popfromstack()
            self.insertatbottom(data)
            self.pushtostack(tmp)
            
    def reversestack(self):
        if self.head:
            tmp = self.popfromstack()
            self.reversestack()
            self.insertatbottom(tmp)
            
    def reverselist(self, head):
        if head.next:
            prev = head
            head = head.next
            self.reverselist(head)
            head.next = prev
        else:
            #self.head.next = None
            self.head = head
            
    def loopdetect(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print "Loop detected"
                self.removeloop(slow_p)
                return
        print "No loop"
        
    def removeloop(self, slow_p):
        ptr1 = slow_p
        ptr2 = slow_p
        k = 0
        while(ptr1.next != ptr2):
            k += 1
            ptr1 = ptr1.next
        ptr1 = self.head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next
        while(ptr1 != ptr2):
            ptr1.next
            ptr2.next
        print k
        ptr1 = ptr1.next
        while(ptr1.next != ptr2):
            ptr1 = ptr1.next
        ptr1.next = None
    
if __name__ == '__main__':
    stack1 = linkedList()
    stack1.pushtostack(11)
    stack1.pushtostack(12)
    stack1.pushtostack(18)
    stack1.pushtostack(19)
    stack1.pushtostack(20)
    stack1.pushtostack(25)
    stack1.pushtostack(32)
    print "STEP: 1"
    stack1.printstack()
    print "STEP: 2"
    stack1.reverselist(stack1.head)
    #stack1.printstack()
    stack1.loopdetect()
    stack1.printstack()
    '''print "STEP 2:"
    stack1.popfromstack()
    stack1.printstack()
    stack1.insertatbottom(19)
    print "STEP: 3"
    stack1.printstack()
    print "STEP: 4"
    stack1.reversestack()
    stack1.printstack()'''
    

