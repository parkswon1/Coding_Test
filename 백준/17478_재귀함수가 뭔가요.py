number = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
string1 =['"재귀함수가 뭔가요?"',
      '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
      '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
      '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."']
string2 =['"재귀함수는 자기 자신을 호출하는 함수라네"']
string3 =['라고 답변하였지.']
for i in (range(number)):
    line ="_"*4*i
    for j in range(len(string1)):
        print(f"{line}{string1[j]}")
i +=1
line ="_"*4*i
print(f"{line}{string1[0]}")
print(f"{line}{string2[0]}")
while i >=0:
    line ="_"*4*i
    print(f"{line}{string3[0]}")
    i -=1