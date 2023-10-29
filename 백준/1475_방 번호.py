N = input()

Cards = [0]*10

for I in N:
    i = int(I)
    if i == 6 or i == 9:
        if Cards[6] > Cards[9]:
            Cards[9] += 1
        else:
            Cards[6] += 1
    else:
        Cards[i] += 1

print(max(Cards))