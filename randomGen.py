import random

#randomize and randoutcome used for S1_AA, S1_AR, S1_RA, S1_RR, S2_AA, S2_RR
#randomizeARRA and randOutcomeARRA used for S2_AR_RA

#This function takes an ascending list of numbers and randomizes them
#Ex: [1,2,3,4,5,6,7,8,9] -> [3,6,4,9,1,10,2,7,5,8]
def randomize(list1):
	#Within list1, loop through two items at a time
	for (i, k) in zip(list1[::2], list1[1::2]):
		#if the list is no completely randomized, break the loop and recursively call the function
		if (i + 1 == k or i - 1 == k):
			list1 = random.sample(list1, len(list1))
			break
		#if list is completely randomized, return that list
		else:
			if list1.index(k) == len(list1) - 1:
				return list1
			else:
				continue 
	return randomize(list1)

#This function takes the above created list of randomized numbers and rearranges "list1" into that order
def randOutcome(list1):
	list2 = list(range(len(list1)))
	list3 = []	
	list2 = randomize(list2)
	#Use numerical list2 to arragen alphabetical list1
	for x in list2:
		list3.append(list1[x])
	return list3

#This function takes an ascending list of numbers, picks out every other number, and then randomizes those
#Ex: [1,2,3,4,5,6,7,8,9] -> [1,4,3,8,5,10,7,2,9,6]
def randomizeARRA(list1,list2):	
	for i in list(range(len(list2))):
		if (list1[i] == list2[i]):
			list2 = random.sample(list2, len(list2))
			break
		#if list is completely randomized, return that list
		else:
			if i == len(list2) - 1:
				return list2
			else:
				continue 
	return randomizeARRA(list1,list2)

#This function takes the above created list of randomized numbers and rearranges "list1" into that order
def randOutcomeARRA(list1):
	#side1 and side2 represent the two different parts of list1, side1 = [1,3,5,7,9] side2 = [2,4,6,8,10]
	side1 = list1[::2]
	side2 = list1[1::2]
	
	#This only randomizes the side2 set of numbers
	list2 = random.sample(side2, len(side2))
	list3 = randomizeARRA(side2,list2)
	
	#the final list combines the randomized side2 with the untouched side1
	final = []
	for i in list(range(len(side1))):
		final.append(side1[i])
		final.append(list3[i])

	return final

def modifySingles(list1,list2):
	list1.insert(0,list1[0])
	list1.insert(len(list1)-1,list1[len(list1)-1])
	list2.insert(0,list2[0])
	list2.insert(len(list2)-1,list2[len(list2)-1])
	list3 = []

	for f, b in zip(list1,list2):
		list3.append((f, b))

	list4 = sorted(list3, key=lambda tup: tup[0])
	list5 = zip(*list4)[1]

	outcome = []
	#AA = [6,32,16,2,8,30,26,24,4,10,28,18,34,14,36,54,48,50,20,42,40,38,44,64,56,62,46,52,12,58,22,60]
	RR = [25,23,21,29,27,31,17,19,9,3,11,7,1,13,15,5,47,35,43,33,39,45,37,41,53,57,61,63,59,55,51,49]
	#AR_RA = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,
	#34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64

	#for i in AA:
	#	outcome.append(list5[i-1])
	for i in RR:
		outcome.append(list5[i-1])	
	#for i in AR_RA_1:
	#	outcome.append(list5[i])
	return outcome

def modifySinglesARRA(list1,list2):
	list1.insert(0,list1[0])
	list1.insert(len(list1)-1,list1[len(list1)-1])
	list2.insert(0,list2[0])
	list2.insert(len(list2)-1,list2[len(list2)-1])
	list3 = []

	for f, b in zip(list1,list2):
		list3.append((f, b))

	list4 = sorted(list3, key=lambda tup: tup[0])
	list5 = zip(*list4)[1]
	list5 = list5[::2]

	outcome = []
	#AA = [6,32,16,2,8,30,26,24,4,10,28,18,34,14,36,54,48,50,20,42,40,38,44,64,56,62,46,52,12,58,22,60]
	#RR = [25,23,21,29,27,31,17,19,9,3,11,7,1,13,15,5,47,35,43,33,39,45,37,41,53,57,61,63,59,55,51,49]
	AR_RA = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,
	34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]

	for i in AR_RA:
		outcome.append(list5[i-1])
	return outcome

