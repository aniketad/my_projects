#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG)

class BST(object):
    def __init__(self):
        self.root = None

    class Node(object):
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data
    
    def searchinbst(self, root, data):
        if root is None or root.data == data:
            if root:
                logging.debug("Data found in BST-> %s" % (root.data))
                return
            else:
                logging.debug("Data not found in BST")
                return
        if data > root.data:
            self.searchinbst(root.right, data)
        else:
            self.searchinbst(root.left, data)
            
    def inorder(self, root, list):
        if root:
            self.inorder(root.left, list)
            list.append(root.data)
            self.inorder(root.right, list)
        
    def preorder(self, root, list):
        if root:
            list.append(root.data)
            self.preorder(root.left, list)
            self.preorder(root.right, list)
    
    def postorder(self, root, list):
        if root:
            self.postorder(root.left, list)
            self.postorder(root.right, list)
            list.append(root.data)
            
    def insert(self, root, node):
        if root is None:
            root = node
        else:
            if node.data > root.data:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)
    
    def searchwithparent(self, root, prev, data):
        if root is None or root.data == data:
            if root:
                logging.debug("Data found in BST-> %s" % (root.data))
                return prev, root
            else:
                logging.debug("Data not found in BST")
                return
        if data > root.data:
            return self.searchwithparent(root.right, root, data)
        else:
            return self.searchwithparent(root.left, root, data)
        
    def delete(self, root, data):
        parent, current = self.searchwithparent(root, None, data)
        if current:
            if current.left is None and current.right is None:
                if parent.left.data == current.data:
                    parent.left = None
                else:
                    parent.right = None
            
            if current.left is None:
                if parent.left.data == current.data:
                    parent.left = current.right
                else:
                    parent.right = current.right
            
            if current.right is None:
                if parent.left.data == current.data:
                    parent.left = current.left
                else:
                    parent.right = current.left
        return root
                
            

if __name__ == '__main__':
    #Driver Code
    tree = BST()
    tree.root = BST.Node(60)
    tree.insert(tree.root, BST.Node(65))
    tree.insert(tree.root, BST.Node(55))
    tree.insert(tree.root, BST.Node(50))
    tree.insert(tree.root, BST.Node(58))
    tree.insert(tree.root, BST.Node(68))
    tree.insert(tree.root, BST.Node(63))
    ptree = []
    tree.inorder(tree.root, ptree)
    logging.debug("%s" % (ptree))
    '''parent, current = tree.searchwithparent(tree.root, None, 58)
    print parent.data, current.data
    ptree = []
    tree.inorder(tree.root, ptree)
    logging.debug("%s" % (ptree))
    ptree = []
    tree.preorder(tree.root, ptree)
    logging.debug("%s" % (ptree))
    ptree = []
    tree.postorder(tree.root, ptree)
    logging.debug("%s" % (ptree))'''
    tree.root = tree.delete(tree.root, 68)
    ptree = []
    tree.inorder(tree.root, ptree)
    logging.debug("%s" % (ptree))

