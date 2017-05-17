import random
import main
import bm
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

cooldown = 2
athresh = 10
ainc = 2


def aggro(hist, ohist, o2hist):
    alevel = (ohist.count("d") + o2hist.count("d"))*ainc - cooldown*len(hist)
    return "d" if alevel >= athresh else "c"

def shubik(hist, ohist, o2hist):
    count = 0
    for i in range(len(ohist)):
        if hist[i] == "c" and (ohist[i] == "d" or o2hist[i] == "d"):
            count += 1
    count -= (len(hist) - ''.join(hist).rfind('c') - 1)
    return "d" if count > 0 else "c"

def envy(hist, ohist, o2hist):
    points, opoints, o2points = main.getscores(hist, ohist, o2hist)
    return "d" if ((sum(opoints) + sum(o2points))/(len(opoints) + len(o2points))) > (sum(points)/len(points)) else "c"

def payoffHistory(hist, ohist, o2hist):
    if len(hist)<6:
        return "c" if len(hist)%2 == 0 else "d"
    plist = []
    for j in range(len(hist)):
        plist[j] = main.getscore(hist[j], ohist[j], o2hist[j])[0]
    cpts = sum(list(filter(lambda x: hist[plist.index(x)] == "c", plist)))
    dpts = sum(list(filter(lambda x: hist[plist.index(x)] == "d", plist)))
    return "c" if cpts/hist.count("c") > dpts/hist.count("d") else "d"

def hardRead(hist, ohist, o2hist):
    if len(hist)<6:
        return "c" if len(hist)%2 == 0 else "d"
    o1l = [int(x == "c") for x in ohist]
    o2l = [int(x == "c") for x in o2hist]
    l1 = list(bm.Berlekamp_Massey_algorithm(o1l))
    l2 = list(bm.Berlekamp_Massey_algorithm(o2l))
    l1.sort(reverse = True)
    l2.sort(reverse = True)
    sum1 = 0
    sum2 = 0
    for i in l1[1:]:
        sum1 += o1l[i - l1[0] - 1]
    for i in l2[1:]:
        sum2 += o2l[i - l2[0] - 1]
    sum1 = sum1 % 2
    sum2 = sum2 % 2
    play1 = "c" if sum1 == 1 else "d"
    play2 = "c" if sum2 == 1 else "d"
    return play1 if random.random() < .5 else play2


def eatherly(hist, ohist, o2hist):
    if len(hist) == 0:
        return "c"
    if ohist[-1] == "d" or o2hist[-1] == "d": 
        c1 = ohist.count("d")
        c2 = o2hist.count("d")
        p = (c1 + c2) / (len(ohist) + len(o2hist))
    return "d" if random.random() < p else "c"

def oneTFT(hist, ohist, o2hist):
    if len(hist) == 0:
        return "c"
    return ohist[-1] if random.random() < .5 else o2hist[-1]

def hindsight(hist, ohist, o2hist):
    if len(hist) == 0:
        return "c"
    c1 = ohist.count("d")
    c2 = o2hist.count("d")
    p = (c1 + c2) / (len(ohist) + len(o2hist))
    return "d" if random.random() < p else "c"

def niceXOR(hist, ohist, o2hist):
    if len(hist) == 0:
        return "c"
    return "d" if ohist[-1] != o2hist[-1] else "c"

def niceOR(hist, ohist, o2hist):
    if len(hist) == 0:
        return "c"
    return "d" if ohist[-1] == "d" or o2hist[-1]  == "d" else "c"

def niceAND(hist, ohist, o2hist):
    if len(hist) == 0:
        return "c"
    return "d" if ohist[-1] == "d" and o2hist[-1]  == "d" else "c"