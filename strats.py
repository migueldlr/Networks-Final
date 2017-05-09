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
def random(h, oh1, oh2):
	return 'c' if random.random() < 0.5 else 'd'

## Cooperate
## Always cooperate
def alwaysc(h,oh1,oh2):
	return 'c'

## Defect
## Always defect
def alwaysd(h,oh1,oh2):
	return 'd'

