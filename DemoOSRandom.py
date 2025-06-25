# DemoOSRandom.py
import random

print(random.random())  # 0.0 ~ 1.0 사이의 실수
print(random.random())  # 
print(random.uniform(2, 5)) 
print(random.uniform(2, 5)) 

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print("----- 샘플링 ----")  
print(random.sample(range(20), 10))  # 0 ~ 19 
print(random.sample(range(20), 10))  # 0 ~ 19 

# 파일명 다루기
from os.path import *

#raw string notation : r
fileName = r"c:\python310\python.exe"

if exists(fileName):
    print("파일이 존재합니다.")
    print("파일크기:", getsize(fileName))  # 파일명
else:
    print("파일이 존재하지 않습니다.")


print("절대경로:", abspath("python.exe"))  # 절대경로
print("파일명만:", basename(fileName))  # 

# 운영체제정보
import os
print("운영체제:", os.name)  # 운영체제 이름
print("환경변수:", os.environ)  # 현재 작업 디렉토리
# os.system("notepad.exe")  # 메모장 실행

# 특정 폴더의 파일 리스트
import glob

result = glob.glob("c:\\work\\*.py")  # c:\work 폴더의 모든 파이썬 파일
for item in result:
    print(item)  # 파일명 출력



