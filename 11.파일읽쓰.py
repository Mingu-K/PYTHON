# 파일객체 = open(파일이름, 파일 열기 모드)
# f = open('새파일.txt','w') #여기서 f는 파일 객체로 다른 말로 설정가능
# f.close()
# 열기모드는 r,w,a가 있다 r은 읽기, w는 쓰기,a는 추가모드(마지막에 새로운 내용추가)
# 쓰기모드로 열면 이미 존재했던 내용 다 지워짐, 없던 파이면 새로 만듦

# f = open('새파일.txt','w')
# for i in range(2,10,1):
#     for j in range(1,10,1):
#         f.write(f"{i}*{j}={i*j}\t") #파일에 값을 입력할 때 print가 아닌 write를 사용한다.
#     f.write('\n')#위의 \t 는 j의 값이 변할 때마다 뛰고 \n은 i의 값이 변할 때마다 개행
# f.close()

#프로그램 읽기
#readline 맨 위에 한줄을 읽어온다
# f = open('새파일.txt','r')
# line = f.readline()
# print(line)
# f.close()

#모든 줄 읽기
# f=open('새파일.txt','r')
# while True:
#     line = f.readline()
#     if line == "":break
#     print(line)
# f.close()
 
 #readlines 함수/ 이 함수는 모든 줄을 읽어서 각각의 줄을 리스트로 돌려줌
# f = open('새파일.txt','r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

#read 함수 사용하기 #read는 파일 내용 전체를 문자열로 돌려줌
# f = open('새파일.txt','r')
# data = f.read()
# print(data)
# f.close()

#파일 내용 추가하기
#쓰기모드 w를 사용하면 내용 전체가 없어지므로 추가할때 a모드를 사용하자
# f = open('새파일.txt','a')
# for x in range(11,20,1):
#     for y in range(1,10,1):
#         f.write(f"{x}*{y}={x*y}\t")
#     f.write("\n")
# f.close()

#with문과 함께 사용하기