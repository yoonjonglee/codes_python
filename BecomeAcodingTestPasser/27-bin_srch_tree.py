class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root
            while True:
                if key < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(key)
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break
    def search(self, key):
        curr = self.root
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

def solution(lst, slist):
    # 1. Create a BST from the list
    bst = BST()
    # 2. Insert the list into the BST
    for key in lst:
        bst.insert(key)
    # 3. Search the BST for the values in the second list
    result = []
    # 4. Return the result
    for sval in slist:
        if bst.search(sval): result.append(True)
        else: result.append(False)
    return result
    
lst=[5,3,8,4,2,1,7,10]; slst=[1,2,5,6]; print(solution(lst, slst))