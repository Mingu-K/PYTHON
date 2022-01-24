#함수를 만드는 예약어 def
# #매개 변수와 인수의 구분을 잘하자
# def add(a,b):       # a,b는 매개변수= 함수의 입력으로 전달된 값을 받는 변수
#     return(a+b)
# print(add(3,4))     #3,4는 인수 = 함수를 호출할 때 전달하는 입력값

#정의된 함수가 없는데, 함수를 돌리면 none이라고 배출되지만, 이를 결과값이라고 오인하면 안된다.

#입력값이 없는 함수가 있을 수 있다
# def say():
#     print('hi')

# say()

# 매개변수 (parameter)와 인수(arguments)

#함수 def 내에서 add(a,b) 의 ab는 입력값이다. 이를 print(~) 출력하면 결과값이 아닌 수행할 문장을 수행한 것이다.
#결과값은 return으로 표현된 것이 결과값이다.
# 그렇기에 바로 위의 함수는 결과값도 입력값도 없는 함수이다.

# def add(a,b):
    
#함수를 설정한 후 add(3,5) 나 add(a=3,b-=5)로 지정해서 입력해도 가능하다 물론 a,b의 위치가 바뀌어도 괜찮다.

#입력값이 몇개일지 모를 때

# def sum(*args): #*args는 입력값을 모두 튜플로 만들어 준다. args= argument(인수)
#     result = 0
#     for i in args:
#         result = result + i
#     return result
# print(sum(1,2,3,4,5))

#매개변수 **kwargs=키워드파라미터 **kwargs(a=1) 하면 딕셔너리 {'a':1} 로 출력해준다.

#함수의 결과값은 언제나 하나이다.
# def summul(a,b):
#     return a+b,a*b

# print(summul(4,5))
#리턴의 값이 2개처럼 보이지만 2개를 하나로 묶은 튜플의 형태로 출력된다.

#return은 함수 내의 if문에서 break와 같은 역햘을 할 수 있다.
# def snick(nick):
#     if nick == '바보':
#         return
#     print(f"나의 별명은{nick}입니다.")
# snick('띨띨스')

#함수의 초기값, 디폴트값 넣어주기,디폴트 값이 항상 입력값의 가장 오른쪽에 있어야 합니다.
# def int(name,old,man=True): #여기서 True는 FALSE를 입력하지 않는다면 자동으로 나가는 디폴트값
#     if man:
#         return print(f"이름은 {name}이고 나이는 {old}이며 성별은 남자입니다.")
#     else:
#         return print(f"이름은 {name}이고 나이는 {old}이며 성별은 여자입니다.")
# int('강민구',26)

# lambda는 함수를 생성할 때 사용하는 예약어, def와 동일한 역할을 함. def를 사용할 정도로 복잡하지 않고 사용할 수 없는 곳에서 자주 쓰임.
# mul = lambda a,b,c : a*b+c
# print(mul(3,4,5))