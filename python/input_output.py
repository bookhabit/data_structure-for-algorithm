# 입출력 예시
# 학생의 성적 데이터가 주어지고 , 이를 내림차순으로 정렬한 결과를 출력하는 프로그램
# n = input()

# score = input().split()  # 여러 개의 문자열을 공백을 기준으로  입력받음
# data = list(map(int,input().split()))  # 공백을 기준으로 문자열을 입력받아 한번에 정수로 변환

# score.sort(reverse=True)
# print(score)
# print(data)

# 빠르게 입력받기 sys라이브러리 사용
# import sys

# data = sys.stdin.readline().rstrip()
# print(data)

# 출력 print()함수
# a = 1
# b = 2
# print(a,b)
# print(7,end=" ")

# answer = 7
# print("정답은"+str(answer)+"입니다.")

answer = 7
print(f"정답은 {answer}입니다.")