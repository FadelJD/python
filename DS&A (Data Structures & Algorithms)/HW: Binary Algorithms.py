
## Question no.3 to find height ##
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):
    if root is None:
        return 0 
    leftAns = height(root.left)
    rightAns = height(root.right)
    return max(leftAns, rightAns) + 1
 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
 
print("Height of the binary tree is: " + str(height(root)))

## Question no.4 to find no. of nodes ##

class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
  
def left_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.left   
    return ht
  
def right_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.right       
    return ht
  
def TotalNodes(root):
    
    if(root == None):
        return 0
        
    lh = left_height(root)
    rh = right_height(root)
      
    if(lh == rh):
        return (1 << lh) - 1
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)
  
print(TotalNodes(root))


## Question no.5 to list all leave nodes ##
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def printLeafNodes(root: Node) -> None:
    if (not root):
        return
    if (not root.left and
        not root.right):
        print(root.data,
              end = " ")
        return

    if root.left:
        printLeafNodes(root.left)

    if root.right:
        printLeafNodes(root.right)
 

if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    printLeafNodes(root)



#



