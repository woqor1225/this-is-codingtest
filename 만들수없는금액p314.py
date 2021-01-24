n = int(input())

money = list(map(int,input().split()))
money.sort()

target = 1 

for i in money:
    #만들수 없는 금액을 찾았을때 반복 종료
    if target < i:
        break
    target += i #target에 수를 더해준다

print(target)

