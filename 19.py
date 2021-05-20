def combination(usages, string, result, last, index, repeatLeft):
    
    for k in usages:
        if (usages[k] - 1 > repeatLeft):
            continue
        result[index] = k
        usages[k] += 1
        if last == index:
            print(''.join(result), end=' ')
        else:
            isRepeated = usages[k] > 1
            combination(usages, string, result, last, index+1, repeatLeft - isRepeated)
    
        usages[k] -= 1
    

def start(n, string):

        usages = {}
        result = []

        for _ in range(n):
            result += ' '

        for char in string:
            usages[char] = 0

        combination(usages, string, result, n-1, 0, n - len(string) - 1)
        print()
	

n = int(input())
string = input()

start(n, string)
