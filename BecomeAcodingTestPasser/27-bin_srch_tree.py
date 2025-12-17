class Node:
    # 트리에서 데이터를 저장하는 **하나의 상자 (노드)**를 정의
    # None:초기값이 없는 변수를 만들 때, 함수 인자의 초기값을 설정할 때 사용
    def __init__(self, key):
        self.left = None # 왼쪽 자식을 가리키는 포인터
        self.right = None # 오른쪽 자식을 가리키는 포인터
        self.val = key # 이 상자에 저장될 노드의 값(key)

class BST:
    # 노드들을 모아서 전체 BST 구조를 관리, 
    # 데이터를 넣고(insert) 찾는(search) 기능을 제공
    def __init__(self):
        self.root = None
        # 초기값이 없는 변수를 만들 때, 함수 인자의 초기값을 설정할 때 사용
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
"""
🌳 핵심 개념: 이진 탐색 트리 (BST)
이진 탐색 트리는 숫자를 저장할 때 항상 다음의 두 가지 규칙을 지킵니다.
- 왼쪽 자식: 부모(현재 노드)의 값보다 작은 값만 저장합니다.
- 오른쪽 자식: 부모(현재 노드)의 값보다 크거나 같은 값만 저장합니다.
이 규칙 덕분에 숫자를 찾을 때 모든 숫자를 일일이 확인할 필요가 없어집니다.
"""