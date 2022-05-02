# # 1부터 9까지 모든 정수의 합 구하기 - while문
# i = 1
# result =0
# while i<=9:
#     result+=i
#     i += 1
# print(result)

# # # 1부터 9까지 홀수의 합 구하기 - while문
# i = 1
# result = 0
# while i <= 9 :
#     if i%2 ==1 :
#         result += i
#     i+=1
# print(result)


# # 1부터 9까지 모든 정수의 합 구하기 - for문
# result =0 
# for i in range(1,10):
#     result += i
# print(result)

# continue 사용한 1부터 9까지의 홀수 합 구하기
# result =0
# for i in range(1,10) :
#     if i %2 == 0 :
#         continue
#     result += i
# print(result)

# arr = [9,8,7,6,5]
# for i in arr:
#     print(i)

# 리스트 컴프리헨션
# print([i for i in range(1,10)])


# break 키워드
# i = 0
# while True:
#     print(f'현재 i의 값 : {i}')
#     if i == 5:
#         break
#     i+=1

# 점수가 80점 넘으면 합격
score =[90,85,77,65,97]

# for i in score:
#     if i >= 80:
#         print("합격")
#     else:
#         print("불합격")

# for i in range(len(score)):
#     if score[i] >= 80:
#         print(f"{i+1}번쨰 학생 합격")

# 특정 번호의 학생은 제외하기
# cheating_student_list = {2,4}

# for i in range(len(score)):
#     if i+1 in cheating_student_list:
#         continue
#     if score[i] >= 80:
#         print(i+1,"번 학생은 합격") 

# 구구단 - 중첩반복문
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} X {j} = {i*j}")