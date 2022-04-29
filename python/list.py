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
array =[ i for i in range(0,20) if i%2==1]
print(array)

#일반적인 코드 (0부터 19까지의 수 중에서 홀수만 포함하는 리스트)
array = []
for i in range(0,20) :
    if i%2 == 1:
        array.append(i)
print(array)