# 주차 요금 입력 받기
A, B, C = map(int, input().split())

# 각 시간대별 주차된 트럭 수를 기록할 리스트
parking_lot = [0] * 101  # 0~100까지의 시간대

# 각 트럭의 주차 시간 입력 받기
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        parking_lot[i] += 1

# 총 요금 계산
total_fee = 0
for trucks in parking_lot:
    if trucks == 1:
        total_fee += A
    elif trucks == 2:
        total_fee += B * 2
    elif trucks == 3:
        total_fee += C * 3

# 결과 출력
print(total_fee)