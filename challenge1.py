sumOfMultiples = 0		# initialize sum 
for i in range(3,1000,3):
	sumOfMultiples += i	# add multiples of 3
for j in range(5,1000,5):
	sumOfMultiples += j	# add multiples of 5
for k in range(15,1000,15):
	sumOfMultiples -=k	# subtract overlapping multiples of 15
print(sumOfMultiples)
