# # 모험가 길드

# - 문제 설명

# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 ‘공포도’를 측정했는데 , ‘공포도’가 높은 모험가는 쉽게 공포를 느껴 위험상황에서 제대로 대처할 능력이 떨어집니다.

# 모험가 길드 장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다

# 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다.

# N명의 모험가에 대한 정보가 주어졌을 때 , 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.

# 내가 짠 코드 - 내림차순    틀릴경우 있음
n = int(input())
x = list(map(int,input().split()))
x.sort(reverse=True) # 내림차순
result = 0 # 그룹만들때마다 카운트
for i in x :
    max_x = max(x)
    if max_x < len(x) : 
        for j in range(max_x) :
            x.pop(0)
        result += 1
    elif max_x > len(x):
        pass
print(result)

# 답안예시 - 오름차순  (최소 인원으로 그룹지음)
# 오름차순으로 정렬하고 앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다 크거나 같다면 이를 그룹으로 설정하면 됩니다.
# 이러한 방법으로 공포도가 오름차순으로 정렬되어 있다는 점에서 , 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 됨
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의 수
count =0 # 현재 그룹에 포함된 모험가의 수

for i in data :  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기  
    if count >= i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 , 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count =0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result)






