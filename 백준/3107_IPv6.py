import sys

IPv6 = list(sys.stdin.readline().rstrip()) + [':']
output = []
stack = []
count = 4
if 7 - (IPv6.count(':') - 1) < 0:
    for i in range(len(IPv6)-2):
        if IPv6[i] == ':' and IPv6[i+1] == ':':
            del IPv6[i]
else:
    plus = [':'] * (7 - (IPv6.count(':') - 1))
    for i in range(len(IPv6)-2):
        if IPv6[i] == ':' and IPv6[i+1] == ':':
            IPv6 = IPv6[:i] + plus + IPv6[i:]
            break

for I in IPv6:
    if I == ':':
        output = output + ['0']*count + stack + [':']
        stack = []
        count = 4
    else:
        stack.append(I)
        count -= 1


print(''.join(output[:-1]))