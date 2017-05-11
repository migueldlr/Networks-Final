import random

'''
Format:
## Name
## Description
def funcname(h,oh1,oh2):
	Either 'c' or 'd' based on strategy


'''

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

