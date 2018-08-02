def solution(A, B):
	
	lenghtA = len(A)
	lenghtB = len(B)

	# Make both lowecase for an easier comparison

	A = A.lower()
	B = B.lower()

	appearsInA = False
	appearingTimes = 0

	for i in range(lenghtA):
		
		if (i + (lenghtB - 1)) <= lenghtA:

			# Create a substring from A anc compare it with B

			subGroupA = A[i:(i+lenghtB)]
			
			for letter in subGroupA:

				for j in range(lenghtB):

					if B[j] == letter:
						appearsInA = True
						break

					elif j == (lenghtB - 1):
						appearsInA = False
						break

				if not appearsInA:
					break

		if appearsInA:
			
			appearingTimes += 1
			appearsInA = False

	return appearingTimes

A = "Hola, que buena ola Laomir"
B = "OAL"

result = solution(A, B)
print("The substring '" + str(B) + "' appears " + str(result) + " times in the string '" + str(A) + "'")
input("\nPress any key to exit")
