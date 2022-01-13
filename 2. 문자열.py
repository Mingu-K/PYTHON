'''
문자열로 배출하는 방법

"Hello world"
'Hello world'
"""Hello world"""(작은 따옴표 3개도 가능)

배출 방법이 다양한 이유는 문자열 배출 시 따옴표를 사용할 수도 있기 때문이다.

food = "python's favorite food is perl" 문자열 중간에 ' 가 들어가 있다. 그렇기에 큰 따옴표로 문자열 표시
만약 작은 따옴표로 문자열 표시를 하고 python에 ' 붙였다면 오류가 발생할 것이다.

say = '"python is very easy." he says'
위와 같은 방식으로 인용구를 표현해주었다. ''로 문자열 출력을 입력하고 ""로 문자열내의 인용구 표시를 하였다.

하지만 큰따옴표 내에서 큰따옴표로 작은 따옴표 안에서 작은따옴표를 사용할 수 있는데, 
이는 따옴표 문자열 표시안에서 사용하는 따옴표 앞에 \를 입력하는 것이다.

food = 'python\'s favorite food is perl'
say = "\"python is very easy.\" he says"  이렇게 출력하고자 하는 따옴표 앞에 \' OR \"를 입력해주면 된다.
'''


'''
줄바꿈 코드

multiline = "Life is too short\nYou need python" 출력된 문자열 중간에 \n 을 입력하면 그 부분에서 줄바꿈을 한다.
또는
multiline = \''' #백슬래쉬는 무시해야함
Life is too short
You need python  이와 같은 작은 따옴표 세개로 위아래를 표시하여 줄바꿈을 할 수 있다.
\''' #백슬래쉬는 무시

이스케이프 코드 = 문자열 내에서 사용가능한 코드
\n = 줄바꿈
\t = 문자열 사이에 탭 가격 입력
\\ = \를 그대로 입력하고 싶을때
\' 
\"
'''


'''
문자열 연산하기(더하기 곱하기)

head = "Python"
tail = " is fun"
head + tail = " Python is fun"

a = "python"
a * 2 = "pythonpython"

문자열 길이 구하기
a = "Life is too short"
len(a) = 17 (띄어쓰기 포함)
'''

'''
문자열 인덱싱

인덱싱은 아래 문자열 단어의 번호를 매겨 출력하는 것이다.
a = "Life is too short, You need python"
L은 0번째, i는 1번째, 띄어쓰기도 포함하며, s는 12이다.
a[3]은 e가 출력이된다. # 파이썬은 0부터 숫자를 세는 것을 기억해야한다.

그렇다면 a = [-1]은 무엇을 출력하느가?
a = [-1] 역순으로 python의 n이 출력된다. 맨 뒤에서 첫번째 글자가 출력된다. 
a = [0] == a = [-0] # 0 = -0이라 같은 것이 출력되기 때문에 -1 부터이다.
'''


'''
문자열 슬라이싱

인덱싱은 글자하나를 뽑아내는 것이라면 슬라이싱은 0~3과 같이 일자로 쫙 뽑아내는것.

a = "Life is too shortYou need python"
b = a[0]+a[1]+a[2]+a[3] = 'Life' #인덱스를 활용한 방법
a = [0:4] = 'Life' #슬라이싱을 활용한 방법 

슬라이싱의 a = [0:4] 는 [0] <= a < [4] 의 의미로 0부터 3까지 포함하고 4는 포함하지 않는다. 
물론 공백도 한칸으로 취급한다. a = [0:5] = 'Life '로 출력 

a = [ :4] 나 a = [19: ]로 입력한다면, 숫자가 없는 빈칸은 맨 처음부터 혹은 맨 끝까지의 의미이다.
'''


'''
슬라이싱으로 문자열 나누기

a = "20010331Rainy"
date = a[ : 8]
weather = a[-1:-5] or a[8:]
>> date ='20010331 / wether = 'Rainy'

a = "pithon"
a = [1] . 'i'
a [1] = 'y' 로 입력하면 a = "python"으로 수정됨.
OR
a[ :1 ] + 'y' + a[2: ] = 'python으로 수정됨
'''

'''
문자열 포매팅

숫자
"I eat %d apples." % 3
'I eat 3 apples.'

문자
"I eat %s apples," % "five"
'I eat five apples."

변수에 입력된 숫자
number = 3
"I eat %d apples." % number
'I eat 3 apples."

2개 이상의 값 넣기
number = 3
day = 'three'
"I ate %d apples, so i was sick for %s day." % (number, day)
'I ate 3 apples, so i was sick for three day.'
'''


