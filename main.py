# Phoenix Valent
	# U3L5
		# Bubble Sort

# (◕_◕)    lucky autism creature loves bubble sort 
#  ᑌ ᑌ ￣ᑌ

def bubbleSort(mess):
	for i in range(len(mess)-1, 0, -1):
		for j in range(i):
			if mess[j] > mess[j+1]:
				mess[j], mess[j+1] = mess[j+1], mess[j]
	return mess

def main():
	messyList = [72, 43, 86, 27, 107, 69, 18, 4, 23, 176]
	print(f"Unsorted List: {messyList}\n")
	cleanList = bubbleSort(messyList)
	print(f"Sorted List: {cleanList}")

if __name__ == "__main__":
	main()