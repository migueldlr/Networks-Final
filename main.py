import strats, random, inspect
from player import Player

NUM_ROUNDS = 20

## Get names/functions from strats
s = inspect.getmembers(strats, inspect.isfunction)
names = [x[0] for x in s]
functions = [x[1] for x in s]

## Initialize Player objects
players = [Player(names[i], functions[i]) for i in range(len(names))]

for p1 in players:
	for p2 in players:
		for p3 in players:
			# print(p3.name)
			p1h = []
			p2h = []
			p3h = []

			for i in range(NUM_ROUNDS):
				p1m = p1.nextMove(p1h, p2h, p3h)
				p2m = p2.nextMove(p2h, p3h, p1h)
				p3m = p3.nextMove(p3h, p1h, p2h)

				p1h.append(p1m)
				p2h.append(p2m)
				p3h.append(p3m)

			# print(p1h, p2h, p3h)

