# 두 자연수 a,b에 대하여 (a>b ) a를 b로 나눈 나머지를 R이라고 하자
# 이때 a와 b의 최대공약수는 b와 R 의 최대 공약수와 같다
# 최대공약수 영어로 GCD(greatest common divisor)
def gcd(a,b):
    if a%b == 0: # a를 b로 나눈 나머지가 0 이라면 ( a가 b의 배수라면 ) b를 반환
        return b
    else:
        return gcd(b , a % b)  # b와 a를 b로 나눈 나머지(한층 더 작은 수의 최대공약수)를 반환
print(gcd(192,162))