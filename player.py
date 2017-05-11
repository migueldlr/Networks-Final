class Player:
	def __init__(self, name, stratFunction):
		self.name = name
		self.stratFunction = stratFunction
		self.w = 0      # wins
		self.l = 0      # losses
		self.t = 0      # ties
		self.pf = 0     # points for
		self.pa = 0     # points against

	def __repr__(self):
		return "{}:\t{}-{}-{}\t{}:{}".format(self.name, self.w, self.t, self.l, self.pf, self.pa)
	# Determine my next move based on
	# h - my history (list)
	# oh1 and oh2 - my opponents' history
	def nextMove(self, h, oh1, oh2):
		return self.stratFunction(h,oh1,oh2)

