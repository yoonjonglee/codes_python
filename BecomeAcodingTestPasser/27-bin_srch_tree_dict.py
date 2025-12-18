# by dictionary
# 1. 데이터를 넣는 함수 (insert)
def insert(root, key):
    # 새로운 노드는 딕셔너리로 만듭니다. (값, 왼쪽, 오른쪽)
    new_node = {'val': key, 'left': None, 'right': None}
    
    # 트리가 비어있다면(root가 None이면), 새 노드가 뿌리가 됩니다.
    if root is None:
        return new_node
    
    # 트리가 비어있지 않다면, 자리를 찾아 내려갑니다.
    curr = root
    while True:
        # 넣으려는 값이 현재 값보다 작으면 왼쪽으로
        if key < curr['val']:
            if curr['left'] is not None:
                curr = curr['left'] # 계속 내려감
            else:
                curr['left'] = new_node # 빈 자리에 연결!
                break
        # 넣으려는 값이 현재 값보다 크거나 같으면 오른쪽으로
        else:
            if curr['right'] is not None:
                curr = curr['right'] # 계속 내려감
            else:
                curr['right'] = new_node # 빈 자리에 연결!
                break
    
    return root # 뿌리는 변하지 않았으니 그대로 반환

# 2. 데이터를 찾는 함수 (search)
def search(root, key):
    curr = root
    # 현재 노드가 있고, 찾는 값이 아닐 때까지 반복
    while curr is not None and curr['val'] != key:
        if key < curr['val']:
            curr = curr['left']  # 왼쪽으로 이동
        else:
            curr = curr['right'] # 오른쪽으로 이동
    
    # 반복이 끝났는데 curr가 None이면 못 찾은 것, 아니면 찾은 것
    if curr is None:
        return False
    else:
        return True

def solution(lst, slist):
    root = None # 처음엔 아무것도 없는 빈 트리
    
    # 1. 리스트의 숫자들을 트리로 만듦
    for key in lst:
        root = insert(root, key)
    #print(root)  # 트리의 뿌리 노드 출력 (디버깅용)
    result = []
    # 2. 검색할 리스트의 숫자가 있는지 확인
    for sval in slist:
        if search(root, sval):
            result.append(True)
        else:
            result.append(False)
            
    return result

# --- 테스트 코드 ---
lst = [5, 3, 8, 4, 2, 1, 7, 10]
slst = [1, 2, 5, 6]
print(solution(lst, slst)) 
# 예상 결과: [True, True, True, False]

"""
클래스가 '설계도'를 미리 만들어두는 방식이라면, 이번 방식은 그때그때 포스트잇(딕셔너리)에 내용을 적어서 붙이는 방식이라고 생각하면 이해하기 쉬워요.
node.val 대신 node['val']을 사용한다는 점만 다르고 논리는 완전히 같습니다.
🧐 무엇이 바뀌었나요?
클래스 버전과 비교했을 때 딱 3가지만 바뀌었습니다.

1. Node 클래스 삭제 🗑️
- 대신 {'val': key, 'left': None, 'right': None} 형태의 딕셔너리를 바로 만들어서 씁니다.
2. 점(.) 대신 대괄호([' ']) 사용
- node.left --> node['left']
- node.val --> node['val']
- 객체의 속성에 접근하는 대신, 딕셔너리의 '키(Key)'로 값을 찾습니다.
3. root 변수 전달
- 클래스에서는 self.root가 알아서 저장되어 있었지만, 여기서는 함수를 부를 때마다 root가 누구인지(어디서 시작해야 하는지)를 함수에게 알려줘야 합니다. (insert(root, key) 처럼요!)

# 트리 구조 예시
       5
    3     8
  2  4   7  10
1
# 위 트리는 다음과 같은 딕셔너리 구조로 표현됩니다.
{'val': 5, 'left': {'val': 3, 'left': {'val': 2, 'left': {'val': 1, 'left': None, 'right': None}, 'right': None}, 'right': {'val': 4, 'left': None, 'right': None}}, 'right': {'val': 8, 'left': {'val': 7, 'left': None, 'right': None}, 'right': {'val': 10, 'left': None, 'right': None}}}
"""