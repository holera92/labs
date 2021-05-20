def getNumbers():
    return 37

def get_k():
    return 12

count = {}
roundAppear = {}
for i in range(getNumbers()):
    count[i] = roundAppear[i] = 0

highestNumber = roundNow = reds = blacks = 0
while (True):
    roundNow += 1
    inpt = int(input())
    if inpt < 0:
        break

    count[inpt] += 1
    roundAppear[inpt] = roundNow
    
    highestNumber = max(count.values())
    for i in range(getNumbers()):
        if count[i] == highestNumber:
            print(i, end = ' ')
    print()

    for i in range(getNumbers()):
        if roundAppear[i] == 0 or roundNow-roundAppear[i]>get_k():
            print(i, end = ' ')
    print()

    if inpt != 0:
        if inpt <= 10 or (inpt > 18 and inpt <= 28):
            if inpt % 2 == 1: reds += 1
            else:             blacks += 1
        else:
            if inpt % 2 == 0: reds += 1
            else:             blacks += 1

    print(reds,blacks,'\n')
