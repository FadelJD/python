class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newnode = Node(val)
        if (self.root is None):
            self.root = newnode
        else:
            self.__insert_node(self.root, newnode)

    def __insert_node(self, current_node, newnode):
        val = newnode.data
        if (val <= current_node.data):
            if (current_node.left is not None):
                self.__insert_node(current_node.left, newnode)
            else:
                current_node.left = newnode
        elif (val > current_node.data):
            if (current_node.right is not None):
                self.__insert_node(current_node.right, newnode)
            else:
                current_node.right = newnode

    def find(self, val):
        return self.__find_node(self.root, val)

    def __find_node(self, current, val):
        found = False
        prev = None
        while not found:
            if val <= current.data:
                if current.data == val:
                    print("found",val)
                    return current, prev
                prev = current
                current = current.left
                if current is None:
                    print("error")
                    return False
            if val > current.data:
                if current.data == val:
                    print("found", val)
                    return current, prev
                prev = current
                current = current.right
                if current is None:
                    print("error")
                    return False

    def remove(self, val):
        nodes = self.find(val)
        if nodes is False:
            print("not in tree")
            return
        re = nodes[0]
        prev = nodes[1]
        if re.left is None and re.right is None:
            if re == self.root:
                self.root = None
                print(val, "removed, tree is empty")
            else:
                if prev.right == re:
                    prev.right = None
                elif prev.left == re:
                    prev.left = None
                print("removed", val)
            return
        if re.left is None:
            if re is not self.root:
                if prev.right == re:
                    prev.right = re.right
                elif prev.left == re:
                    prev.left = re.right
                re.right = None
                return
            if re is self.root:
                self.root = re.right
        if re.left is not None:
            current = re.left
            if current.right is None:
                if prev.right == re:
                    prev.right = current
                if prev.left == re:
                    prev.left = current
                current.right = re.right
                re.left = None
                re.right = None
                print("removed", val)
                return
            else:
                while current.right is not None:
                    before = current
                    current = current.right
                if re is not self.root:
                    if prev.right == re:
                        prev.right = current
                    if prev.left == re:
                        prev.left = current
                if current.left is not None:
                    before.right = current.left
                if current.left is None:
                    before.right = None
                current.left = re.left
                current.right = re.right
                if re is self.root:
                    self.root = current
                re.left = None
                re.right = None
                print("removed", val)
                return

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def preorder(self,root):
        if root is not None:
            if root == self.root:
                print(root.data, "(TOP)")
            else:
                print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            if root == self.root:
                print(root.data, "(TOP)")
            else:
                print(root.data)
            self.inorder(root.right)

    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            if root == self.root:
                print(root.data, "(TOP)")
            else:
                print(root.data)

    def print(self,root):
        if root.left is not None:
            self.print(root.left)
        if root == self.root:
            print(root.data,"(TOP)")
        if root != self.root:
            print(root.data)
        if root.right is not None:
            self.print(root.right)

    def trim(self,minimum, maximum, root):
        if root is not None:
            self.trim(minimum,maximum,root.left)
            self.trim(minimum,maximum,root.right)
            if root.data < minimum or root.data > maximum:
                self.remove(root.data)

def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)


c = BST()
print("Tree is empty?", c.is_empty())
c.insert(50)
print("Tree is empty?", c.is_empty())
c.remove(50)
print("Tree is empty?", c.is_empty())

