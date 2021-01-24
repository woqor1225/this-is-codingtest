############################################ 내가 푼거 
n, m = map(int,input().split())

ball = list(map(int,input().split()))

cnt = 0

for i in range(n):
    for j in range(i + 1, n):
        if ball[i] != ball[j]:
            cnt += 1

print(cnt)
#/////////////////////////////////////////////////// 책에 있는것
n, m = map(int,input().split())

data = list(map(int,input().split()))

result = 0

array = [0] * 11

for x in data:
    array[x] += 1

print(array)

for i in range(1, m + 1):
    n -= array[i]
    print(n, array[i])
    result += array[i] * n

print(result)
