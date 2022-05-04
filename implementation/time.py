#정수 N이 입력되면 00시00분00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
# n = int(input())

# sum = 0

# for hour in range(24):
#     if hour == n+1 :  # n시 59분 59초까지 계산하고  그다음 hour부터 break
#         break
#     if hour == 3 or hour == 23:
#         sum +=1
#     for minutes in range(1,60):
#         if minutes == 3:
#             sum +=1
#         for second in range(1,60):
#             if second == 3:
#                 sum +=1
# print(sum)


# 혼자 못풀겠음 > 해설
#------------------------- 답안
# 완전탐색 문제(가능한 경우의 수를 모두 검사해보는 탐색방법)
# 하루는 86,400초이므로 00시00분00초부터 23시59분59초까지의 모든 경우는 86,400가지입니다.  (24*60*60=86,400)
# 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됩니다.
n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)