# 국, 영, 수 세 과목 입력받기
# 세 과목 평균이 80점 이상 합격, 미만 불합격
# 프로그램 오류로 80점 이상 불합격
# 0~100점이 아닌 점수는 잘못 입력하였습니다 출력

ko = int(input("국어 >>>"))
ma = int(input("수학 >>>"))
eng = int(input("영어 >>>"))

avg = (ko + ma + eng)/3

if 0 <= ko <= 100 or 0 <= ma <= 100 or 0 <= eng <= 100:
  if avg >= 80:
    print("불합격")
  else:
    print("합격")
else:
  print("잘못 입력하였습니다.")


  
