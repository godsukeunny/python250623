#DemoStr.py

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(strA.capitalize())  # 첫 글자 대문자
print(len(strA))  # 문자열 길이
print(len(strB))  # 문자열 길이
print("mbc2580".isalnum())  # 알파벳과 숫자로만 구성되어 있는지 확인
print("2580".isdecimal())  # 숫자로만 구성되어 있는지 확인

data = "<<<  spam and ham  >>>"
result = data.strip("<> ")  # 양쪽 공백 제거
print(data)  # "<<<  spam and ham  >>>"
print(result)  # "spam and ham" 
result2 = result.replace("spam", "spam egg")  # 문자열 치환
lst = result2.split()  # 공백을 기준으로 분리
print(lst)  # ['spam', 'egg', 'and', 'ham']
print(" ".join(lst))  # 리스트를 문자열로 합치기

#정규 표현식을 사용
import re

result = re.search("[0-9]*th", "   35th")
print(result)
print(result.group())  # '35th'

# result = re.match("[0-9]*th", "    35th")
# print(result)
# print(result.group())  # '35th'

