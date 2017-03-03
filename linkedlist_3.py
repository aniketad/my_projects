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
    
    def addlists(self, l1, l2):
        carry = 0
        first = l1.head
        second = l2.head
        while(first and second):
            sum = first.data + second.data + carry
            if sum > 10:
                carry = 1
            else:
                carry = 0
            if carry == 1:
                sum = sum % 10
            self.insertatbottom(sum)
            first = first.next
            second = second.next
            
        if first:
            rem = first
        elif second:
            rem = second
            
        if rem:
            while(rem):
                sum = rem.data + carry
                if sum > 10:
                    carry = 1
                else:
                    carry = 0
                if carry == 1:
                    sum = sum % 10
                self.insertatbottom(sum)
                rem = rem.next
                
    def insertatbottom(self, data):
        if self.head == None:
            self.pushtostack(data)
        else:
            tmp = self.popfromstack()
            self.insertatbottom(data)
            self.pushtostack(tmp)

# Python program to demonstrate circular linked list traversal 

# Structure for a Node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data 
		self.next = None

class CircularLinkedList:
	
	# Constructor to create a empty circular linked list
	def __init__(self):
		self.head = None

	# Function to insert a node at the beginning of a
	# circular linked list
	def push(self, data):
		ptr1 = Node(data)
		temp = self.head
		
		ptr1.next = self.head
        import pdb
        pdb.set_trace()
	# If linked list is not None then set the next of
	# last node
	if self.head is not None:
	    while(temp.next != self.head):
	        temp = temp.next
		temp.next = ptr1
	else:
	    ptr1.next = ptr1 # For the first node

	self.head = ptr1 

	# Function to print nodes in a given circular linked list
	def printList(self):
		temp = self.head
		if self.head is not None:
			while(True):
				print "%d" %(temp.data),
				temp = temp.next
				if (temp == self.head):
					break
                
if __name__ == '__main__':
    '''stack1 = linkedList()
    stack1.pushtostack(2)
    stack1.pushtostack(3)
    stack1.pushtostack(8)
    print "STEP: 1"
    stack1.printstack()
    stack2 = linkedList()
    stack2.pushtostack(3)
    stack2.pushtostack(4)
    stack2.pushtostack(5)
    stack2.pushtostack(2)
    stack2.pushtostack(3)
    stack2.pushtostack(8)
    print "STEP: 2"
    stack2.printstack()
    stack3 = linkedList()
    stack3.addlists(stack1, stack2)
    print "STEP: 3"
    stack3.printstack()'''
    # Driver program to test above function

    # Initialize list as empty
    cllist = CircularLinkedList()

    # Created linked list will be 11->2->56->12
    cllist.push(12)
    cllist.push(56)
    cllist.push(2)
    cllist.push(11)

    print "Contents of circular Linked List"
    cllist.printList()  

