#알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어짐
#이떄 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤
#그 뒤에 모든 숫자를 더한 값을 이어서 출력

# 내가 짠 코드
import re

a = input()

numbers = re.findall('\d', a)
alphas = alphas = re.findall('[A-Z]', a)
num=[]

# 문자리스트 알파벳 오름차순 정렬
alphas.sort()

# 숫자리스트를 숫자로 변환해서 새로운 숫자리스트 만듬
for i in numbers:
    num.append(int(i))
# 숫자합계 추출
num_sum = sum(num)

# 문자리스트에 숫자합계 추가 
alphas.append(str(num_sum))

# 문자열을 string으로 변환해서 출력
alphas = "".join(alphas)
print(alphas)

print("------답안코드------")

# 답안 예시
s =input()
stringList =[]
sum = 0
for i in s:
    # 알파벳인 경우 리스트 삽입
    if i.isalpha():
        stringList.append(i)
    # 숫자는 따로 더하기
    else:
        sum += int(i)
# 알파벳 오름차순 정렬
stringList.sort() 
# 숫자가 하나라도 존재하면 가장 뒤에 삽입
if sum != 0 :
    stringList.append(str(sum))

# 최종결과 출력 ( 리스트를 문자열로 변환하여 출력)
print("".join(stringList))
