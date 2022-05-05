# 재귀함수
# 종료조건 없는 재귀함수 - 무한루프처럼 반복되다가 최대재귀깊이 초과로 프로그램종료됨
def recursive_funtion():
    print("재귀 함수 호출")
    recursive_funtion()

recursive_funtion()

# 종료조건 명시한 재귀함수
def recursive_funtion(i):
    # 100번째 호출했을 때 종료되도록 조건 명시
    if i == 10:
        return  # return 문으로 종료시킨다
    print(i,"번째 재귀함수에서",i+1,"번쨰 재귀함수 호출")
    recursive_funtion(i+1)
    print(i,"번째 재귀함수 종료")

recursive_funtion(1)
