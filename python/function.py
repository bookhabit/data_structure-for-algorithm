# def add(a,b):
#     return a+b
# print(add(3,7))
# add(b=3,a=7)  # 인자를 넘겨줄 떄 직접 변수(인자)를 지정하면 매개변수의 순서가 달라도 상관없음


# def subtract(a,b):
#     return a-b

# result = add(3,7)  # 함수의 결과값을 변수에 담음
# print(result)

# global 키워드
# a = 10

# def func():
#     global a
#     a+=1
#     print(a)

# for i in range(10):
#     func()
# print(a)

# 리스트 지역변수 전역변수
# array = [1,2,3,4,5,6]

# def func():
#     array.append(7)
#     print(array)
# func()

# 람다표현식
# def add(a,b):
#     return a+b

# # 일반적인 add 메서드 사용
# print(add(3,7))

# # 람다 표현식으로 구현한 add() 메서드
# print((lambda a,b : a+b)(3,7)

# 내장함수에서 람다 표현 사용
# array = [("홍길동",50),("이순신",32),("아무개",74)]

# def my_key(x):
#     return x[1]

# print(sorted(array,key=my_key))
# print(sorted(array,key=lambda x:x[1]))

# 여러개이ㅡ 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result=map(lambda a,b : a+b , list1,list2)
print(list(result))