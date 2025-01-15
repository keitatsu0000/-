from collections import deque

INF = (1 << 30)
h, w, d = map(int, input().split())
s = [input() for i in range(h)]

# 隣接するマスのパターン
di = [1, 0, -1,  0]
dj = [0, 1,  0, -1]

que = deque()
dist = [[INF for _ in range(w)] for _ in range(h)] # 加湿器から各マスまでの最短移動回数
for i in range(h):
    for j in range(w):
        if s[i][j] == 'H':
            que.append((i, j))
            dist[i][j] = 0
while que:
    now_i, now_j = que.popleft()

    for direction in range(4):
        next_i = now_i + di[direction]
        next_j = now_j + dj[direction]
        if 0 <= next_i < h and 0 <= next_j < w and dist[next_i][next_j] == INF and s[next_i][next_j] != '#':
            que.append((next_i, next_j))
            dist[next_i][next_j] = dist[now_i][now_j] + 1

result = 0
for i in range(h):
    for j in range(w):
        if dist[i][j] <= d:
            result += 1

print(result)

# 参考: https://programming-hiroba.com/abc383-c/
