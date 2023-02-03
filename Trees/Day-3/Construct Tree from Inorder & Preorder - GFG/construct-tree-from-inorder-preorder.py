#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def buildtree(self, inorder, preorder, n):
        indexmap = {}
        for i in range(len(inorder)):
            indexmap[inorder[i]] = i
        self.index = 0
        def getIndex(iStart, ie, target):
            for i in range(iStart, ie + 1):
                if(inorder[i] == target):
                    return i
        def constructTree(istart, ie):
            if(istart > ie):
                return None
            root = Node(preorder[self.index])
            self.index += 1
            inorder_index = getIndex(istart, ie, root.data);
            root.left = constructTree(istart, inorder_index - 1)
            root.right = constructTree(inorder_index + 1, ie)
            return root
        return constructTree(0 , len(inorder) - 1)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends