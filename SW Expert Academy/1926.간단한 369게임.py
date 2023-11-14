N = int(input())

output = []
for n in range(1,N+1):
    str_n = str(n)
    count = 0
    for s in str_n:
        if s == '3' or s == '6' or s == '9':
            count += 1

    if count == 0:
        output.append(n)
    else:
        slash = '-' * count
        output.append(slash)

print(*output)