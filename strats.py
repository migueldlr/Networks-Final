import random

'''
Format:
## Name
## Description
def funcname(h,oh1,oh2):
	Either 'c' or 'd' based on strategy


'''

COOLDOWN = 2
ATHRESH = 10
AINC = 2

## Random
## 50-50
def alwaysrand(h, oh1, oh2):
	return 'c' if random.random() < 0.5 else 'd'

## Cooperate
## Always cooperate
def alwaysc(h, oh1, oh2):
	return 'c'

## Defect
## Always defect
def alwaysd(h, oh1, oh2):
	return 'd'

## Alternate
## Cooperate, then defect, then cooperate, then defect...
def alternate(h, oh1, oh2):
	return 'c' if len(h)%2==0 else 'd'

## Grudger
## Cooperate until one defects, then defect forever
def grudger(h, oh1, oh2):
	return 'd' if ('d' in oh1) or ('d' in oh2) else 'c'

## Grudger2
## Cooperate until both defect, then defect forever
def grudger2(h, oh1, oh2):
	return 'd' if ('d' in oh1) and ('d' in oh2) else 'c'

## AntiGrudger
## Defect until one cooperates, then cooperate forever
def agrudger(h, oh1, oh2):
	return 'c' if ('c' in oh1) or ('c' in oh2) else 'd'

## AntiGrudger2
## Defect until both cooperate, then cooperate forever
def agrudger2(h, oh1, oh2):
	return 'c' if ('c' in oh1) and ('c' in oh2) else 'd'

## RandomTFT
## Choose one of the opponent's choices from last turn
def randomtft(h, oh1, oh2):
	if len(h)!=0:
		return oh1[-1] if random.random()<0.5 else oh2[-1]
	else:
		return 'c'

## Aggravation
## Cooperate. Every time an opponent defects, your aggravation increases.
## When your aggravation level exceeds a value, defect, and aggravation goes down. 
def aggravation(hist, ohist, o2hist):
	global AINC, COOLDOWN, ATHRESH
	alevel = (ohist.count("d") + o2hist.count("d"))*AINC - COOLDOWN*len(hist)
	return "d" if alevel >= ATHRESH else "c"

# ## Envy
# ## Defect when the opponents’ average total score is higher than yours
# def envy(points, opoints, o2points):
# 	return "d" if ((sum(opoints) + sum(o2points))/(len(opoints) + len(o2points))) > (sum(points)/len(points)) else "c"

## Shubik
## Retaliate with single defection but defect for 1 more turn each time another opponent defects when this cooperates
def shuuuubik(hist, ohist, o2hist):
	count = 0
	for i in range(len(ohist)):
		if hist[i] == "c" and (ohist[i] == "d" or o2hist[i] == "d"):
			count += 1
	count -= (len(hist) - ''.join(hist).rfind('c') - 1)
	return "d" if count > 0 else "c"

def pickonetft(hist, ohist, o2hist):
	if len(hist)==0:
		return 'c'
	else:
		return ohist[-1]

def nicexor(hist, ohist. o2hist):
	if len(hist)==0:
		return 'c'
	else:
		return 'd' if (ohist[-1]=='c')!=(o2hist[-1]=='c') else 'c'

def niceor(hist, ohist. o2hist):
	if len(hist)==0:
		return 'c'
	else:
		return 'd' if (ohist[-1]) or o2hist[-1] else 'c'

