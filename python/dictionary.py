data =dict()
data['사과'] ="Apple"
data["바나나"] = "Banana"
data["코코넛"] = "Coconut"

# if "사과" in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다")

# 키 데이터만 담은 리스트
# key_list = data.keys()
# 값 데이터만 담은 리스트
# value_list = data.values()

# dict_keys([~~])  객체안에 리스트 형식으로 반환됨
# print(key_list)
# print(value_list)

# 리스트로 형변환해서 주로 사용
key_list = list(data.keys())
value_list = list(data.values())
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])


# 딕셔너리

