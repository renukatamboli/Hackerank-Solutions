k = int(raw_input())
rooms = map(int,raw_input().split())
from collections import Counter
roomcout = Counter(rooms)
print(roomcout.most_common()[-1][0])
