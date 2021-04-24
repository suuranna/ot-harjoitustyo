import random

def generate_matrix(size):
	while True:
		amounts = {}
		amounts[0] = 0
		amounts[1] = 0
		amounts[2] = 0
		amounts[3] = 0
		matrix = [[]]*size
		for y in range(size):
			row = []
			for x in range(size):
				number = random.randint(0,3)
				amounts[number] += 1
				row.append(number)
			matrix[y] = row
		#print(matrix)
		if amounts[0] <= 6 and amounts[3]+amounts[2] <= 6 and amounts[0] >= 4 and amounts[3] >= 1 and amounts[2] >= 2 and amounts[3] <= 3:
			return matrix
