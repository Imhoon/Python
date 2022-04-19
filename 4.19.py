f = open("새파일.text",'w')
#'r' : read읽기모드/ 'w': write 쓰기 모드
#'a' : add 추가 모드 -
# 파일의 마지막에 새로운 내용 추가시킬때

for i in range(10):
    i+=1
    f. write(str(i)+"번째 줄입니다.")
#파일 객체 = open(파일 이름, 파일 열기모드)
f.close()
