def preorder(nodes, idx):
  # idx가 노드 리스트의 길이보다 작을 때
  if idx < len(nodes):
    # 루트 노드를 출력한 다음, 왼쪽 서브 트리와 오른쪽 서브 트리를 재귀 호출하여 출력 순서대로 이어붙임
    ret = str(nodes[idx]) + " "
    ret += preorder(nodes, idx * 2 + 1) 
    ret += preorder(nodes, idx * 2 + 2)
    return ret
  # idx >= len(nodes)일 때는 빈 문자열 반환
  else: return ""

def inorder(nodes, idx):
  # idx가 노드 리스트의 길이보다 작을 때
  if idx < len(nodes):
    # 왼쪽 서브 트리를 먼저 재귀 호출하여 출력 순서대로 이어붙임
    ret = inorder(nodes, idx * 2 + 1)
    # 루트 노드를 출력한 다음, 오른쪽 서브 트리를 재귀 호출하여 출력 순서대로 이어붙임
    ret += str(nodes[idx]) + " "
    ret += inorder(nodes, idx * 2 + 2)
    return ret
  # idx >= len(nodes)일 때는 빈 문자열 반환
  else: return ""

def postorder(nodes, idx):
  # idx가 노드 리스트의 길이보다 작을 때
  if idx < len(nodes):
    # 왼쪽 서브 트리와 오른쪽 서브 트리를 재귀 호출하여 출력 순서대로 이어붙임
    ret = postorder(nodes, idx * 2 + 1)
    ret += postorder(nodes, idx * 2 + 2)
    # 루트 노드를 출력함
    ret += str(nodes[idx]) + " "
    return ret
  # idx >= len(nodes)일 때는 빈 문자열 반환
  else: return ""

def solution(nodes):
  # 전위 순회, 중위 순회, 후위 순회 결과 계산
  # 노드 리스트와 루트 노드의 인덱스를 매개변수로 각각 호출
  return [
    preorder(nodes,0)[:-1],  # 마지막 공백 제거
    inorder(nodes,0)[:-1],   # 마지막 공백 제거
    postorder(nodes,0)[:-1],  # 마지막 공백 제거
  ]
# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
#    1
#  2   3
# 4 5 6 7
print(solution([1, 2, 3, 4, 5, 6, 7])) 
# 반환값 : ["1 2 4 5 3 6 7", "4 2 5 1 6 3 7", "4 5 2 6 7 3 1"]
"""
#### preod: idx - start
preo(x,0)
- 0<1>
- preo(x,1)
  - 1<2>
  - preo(x,3)
    - 3<4>
    - preo(x,7)
	  - ""
	- preo(x,8)
	  - ""
  - preo(x,4)
    - 4<5>
	- preo(x,9)
	  - ""
	- preo(x,10)
	  - ""
- preo(x,2)
  - 2<3>
  - preo(x,5)
    - 5<6>
	- preo(x,11)
	  - ""
	- preo(x,12)
	  - ""
  - preo(x,6)
    - 6<7>
	- preo(x,13)
	  - ""
	- preo(x,14)
	  - ""
#### preod: idx - end
#### inod: idx - start
inod(x,0)
- inod(x,1)
  - inod(x,3)
    - inod(x,7)
	  - ""
	- 3<4>
	- inod(x,8)
	  - ""
  - 1<2>
  - inod(x,4)
    - inod(x,9)
	  - ""
	- 4<5>
	- inod(x,10)
	  - ""
- 0<1>
- inod(x,2)
  - inod(x,5)
    - inod(x,11)
	  - ""
	- 5<6>
	- inod(x,12)
	  - ""
  - 2<3>
  - inod(x,6)
    - inod(x,13)
	  - ""
	6<7>
	- inod(x,14)
	  - ""
#### inod: idx - end
#### postod: idx - start
postod(x,0)
- postod(x,1)
  - postod(x,3)
    - postod(x,7)
	  - ""
	- postod(x,8)
	  - ""
	- 3<4>
  - postod(x,4)
    - postod(x,9)
	  - ""
	- postod(x,10)
	  - ""
	- 4<5>
  - 1<2>
- postod(x,2)
  - postod(x,5)
    - postod(x,11)
	  - ""
	- postod(x,12)
	  - ""
	- 5<6>
  - postod(x,6)
    - postod(x,13)
	  - ""
	- postod(x,14)
	  - ""
	- 6<7>
  - 2<3>
- 0<1>
#### postod: idx - end
"""