"""QuickSort"""

def partition(arr, low, high):

	#Set pivot point choosing further value to the right of the partition
	pivot = arr[high]

	#Set smaller index element
	i = (low - 1)
	print i
	#Check the current element against the pivot point
	for j in range(low, high):
		
		#if the current element is less than the pivot value
		#increment the smaller index value, and swap current value
		#with the smaller index value
		if arr[j] <= pivot:
			print j
			i = i+1
			print i
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[high] = arr[high],arr[i+1]
	return (i+1)

def quicksort(arr, low, high):
	if low < high:

		#partition the array
		pi = partition(arr,low,high)

		#quicksort values to the right and left of the partition
		quicksort(arr,low,pi-1)
		quicksort(arr,pi+1,high)

arr = [10, 7, 8, 9, 1, 5]

n = len(arr)
quicksort(arr,0,n-1)

print("Sorted Array is:")
for i in range(n):
	print ("%d" % arr[i])