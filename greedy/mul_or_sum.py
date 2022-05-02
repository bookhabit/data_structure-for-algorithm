# 각 자리가 숫자(0부터9)로만 이루어진 문자열 S가 주어졌을 때 , 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 ‘x’ 혹은 ‘+’ 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요 . 

# 단, + 보다 x를 먼저 계산하는 일반적인 방식과는 달리

# 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

# 예를 들어 02894라는 문자열로 만들 수 있는 가장 큰 수는 ((((0+2)x9)x8)x4)=576 입니다.

# 또한 만들어질 수 있는 가장 큰 수는 항상 20억이하의 정수 입력됨

# 내가 짠 코드

s = input()
result = 0
for i in s :
    i = int(i)
    if i <= 1 :  #i가 1 이하일 때 더하기해줌
        result += i
        # i가 1 이하일 때 더하기해준 코드로 첫번째 숫자가 0일 때 result에 0이 들어가있으니 곱하면 안되니까 > 다음 i를 더해줌
    elif result == 0 :
        result += i
    else:
        result *= i
print(result)

# 답안 예시
data = input()

# 첫번쨰 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1,len(data)):
    # 두 수 중에서 하나라도 0 혹은 1 인경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num
print(result)