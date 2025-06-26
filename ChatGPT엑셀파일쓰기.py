# chatgpt-excel-파일쓰기.py

import openpyxl as op
import random

# 워크북 및 시트 생성
wb = op.Workbook()
ws = wb.active
ws.title = "전자제품목록"

# 헤더 작성
ws.append(["제품ID", "제품명", "가격", "수량"])

# 샘플 제품명 리스트
product_names = [
    "노트북", "스마트폰", "태블릿", "모니터", "키보드",
    "마우스", "프린터", "스피커", "헤드폰", "웹캠"
]

# 100개 데이터 생성 및 추가
for i in range(1, 101):
    pid = i
    name = f"{random.choice(product_names)}_{i}"
    price = random.randint(50000, 2000000)
    qty = random.randint(1, 100)
    ws.append([pid, name, price, qty])

# 파일 저장
wb.save("ProductList.xlsx")
