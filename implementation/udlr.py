# # 상하좌우 문제
# - 문제설명

# 여행가  A는 N X N 크기의 정사각형 공간 위에 서 있습니다.

# 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있습니다.

# 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다.

# 여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1) 입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.

# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀있습니다. 각 문자의 의미는 다음과 같습니다.

# L: 왼쪽으로 한 칸 이동

# R : 오른쪽으로 한 칸 이동

# U : 위로 한 칸 이동

# D : 아래로 한 칸 이동

# 첫째 줄에 공간의 크기를 나타내는 N 주어짐
# n = int(input())
# # 둘쨰 줄에 여행가 A가 이동할 계획서 내용 주어짐
# plan = list(input().split())

# # 2차원 공간 만듬 - 정사각형
# for i in range(1,n): #( 1,1) 을 첫번재로  가장 왼쪽 위 좌표로 만듬
#     for j in range(1,n):
#         print("(",i,",",j,")")


# for i in plan :
#     if i == "R" :
#         pass # 열 +1
#     elif i == "U":
#         pass # 행 -1
#     elif i == "L":
#         pass # 열 - 1
#     elif i == "D" :
#         pass # 행 + 1
# print(plan)

# 답안  예시
n = int(input())
x,y = 1,1
plans = input().split()

# L,R,U,B,에 따른 이동방향
dx = [0,0,-1,1] # x축 좌 우 어디로 가든 0 0 똑같음 >  u로 가면 -1 d 아래로 가면 +1 
dy = [-1,1,0,0] # y축 위 아래 로 가도 똑같음 > 0 0   왼쪽은 -1 오른쪽은 1 
move_types = ["L","R","U","D"]

# 이동 계획을 하나씩 확인하기
for plan in plans :
    for i in range(len(move_types)):
        if plan == move_types[i]:  # 계획서 하나하나씩과   move_types[i]는 L R U D 하나씩 뜻함  계획서와 move_type가 같으면
            nx = x + dx[i]  # 그 인덱스(문자)에 맞는 이동방향 연산해줌
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny<1 or nx > n or ny > n:  # nx 가 1 이하이면(행이 0 이하가 됨)  ny가 1 이하(열이 0이하가됨)이면 nx가 n보다 크면(n이 5인데 행이 5를 초과함)  ny가 n보다 크면(n이 5인데 y가 5를 초과함)
        continue
    # 공간을 벗어나지 않는 경우 이동수행
    x,y = nx,ny
print(x,y)