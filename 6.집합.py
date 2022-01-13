#집합 자료형은 집합 내의 중복을 허용하지 않는다. 그리고 순서의 개념이 없다./ 리스트or튜플 = 순서있음 but 딕셔너리, 집합은 순서없다

#집합의 형태

# s1 = set([1,2,3])           #집합을 만들때는 set함수를 쓰고 출력시 {}로 출력된다.
# print(s1)

# s2 = set("Hello")           #집합은 집합 내의 중복으로 표시하지 않습니다.
# print(s2)

####

#집합에 순서를 부여하려면? 리스트화 혹은 튜플화 시켜줘야함 >> 인덱싱을 할 수 있게 된다. / list() or tuple()

# s1 = set([1,2,3]) 
# i = list(s1)
# print(i)

# s2 = set([4,5,6])
# j = tuple(s2)            
# print(j)

####

#집합의 교집합 차집합 합집합

#교집합 / s1 & s2 or s1.intersections2

# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# # print(s1 & s2)              # &를 통해서 집합끼리의 교집합을 구함

# print(s1.intersection(s2))     # 집합.intersection(다른집합) 으로도 교집합 생성가능

#합집합 / s1|s2 or s1.union(s2)

# print(s1|s2)
# print(s1.union(s2))             # 두가지 방법 모두로 합집합 가능

#차집합 / s1 - s2 or s1.difference(s2)

# print(s1 - s2)
# print(s1.difference(s2))        # 두가지 방법 모두로 차집합 가능

####

#집합 자료형 관련 함수들

#값 1개 추가하기 s1.add
# s1 = set([1,2,3])
# s1.add(4)
# print(s1)

#값 여러 개 추가하기 s1.update([])
# s1 = set([1,2,3])
# s1.update([4,5,6])
# print(s1)

#특정값을 제거하기 s1.remove([])
# s1 = ([1,2,3])
# s1.remove(2)
# print(s1)

####