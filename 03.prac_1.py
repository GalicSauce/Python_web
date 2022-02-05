# 로또 예상번호 추출 프로그램
'''
1. 로또 번호 6개 생성
2. 로또 번호는 1~45까지의 랜덤한 번호
3. 6개 숫자 모두 달라야함
'''

import random


def getRandomNumber() :
  number = random.randint(1, 45)
  return number

list = []

count = 0 # 현재 뽑은 숫자 개수

while True:
  if count == 6:
    break
  random_num = getRandomNumber()
  if random_num not in list:
    list.append(random_num)
    count += 1


list.sort()
for num in list:
  print(num, end=" ") # 대괄호 없애기





'''
랜덤수 생성 함수 정의
6번 생성
리스트에 저장
6개 번호 다 다른지 조건문으로 확인
'''