# 어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 

# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다
# 예를 들어 N이 17, K가 4라고 가정하자. 
# 이때 1번의 과정을 한번 수행하면 N은 16이 된다. 
# 이후에 2번의 과정을 두 번 수행하면 N은 1이 된다. 
# 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됩니다. 
# 이는 N을 1로 만드는 최소 횟수입니다.

# N과 K가 주어질 때 N이 1이 될 떄까지 1번 혹은 2번의 과정을 수행해야 하는 
# 최소 횟수를 구하는 프로그램을 작성하세요

# 내가 짠 코드
# n,k= map(int,input().split())

# count =0

# while True:
#     if n == 1:
#         break
#     if n%k == 0:  # 0으로 나누어 떨어지면  n을 k로 나누기
#         n =  n /k
#         count += 1
#     else :
#         n = n - 1  # n을 k로 나누어 떨어지지 않으면 -1 해주기
#         count += 1
# print(count)

# 답안코드    - 내가 짠 코드보다 시간복잡도가 줄어듬 > 아무리 큰 수라도 빨리 실행됨
n,k = map(int,input().split())

result =0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k
    result += (n-target)
    n = target
    # n이 k보다 작을 때 (더이 상 나눌 수 없을때) 반복문 탈출
    if n <k:
        break

    # k로 나누기
    result += 1
    n //= k
result += (n-1)
print(result)


