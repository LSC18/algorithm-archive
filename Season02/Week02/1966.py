# BOJ 1966 프린터 큐
# 날짜: 2026-04-01
# 분류: 큐, 덱, 시뮬레이션
# 핵심 아이디어:
# - (인덱스, 중요도) 형태로 큐 구성하여 특정 문서 추적
# - popleft로 현재 문서를 꺼낸 뒤
# - 큐 내부에 더 높은 중요도가 존재하면 다시 append
# - 없으면 출력 처리하며 count 증가
# - M번째 문서가 출력되는 순서를 반환
# 시간복잡도: O(N^2)

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    s = list(map(int, input().split()))
    
    # (인덱스, 중요도) 형태로 변경
    s = deque((i, s[i]) for i in range(N))
    
    cnt = 0
    
    while True:
        cur = s.popleft()   # 현재 문서 (인덱스, 중요도)
        
        # 뒤에 더 큰 중요도가 있는지 확인
        if any(cur[1] < x[1] for x in s):
            s.append(cur)   # 있으면 뒤로
        else:
            cnt += 1        # 없으면 출력
            
            if cur[0] == M: # 우리가 찾는 문서면
                print(cnt)
                break
