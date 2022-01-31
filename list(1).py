# 1. 리스트 마지막에 데이터 9 추가
# 2. 데이터 40을 50으로 변경
# 3. 3번부터 6번까지 데이터 슬라이싱
# 4. 데이터를 오름차순으로 정렬


result = [33, 40, 12, 63, 52]

result.append(9)
print(result)

result[1] = 50
print(result)

print(result[2:6])

result.sort()
print(result)