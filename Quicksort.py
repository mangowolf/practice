"""QuickSort"""

def partition(arr,low,high):
	#set the pivot point
	pivot = arr[high]

	#set the index for the value larger than the pivot
	i = (low - 1)

	'''Loop through and partition the array setting larger values
	to the right and smaller values to the left.
	'''
	for j in range(low,high):
		if arr[j] <= pivot:
			i = i + 1
			arr[i],arr[j] = arr[j],arr[i]
	#Set the pivot to the correct location
	arr[i+1],arr[high] = arr[high],arr[i+1]
	return (i+1)

def quicksort(arr,low, high):
	#Check if the higher number is greater than the lower number
	if low < high:

		#Helper function to partition the array
		pi = partition(arr,low,high)

		quicksort(arr,0,pi-1)
		quicksort(arr,pi+1, high)

#Test Cases
arr = [10,8,4,3,7,5]
n = len(arr)
quicksort(arr,0,n-1)

print arr