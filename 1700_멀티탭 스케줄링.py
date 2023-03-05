import sys
N, K = list(map(int,sys.stdin.readline().split()))

sequence = list(map(int,sys.stdin.readline().split()))
plug = []
count = 0
output = 0

for i in range(len(sequence)):
    if sequence[i] not in plug:
        if len(plug) < N:
            plug.append(sequence[i])
        else:
            if i+N < len(sequence):
                for p in range(len(plug)):
                    if plug[p] not in sequence[i+1:i+N]:
                        plug[p] = sequence[i]
            elif i+1 < len(sequence):
                for p in range(len(plug)):
                    if plug[p] not in sequence[i+1:len(sequence)]:
                        plug[p] = sequence[i]
            output += 1
                
print(output)