import sys
length, num = map(int, sys.stdin.readline().rstrip().split(" "))
num_list = []
for i in range(1, length+1):
    num_list.insert(i, i) # 1부터 시작해도 i의 pos는 0임

for j in range (num):
    start, end = map(int, sys.stdin.readline().rstrip().split(" "))
    start-=1
    end-=1
    rep = (end - start+1)//2
    for k in range(rep):
        curr = num_list[start]
        num_list[start] = num_list[end]
        num_list[end] = curr
        start+=1
        end-=1
print(*num_list)