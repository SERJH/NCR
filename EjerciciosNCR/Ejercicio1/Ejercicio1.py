def solucion(A, B, N, C, M):

	amountOfPlanks = N
	amountOfNails = M

	amountOfNailsNeeded = 0
	planksDone = 0
	allPlanksDone = False

	# Check for bad inputs on either the A array or the B array
	
	for i in range(amountOfPlanks):
		
		if A[i] > B[i]:

			print("All elements in the A array must be less or equal than the element in the same index of the B array\n")
			return -1
	
	# Start process

	for i in range(amountOfPlanks):

		for j in range(amountOfNails):
			
			print("Plank: [" + str(A[i]) + "-" + str(B[i]) + "]")
			print("Nail: " + str(C[j]))

			if A[i] <= C[j] and C[j] <= B[i]:

				print("Success" + "\n")
				amountOfNailsNeeded += 1
				planksDone += 1

				if planksDone == amountOfPlanks:
					
					allPlanksDone = True
					break

				break

			else:

				print("This nail wont work with this plank" + "\n")

		if allPlanksDone:
			break

	if allPlanksDone:
		
		return amountOfNailsNeeded

	else:

		return -1
	
result = solucion([1,4,5,8], [4,5,9,10], 4, [4,6,7,10,2], 5)

if result != -1:

	print("Minumum amount of nails needed: " + str(result))
	
else:

	print("There was either a problem with the data given or the is no way of nailing all of the planks with the nails given")

input("\nPress any key to exit")
