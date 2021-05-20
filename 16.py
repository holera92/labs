n = (int(input()))
result = []
tickets = input().split()
for i in range(0, n):
    if tickets[i].startswith('a') and tickets[i].endswith('55661'):
        result.append(tickets[i])

if len(result) == 0:
    print(-1)
else:
    print(' '.join(result))
