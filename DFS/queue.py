# 리스트로 큐 구현하면 시간복잡도 높으니 deque라이브러리 사용
# queue = []

# # 삽입시 append()로 늦게 들어온 순으로 뒤로 쭉 나열되게함

# queue.append(7)
# queue.append(3)
# queue.append(2)
# queue.append(5)

# # 삭제 시 pop(0) 0인덱스로 가장 첫번째 원소부터 출력
# queue.pop(0)
# queue.append(10)
# queue.append(9)
# queue.pop(0)

# print(queue)  # 첫번째 원소부터 출력


from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
