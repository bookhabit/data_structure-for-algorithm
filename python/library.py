# # 자주 사용되는 내장 함수
# result = sum([1,2,3,4,5])
# print(result)

# min(7,4,5,2)  # 최소값 
# max(7,4,5,2)  # 최대갑

# result = eval("(3+5)*7")  # 수식이 있으면 그 수식을 계산해서 수로 반환
# print(result)

#result = sorted(9,1,8,5,4)


# 순열과 조합
# {"A","B","C"}에서 순서를 고려하지 않고 두 개를 뽑는 경우 : 'AB', 'AC' , 'BC'

# from itertools import combinations

# data = ['A','B','C']

# result = list(combinations(data,2))
# print(result)

# collection 라이브러리의 Counter
# from collections import Counter

# counter = Counter(['red','blue','red','green','blue','blue'])

# print(counter['blue'])
# print(counter['green'])
# print(dict(counter))

# math 라이브러리의 최대 공약수 최소 공배수
import math

# 최소 공배수
def lcm(a,b):
    return a*b // math.gcd(a,b)

a= 21
b = 14

print(math.gcd(21,14))  # 최대 공약수 gcd 계산
print(lcm(21,14))  # 최소 공배수 lcm 계산