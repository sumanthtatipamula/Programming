from os import *
from sys import *
from collections import *
from math import *

''' 
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def BTtoDLL(root):
    global head, prev
    def traverse(root):
        global head, prev
        if(not root):
            return
        traverse(root.left)
        if(not head):
            head = root
        if(prev):
            prev.right = root
        root.left = prev
        prev = root
        traverse(root.right)
    head, prev = None, None
    traverse(root)
    return head



    