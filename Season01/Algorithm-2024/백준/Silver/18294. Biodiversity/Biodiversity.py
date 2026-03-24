from collections import Counter

N = int(input())
animals = [input().strip() for _ in range(N)]

cnt = Counter(animals)
top_anm , top_cnt = cnt.most_common(1)[0]

total_cnt = sum(cnt.values())
rst_cnt = total_cnt - top_cnt

if top_cnt > rst_cnt:
    print(top_anm)
else:
    print('NONE')