#if의 조건문 표현식
# i = [43,123,32,12]
# # for j in range(0,4,1):
# #     if i[j] >= 60:
# #         message = "success"
# #     else:
# #         message = 'failure'
# #     print(message)
# for j in range(4):
#     message = "success" if i[j] >= 60 else "failure"
#     print(message)

# 출력하고자 하는 결과물\if조건\else출력물

####

#for 반복문의 다양한 쓰임

# a = [(1,2),(3,4),(5,6)]
# for (first, last) in a:     #리스트를 반복문에 포함시킬 수 있다.
#     print(first + last)
    
# marks = [90,25,67,45,80]

# for mark in marks:
#     if mark>=60:
#         print("합겨그")
#     else:
#         print("불합격")     
        
# # for 문의 list comprehension 리스트 내포
# a = [1,2,3,4]
# result = [num * 3 for num in a if num % 2 ==0]
# print(result)
# 리스트 만든 후 결과를 출력할 변수를 입력 한칸 띄고 for 문 후 if절이 있으면 if까지 뚝딱