import sys
char = sys.stdin.readline()
link = [['','Lend',1]]
cuser = len(char)
for i in range(0,len(char)):
    link.append([i,char[i],i+2])
i+=1
link.append([i,'Rend',''])
i+=1
M = int(sys.stdin.readline())
for j in range(M):
    command = input().split()
    if command[0] == 'L':
        if link[cuser][1] != 'Lend':
            cuser = link[cuser][0]
    elif command[0] == 'D':
        if link[link[cuser][2]][1] != 'Rend':
            cuser = link[cuser][2]
    elif command[0] == 'B':
        if link[cuser][1] != 'Lend':
            left = link[cuser][0]
            right = link[cuser][2]
            link[left][2]= right
            link[right][0] = left
            cuser = left
    elif command[0] == 'P':
        left = cuser
        right = link[cuser][2]
        i+=1
        link.append([left,command[1],right])
        link[cuser][2] = i
        cuser = i
        link[link[cuser][2]][0] =i

cuser = link[0][2]
string = ''
while(1):
    string = string + link[cuser][1]
    if link[link[cuser][2]][1] == 'Rend':
        break
    cuser = link[cuser][2]
    
print(string.replace("'",""))