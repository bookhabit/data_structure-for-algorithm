# a = [1,2,3,4,5,6,7,8,9]
# print(a)

# print(a[3])


# a[3] = 10
# print(a[3])

# n= 10
# a = [0]*n    # 0이라는 원소를 n번 곱하면 0을 n번 반복해서 생성
# print(a)

# indexing
# a = [1,2,3,4,5,6,7,8,9]
# print(a[7])
# print(a[-1])
# print(a[-3])
# a[3] = 7
# print(a)

# slicing
# a = [1,2,3,4,5,6,7,8,9]
# print(a[3])
# print(a[1:4])

# 리스트 컴프리헨션 리스트 초기화 - 반복문 조건문함수
# array = [i for i in range(10)]
# print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
# array =[ i for i in range(0,20) if i%2==1]
# print(array)

# 1부터 9까지의 수들의 제곱값을 포함하는 리스트
# array =[i*i for i in range(1,10)]
# print(array)


# 리스트 컴프리헨션   (0부터 19까지의 수 중에서 홀수만 포함하는 리스트)
# array =[ i for i in range(0,20) if i%2==1]
# print(array)

#일반적인 코드 (0부터 19까지의 수 중에서 홀수만 포함하는 리스트)
# array = []
# for i in range(0,20) :
#     if i%2 == 1:
#         array.append(i)
# print(array)

# 리스트컴프리헨션 (좋은예시)
# N X M 크기의 2차원 리스트 초기화 
# n =4
# m = 3
# array =[[0]*m for _ in range(n)]
# print(array)

# array[1][1] = 5  # 2차원 배열의 값 수정
# print(array)   올바른 방법은 [1][1] 1행1열에 원소가 5로 바뀌었음 

# # N X M 크기의 2차원 리스트 초기화 (잘못된 방법)
# n =4
# m =3
# array = [[0]*m] *n
# print(array)

# array[1][1] = 5
# print(array)  잘못된 방법은 [1][1] 모든행에 1열 원소가 5로 바뀌었음

# 언더바 사용
# 1부터 9까지의 자연수 더하기
# summary =0
# for i in range(1,10):
#     summary += i
# print(summary)

# # "Hello World" 를 5번 출력하기
# for _ in range(5):
#     print("Hello World")

# # 리스트 관련함수들
# a = [1,4,3]
# print("기본 리스트 : ",a)

# # 리스트에 원소 삽입
# a.append(2)
# print(a)

# # 오름차순 정렬
# a.sort()
# print(a)

# # 내림차순 정렬
# a.sort(reverse=True)
# print(a)

# # 리스트 원소 뒤집기
# a.reverse()
# print(a)

# # 특정 인덱스에 데이터 추가
# a.insert(2,3)
# print(a)

# # 특정 값인 데이터 개수 세기
# a.index(3)
# print(a)

# # 특정 값 데이터 삭제
# a.remove(1)
# print(a)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3,5}  # 집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a  if i not in remove_set]
print(result)