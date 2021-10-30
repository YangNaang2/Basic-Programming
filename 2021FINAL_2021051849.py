################################################
# [CSE1017] Programming Languages - 2021 Spring
#
#   Final Term.
#
# sid  : 2021051849
# name : 양진우
#
################################################

import final_aux

name = "양진우"
sid = 2021051849
final_aux.verify(sid, name)

################################################
# [10] 1. 카이사르 암호법
################################################

# [5] 1.1 암호화
def encrypt(s):
    code = ""
    for i in range(len(s)):
        if s[i].isupper():
            code+=chr((ord(s[i])-ord('A')+2)%26+ord('A'))
        elif s[i].islower():
            code+=chr((ord(s[i])-ord('a')+2)%26+ord('a'))
        elif s[i].isspace():
            code+=" "
        elif s[i]==('.'):
            code+="."
    return code

# [5] 1.2 복호화
def decrypt(s):
    answer = ""
    for i in range(len(s)):
        if s[i].isupper():
            answer+=chr((ord(s[i])-ord('A')-2)%26+ord('A'))
        elif s[i].islower():
            answer+=chr((ord(s[i])-ord('a')-2)%26+ord('a'))
        elif s[i].isspace():
            answer+=" "
        elif s[i]==('.'):
            answer+="."
    return answer

################################################
# [20] 2. 카이사르 암호법의 확장
################################################

# [10] 2.1 암호화 확장
def encryptE(s):
    code = ""
    for i in range(len(s)):
        if s[i].isupper():
            code+=chr((ord(s[i])-ord('A')+2)%26+ord('A'))
        elif s[i].islower():
            code+=chr((ord(s[i])-ord('a')+2)%26+ord('a'))
        elif s[i].isdigit():
            code+=chr((ord(s[i])-ord('0')+2)%10+ord('0'))
        elif s[i].isspace():
            code+=" "
        elif s[i]==('.'):
            code+="."
    return code

x = encryptE('I love You 3000.')
print(x)

# [10] 2.2 복호화 확장
def decryptE(s):
    answer = ""
    for i in range(len(s)):
        if s[i].isupper():
            answer+=chr((ord(s[i])-ord('A')-2)%26+ord('A'))
        elif s[i].islower():
            answer+=chr((ord(s[i])-ord('a')-2)%26+ord('a'))
        elif s[i].isdigit():
            answer+=chr((ord(s[i])-ord('0')-2)%10+ord('0'))
        elif s[i].isspace():
            answer+=" "
        elif s[i]==('.'):
            answer+="."
    return answer

################################################
# [20] 3. 변종 369 게임
################################################

# [10] 3.1 0보다 큰 정수 n을 입력받아 n 까지의 369 시퀀스를 생성해주는 함수
def seq369(n):
    return None

# [10] 3.2 임의의 리스트를 받아서 369 시퀀스인지를 확인해주는 함수
# ! 입력받은 369 시퀀스는 항상 1에서 시작하지 않음. 0보다 큰 임의의 정수에서 시작할 수 있음
def checkSeq369(ns):
    return False

################################################
# [25] 4. 넷이서 했던 007빵!
################################################

# [15] 4.1 한 라운드에서 패배한 플레이어를 리턴해주는 함수
def round007(rnd):
    return None

# [10] 4.2 여러 라운드의 결과를 리턴해주는 함수
def game007(rnds):
    return None

################################################
# [20] 5. 도서 정리 프로그램
################################################

# [10] 5.1 도서 목록을 입력받아 출력하는 함수
def printBooks(books):
    pass

# [10] 5.2 도서 목록을 정렬해서 리턴해주는 함수
def sortBooks(books):
    return None