'''
문자열 포맷 코드
%s = 문자열
%c = 문자 1개
%d = 정수
%f = 부동소수
%o = 8진수
%x = 16진수
%% = 문자 % 그대로 출력

%s의 경우 문자 이외에 정수와 부동소수 모두 입력이 가능하다.

a = "Error is %d%"로 하면 %가 출력이 안된다
a = "Error is %d%%"로 해야 ~%라고 산출이 된다.
'''


'''
포맷 코드와 숫자 함께 사용하기.

정렬과 공백
"%10s" % "hi" >> "        hi" 로 출력된다 10칸 중 맨 오른쪽에 hi입력을 한다. 10칸 중 오른쪽 끝네 hi입력이라는 뜻이다.
"%-10sjane" % "hi" >> "hi        jane"로 출력된다. -10을 사용했기 때문에 좌측 처음에 hi가 입력되고 %-10이 끝나면 jane을 출력한다.

소수점 표현하기
"%0.4f" % 3.42134 >> ' 3.4213으로 출력된다. 소수점 넷째자리 까지만 출련된다. >> .은 소수점을 뒤에 숫자는 자릿수를 뜻한다.
'''


'''
format 함수를 사용한 포매팅

"I eat {0} apples".format(3)
>> "I eat 3 apples"
"I eat {0} apples".format("five")
>> "I eat five apples"

2개 이상의 값

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
>> "I ate 10 apples. so I was sick for three days." format( , )의 순서가 {0}, {1} 순서대로 삽입된다. + 숫자 없을 시 순서대로 입력됨

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3) 로 해도 출력됨

위의 방법과 아래방법을 동시에 섞어서 사용도 가능하다.

정렬

"{0:<10}".format("hi") 화살표 방향쪽으로 붙여서 정렬시키고 10은 10칸이라는 소리이다.
>> 'hi        '
"{0:>10}".format("hi") >방향에 따라 오른쪽으로 붙여서 정렬
>> '        hi'
"{0:^10}".format("hi") ^는 가운데 정렬이다.
>>'    hi    '

hi출력 앞뒤로 공백을 채우기

"{0:=^10}".format("hi") 방향을 나타내는 화살표 앞에 문자를 넣으면 그 문자로 빈 공간을 채워 넣는다.
'====hi===='

소수점 표현하기
y=3.42134234
"{0:0.4f}".fotmat(y)
'3.4213
"{0:10.4f}".fotmat(y)
'    3.4213' . 도 한자리로 생각하고 계산함
"{{ and }}".format()
'{ and }' 로 출력함
'''

'''
f문자열 포맷팅

name = 홍길동
age = 30
f"나의 이름은{name}입니다. 나이는 {age}입니다."
>> '나의 이름은 홍길동입니다. 나이는 30입니다.'
f"나이는 {age + 1}입니다. {}내에서 숫자 계산이 가능하다.
>>나이는 31입니다.

f문자열 포맷팅의 key 와 value

d = {'name' : '홍길동', 'age' : 30}
f"나의 이름은{d['name']}입니다. 나이는 {d[age]}입니다."
>> '나의 이름은 홍길동입니다. 나이는 30입니다.'

정렬
f"{"hi":>10}" 위의 포맷코드와 ㅉ똑같다.
'        hi'
'''


'''
문자열 관련 함수

문자 개수 세기 (count)
a = "hobby"
a.count('b') = 2 문자 중 b의 갯수를 구해준다.

위치 알려주기1(find)
a = "python is the best choice"
a.find('b') = 14(14번째에 있다)
a.find('k') = -1 > -1은 존재하지 않다는 것을 의미한다.

위치알려주기2(index)
a = "python is the best choice"
a.index('b') = 14
a.find('k') = 존재하지 않는 문자를 찾을 때는 find가 -1을 출력한 것과 달리 에러가 발생하여 아무 값도 출력하지 못함.

문자열 삽입(join)
",".join('abcd')
'a,b,c,d'
or
",",join(['a','b','c','d']) >> join함수는 리스트나 튜플도 입력가능하다.
'a,b,c,d'

소문자를 대문자로 바꾸기
a = "hi"
a.uppear()
"HI"

대문자를 소문자로 바꾸기
a = 'HI'
a.lower()
'hi'

왼쪽 공백지우기 = .lstrip()
오른쪽 공백지우기 = .rstrip()
양쪽 공백지우기 = .strip()

문자열 바꾸기
a = "Life is too short"
a.replace("Life", "Your leg")
'Your leg is too short'

문자열 나누기
a = "Life is too short"
a.split()
['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':')
['a','b','c','d']
'''

#git이 잘 연결되었는가?  어떻게 새로 올리는가?
# git add . 하면 추가됨
