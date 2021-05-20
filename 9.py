minsInHour = 60

print('В первой строке введите назначенное время вcтречи по паттерну ЧЧ:ММ. C новой строки время прибытия')

h1, m1 = map(int, input().split(sep=':'))
h2, m2 = map(int, input().split(sep=':'))

m1 = minsInHour * h1 + m1
m2 = minsInHour * h2 + m2

m1 = m1 + 15

if m1 > 1439:
    m1 -= 1440
    
if m2 > m1:
    print('Встреча не состоится')
else:
    print('Встреча состоится')
