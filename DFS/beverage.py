# n*m 크기의 얼음 틀이 있다 ( 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시) 구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램

# 못풀엇음
# n,m= map(int,input().split())
# frame = []
# for i in range(n):
#     ice = input()
#     frame.append(ice)
    
# for i in range(5):
#     for ice in frame[i]:
#         print(i, "i", ice,'ice')

# 답안 예시
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    # 현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0 :
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


# n,m을 공백을 기준으로 구분하여 입력 받기
n,m= map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 노드에 대하여 음료수 채우기 
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)

# 구멍뚫려있는 부분 0인 부분 >>  연결된 노드 모두 방문처리
# 칸막이가 있는 1은 이동불가 처리 
# 모든 노드 지점에 대해서 DFS , BFS 수행하여 방문된 노드 카운트 수행