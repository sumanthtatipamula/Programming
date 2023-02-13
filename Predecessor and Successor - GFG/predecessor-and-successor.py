#User function Template for python3

'''
class Node:

	def __init__(self, x):
	    self.key = x
	    self.left = None
	    self.right = None
'''


# to simulate pass by reference pre and suc are passed as list of 1 element
#so use pre[0] and suc[0] to update their respective values

def findPreSuc(root, pre, suc, key):
    while(root):
        if(root.key < key):
            pre[0] = root
            root = root.right
        elif(root.key > key):
            suc[0] = root
            root = root.left
        else:
            right = root.right
            left = root.left
            while(left):
                pre[0] = left
                left = left.right
            while(right):
                suc[0] = right
                right = right.left
            break;
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:

	def __init__(self, x):
	    self.key = x
	    self.left = None
	    self.right = None

key=0

def insert(root,n1, n2, lr):
    if (root==None):
        return
    if(root.key==n1):
        if lr == "L":
            root.left= Node(n2)
        else:
            root.right= Node(n2)

    else:
         insert(root.left,n1,n2,lr)
         insert(root.right,n1,n2,lr)


# Driver program to test above functions
if __name__ == "__main__":

    # Let us construct the tree shown in above diagram 
    for _ in range(int(input())):
            
        n = int(input())
        root=None
        pre=[None]
        suc=[None]
        arr = [i for i in input().split()]
        i = 0
        while n:
            n1 = int(arr[i])
            i += 1
            n2 = int(arr[i])
            i+=1
            lr = arr[i]
            i+=1
            if(root==None):
                root= Node(n1)
                if lr == 'L': 
                    root.left= Node(n2)
                else:
                    root.right= Node(n2)

            else:
                insert(root,n1,n2,lr)
            n-= 1

        key = int(input())
        findPreSuc(root, pre, suc, key)
        if (pre[0] != None):
            print(pre[0].key, end = " ")
        else:
            print(-1, end = " ")
        if (suc[0] != None):
            print(suc[0].key)
        else:
            print(-1)


# } Driver Code Ends