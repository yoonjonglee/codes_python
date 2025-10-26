# Welcome to the Python coding playground.
# Find the longest palindrome from the given letters string.

# Sample program:
letters = "abbbbcceeezdda" # "bbbb"
#str = "abc"
#print(str[0:3]) # l to r ; print(str[-1:-4:-1]) # r to l

# Type your code here:
# 1.  **`find_longest_palindrome(let)`:** 메인 함수로, 문자열 `let`의 모든 인덱스 `x`를 순회합니다.
def find_longest_palindrome(let):
    """
    2.  **`expnd_frm_cntr(l, r)`:** 팰린드롬을 확장하는 핵심 보조 함수입니다.
    * `while l >= 0 and r < len(let) and let[l] == let[r]:` 이 조건이 참인 동안, 즉, 문자열의 범위를 벗어나지 않고 양쪽 문자가 같으면 계속 확장합니다.
    * `return let[l+1:r]` 확장이 멈춘 시점의 `l`과 `r`은 **팰린드롬을 벗어난 위치**이므로, 실제 팰린드롬 부분 문자열은 한 칸씩 안쪽인 `l+1`부터 `r` 전까지를 슬라이싱하여 반환합니다.
    """
    def expnd_frm_cntr(l, r):
      while l >= 0 and r < len(let) and let[l] == let[r]:
        l-= 1; r+=1
      return let[l+1:r]
    lp = ""
    for x in range(len(let)):
      # 3.  **`po = expnd_frm_cntr(x, x)`:** **홀수 길이** 팰린드롬 탐색 (중심이 한 문자)
      po = expnd_frm_cntr(x, x)
      # 4.  **`pe = expnd_frm_cntr(x, x+1)`:** **짝수 길이** 팰린드롬 탐색 (중심이 두 문자 사이)
      pe = expnd_frm_cntr(x, x+1)
      # 5.  **`if len(po) > len(lp): lp = po`** 및 **`if len(pe) > len(lp): lp = pe`:** 찾은 팰린드롬 중 가장 긴 것을 **`lp`**에 저장합니다.
      if len(po) > len(lp): lp = po
      if len(pe) > len(lp): lp = pe


    print(lp)

find_longest_palindrome(letters)

"""
제시하신 파이썬 코드는 **"중심점 확장(Expand Around Center)"** 알고리즘을 사용하여 주어진 문자열에서 **가장 긴 팰린드롬 부분 문자열(Longest Palindromic Substring)**을 찾는 방식입니다.

---

## 🔍 중심점 확장 알고리즘 (Expand Around Center)

이 알고리즘은 **모든 가능한 중심점**을 기준으로 팰린드롬을 확장하며, 그중 가장 긴 것을 찾아내는 방식으로 작동합니다.

### 💡 핵심 원리

* **중심점(Center):** 팰린드롬은 **단일 문자**(`a`b`a`) 또는 **두 문자 사이의 공간**(`a`bb`a`)을 중심으로 가질 수 있습니다.
    * **홀수 길이 팰린드롬:** 한 문자($let[x]$)를 중심($x$, $x$)으로 설정하고 양쪽으로 확장합니다. (예: `b`b`b`)
    * **짝수 길이 팰린드롬:** 인접한 두 문자($let[x], let[x+1]$) 사이의 공간을 중심($x$, $x+1$)으로 설정하고 양쪽으로 확장합니다. (예: `b`bbb`)
* **확장(Expansion):** `expnd_frm_cntr(l, r)` 함수는 중심점 $(l, r)$에서 시작하여 **양쪽 끝 문자열이 같을 때까지** 좌우로 한 칸씩 확장($l-=1$, $r+=1$)합니다.
* **비교 및 저장:** 문자열의 모든 위치($x$)를 중심으로 홀수 길이 팰린드롬(`po`)과 짝수 길이 팰린드롬(`pe`)을 찾은 후, 현재까지 찾은 **가장 긴 팰린드롬($lp$)**과 길이를 비교하여 갱신합니다.

### 💻 코드 분석

이 알고리즘은 **$O(n^2)$**의 시간 복잡도를 가집니다. 여기서 $n$은 입력 문자열의 길이입니다. 모든 위치($n$번)에서 최대 $n$번의 확장이 발생하기 때문입니다.

"""