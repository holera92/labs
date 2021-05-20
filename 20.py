class Drink:
    def __init__(self):
            self.price  = 0.0
            self.volume = 0.0
            self.name   = ""

balance = int(input())
drinkAmount = int(input())

best = Drink()
_input = Drink()

for i in range(drinkAmount):
	row = input().split()
	_input.name   = row[0]
	_input.price  = int(row[1])
	_input.volume = int(row[2])

	liters = (balance // _input.price) * _input.volume
	if liters == 0:
		continue
	
	if best.price == 0:
		best = _input
		continue
	
	bestLiters = (balance // best.price) * best.volume
	if liters > bestLiters:
		best = _input

if best.price == 0:
	print(-1)
else:
    bottles = balance // best.price
    print("{} {}\n{}\n{}".format(best.name, bottles, bottles * best.volume, balance - best.price * bottles))