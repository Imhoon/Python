num = []
arr = [13,24,53,5]

def insert(pos, item): #삽입하는 함수
    num.insert(pos, item)

def delete(pos): #삭제하는 함수
    return num.pop(pos)
def getEntry(pos): #pos에 있는 값을 반환하는 함수
    return num[pos]

def isEmpty(): #리스트가 공백인지 확인 하는 함수
    return

def size(): #리스트의 크기를 반환하는 함수
    return len(num)
    
def merge(arr): #병합, 확장하는 함수  
    num.extend(arr)
def display(msg='배열리스트:'):#출력: 기본값(default)인수사용
    print(size(),num)         #메세지 + 크기+배열의 내용 출력
    
display('파이썬으로 리스트로 구현한 리스트 확인')
print('리스트 공백인지 확인:',isEmpty())

insert(0,10); insert(0,20); insert(1,30)
insert(size(),40); insert(2,50)
display('파이썬 리스트로 구현한 List (삽입*5)')

num.sort()
display('파이썬 리스트로 구현한 List(정렬 후)')

delete(3); delete(size()-1); delete(0)
display('파이썬 리스트로 구현한 List(삭제 후')

merge(arr)
display('파이썬 리스트로 구현한 List(병합 후)')
