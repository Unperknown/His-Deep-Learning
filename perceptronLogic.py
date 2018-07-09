def AND(in1, in2):
	input = np.array([in1, in2])
	weight = np.array([1, 1])
	std = -1
	value = np.sum(input * weight) + std
	if value > 0:
		return 1
	else:
		return 0
		
def OR(in1, in2):
	input = np.array([in1, in2])
	weight = np.array([1, 1])
	std = 0
	value = np.sum(input * weight) + std
	if value > 0:
		return 1
	else:
		return 0
		
def NAND(in1, in2):
	input = np.array([in1, in2])
	weight = np.array([-1, -1])
	std = 2
	value = np.sum(input * weight) + std
	if value <= 0:
		return 0
	else:
		return 1
		
def NOR(in1, in2):
	input = np.array([in1, in2])
	weight = np.array([-1, -1])
	std = 0
	value = np.sum(input * weight) + std
	if value <= 0:
		return 0
	else:
		return 1
		
def XOR(in1, in2):
	value = AND(NAND(in1, in2), OR(in1, in2))
	return value