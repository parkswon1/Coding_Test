import sys

N = int(sys.stdin.readline())
student = [[] for i in range(200)]
for n in range(N):
    num, name = sys.stdin.readline().split()
    student[int(num)-1].append(name)

for i in range(200):
    for output in student[i]:
        print(i+1,output)