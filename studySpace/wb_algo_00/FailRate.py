import sys

input = sys.stdin.readline

print("input single number")
n = int(input())

print("input multiple numbers for list")
usr_stgs = list(map(int, input().splitf()))  #[2, 3, 1, 3, 5, 4, 6, 2]

#fail rate : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

for i in range(1, n+1):

    not_clear = usr_stgs.count(i)
    reach = len([x for x in usr_stgs if x >= i])
    fail_rate = 0 if reach == 0 else not_clear / reach
    print(f"stage: {i}, not clear: {not_clear}, reach: {reach}, fail rate: {fail_rate:.2f}")

