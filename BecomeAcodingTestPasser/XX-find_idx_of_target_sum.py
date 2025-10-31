# Welcome to the Python coding playground.
# Find which two numbers of the given numbers list, when summed up, equal the target value. Return their indices.

# Sample list and target values to use:
numbers = [1, 2, 4, 7, 12]
target1 = 6 # 1, 2
target2 = 11 # 2, 3
target3 = 18 # 2, 4, 12
target4 = 26 # 0, 1, 2, 3, 4
target5 = 88
# Type your code here:
def find_indices_of_target_sum(ns, t):
    """
    # 주어진 숫자 리스트에서 두 수의 인덱스를 찾는 함수
    for x in range(len(ns)):
        if ns[x] > t: continue
        elif (t-ns[x]) in ns: return x, ns.index(t-ns[x])
    """
    """
    # 주어진 숫자 리스트에서 두 수의 인덱스를 찾는 함수 - 해시맵 사용
    idx = {}
    for x, n in enumerate(ns):
        cv = t - n
        if cv in idx: return idx[cv], x
        idx[n] = x; print(idx)
    """
    res = [] # 결과를 찾았을 때 저장할 리스트
    """재귀적으로 모든 부분집합의 합을 탐색하는 함수"""
    def backtrack(st, csum, cidx):
        # 1. 종료 조건 및 성공 조건 
        if csum == t:
            # 합이 target과 같으면 결과에 인덱스 추가
            res.extend(cidx)
            return True # 결과를 찾았으므로 True 반환
        # 2. 탐색 중단 조건 (성공 가능성이 없을 때 가지치기)
        if csum > t:
            return False # 현재 합이 이미 target 초과, 추가 탐색 불필요
        # 3. 재귀 호출 (현재 인덱스부터 끝까지 다음 원소 선택)
        for x in range(st, len(ns)):
            # 백트래킹 과정: 현재 원소를 선택
            csum += ns[x] # 현재 원소를 더함
            cidx.append(x) # 현재 인덱스를 추가
            # (2) 다음 탐색
            # 다음 원소는 현재 원소의 다음 인덱스(i + 1)부터 탐색 시작
            if backtrack(x+1, csum, cidx):
                return True # 결과를 찾았으므로 True 반환
            # 백트래킹 과정: 현재 원소 선택 취소
            csum -= ns[x] # 현재 원소를 더한 값을 빼서 원래 상태로 복원
            cidx.pop() # 현재 인덱스를 제거하여 원래 상태로 복원
        return False # 모든 원소를 탐색했으나 결과를 찾지 못함

    backtrack(0, 0, []) # 초기 호출: 시작 인덱스 0, 현재 합 0, 현재 인덱스 리스트 빈 리스트

    return tuple(res) # 결과 인덱스 리스트를 튜플로 변환하여 반환
    

print(find_indices_of_target_sum(numbers, target1))  # (1, 2)
print(find_indices_of_target_sum(numbers, target2))  # (2, 3)
print(find_indices_of_target_sum(numbers, target3)) # (1, 2, 4)
print(find_indices_of_target_sum(numbers, target4)) # (0, 1, 2, 3, 4)
print(find_indices_of_target_sum(numbers, target5)) # ()
