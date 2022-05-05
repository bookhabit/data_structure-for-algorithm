# 팩토리얼 구현


# 반복문으로 구현
def factorial_iterative(n):
    result=1
    # n부터 1까지 차례대로 곱하기
    for i in range(1,n+1):
        result *= i
    return result
print(factorial_iterative(5))

# 재귀적으로 구현
def factorial_recursive(n):
    if n<= 1 : # n이 1 이하인 경우 1 반환
        return 1
    # n! = n * (n-1) 팩토리얼 식을 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)  # 자기자신보다 1 작은 만큼의 팩토리얼을 호출한 값을  곱한 결과를 반환
print(factorial_recursive(5))
