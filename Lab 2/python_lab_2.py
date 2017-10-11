# Print out all the 8 bit binary numbers 
# Do not use a decimal to binary conversion


def add1(arr):
	i=len(arr)-1
	if(arr[i] == 0):
		arr[i] = 1
		return arr
	else:
		while(arr[i] == 1 and i>=0):
			arr[i] = 0
			i = i-1
		arr[i] = 1
		return arr


if __name__ == "__main__":
	arr = [0,0,0,0,0,0,0,0]
	print(arr)
	for i in range(pow(2,len(arr))):
		print(add1(arr))
	print("Total numbers printed = " + str(i+1))