##################################################################################
# 3-Player Axelrod's Tournament                                                  #
# MA468 Networks - D Block                                                       #
# Miguel de los Reyes, Angela Deng, Nikhil Reddy, Sreeram Venkat                 #
# May 2017                                                                       #
##################################################################################

import random, inspect

## Import our stuff
import strats
from player import Player

NUM_ROUNDS = 20

## Get names/functions from strats
s = inspect.getmembers(strats, inspect.isfunction)
names = [x[0] for x in s]
functions = [x[1] for x in s]

## Initialize Player objects
players = [Player(names[i], functions[i]) for i in range(len(names))]

## Print some information
print("3-Player Axelrod's Between {} Strategies, {} Rounds/Game".format(len(players), NUM_ROUNDS))


def getscores(p1h, p2h, p3h):
	t1 = 0
	t2 = 0
	t3 = 0
	for i in range(NUM_ROUNDS):
		s = getscore(p1h[i], p2h[i], p3h[i])
		t1 += s[0]
		t2 += s[1]
		t3 += s[2]
	return (t1, t2, t3)

def getscore(m1, m2, m3):
	res = (m1, m2, m3)
	if res.count('c')==3:
		return (6,6,6)
	elif res.count('c')==2:
		return (2+(res[0]!='c')*7, 2+(res[1]!='c')*7, 2+(res[2]!='c')*7)
	elif res.count('c')==1:
		return ((res[0]!='c')*4, (res[1]!='c')*4, (res[2]!='c')*4)
	else:
		return (2,2,2)

		
def play(p1, p2, p3):
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

	return getscores(p1h, p2h, p3h)

def updateresults(p1, p2, p3, scores):
	p1.pf += scores[0]
	p2.pf += scores[1]
	p3.pf += scores[2]

	p1.pa += (scores[1]+scores[2])
	p2.pa += (scores[0]+scores[2])
	p3.pa += (scores[0]+scores[1])


	# Increment wins and losses
	# This might have problems?
	if scores[0]>scores[1] and scores[0]>scores[2]: # p1 wins
		p1.w += 1
		p2.l += 1
		p3.l += 1
	elif scores[1]>scores[0] and scores[1]>scores[2]: # p2 wins
		p1.l += 1
		p2.w += 1
		p3.l += 1
	elif scores[2]>scores[0] and scores[2]>scores[1]: # p3 wins
		p1.l += 1
		p2.l += 1
		p3.w += 1
	elif scores[0]==scores[1] and scores[0]>scores[2]: # p1p2 tie
		p1.t += 1
		p2.t += 1
		p3.l += 1
	elif scores[1]==scores[2] and scores[1]>scores[0]: # p2p3 tie
		p1.l += 1
		p2.t += 1
		p3.t += 1
	elif scores[0]==scores[2] and scores[2]>scores[1]: # p1p3 tie
		p1.t += 1
		p2.l += 1
		p3.t += 1
	else: # 3-way tie
		p1.t += 1
		p2.t += 1
		p3.t += 1



for p1 in players:
	for p2 in players:
		for p3 in players:
			s = play(p1,p2,p3)
			updateresults(p1,p2,p3,s)

players = sorted(players, key=lambda p: p.pf, reverse=True)

for p in players:
	print(p)
