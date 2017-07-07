"""QuickSort"""

def partition(arr,low, high):

	#Set pivot, using right most element.
	pivot = arr[high]

	#Index of smaller element
	i = (low - 1)

	#compare values and swap if less than pivot
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]
	
	arr[i+1],arr[high] = arr[high], arr[i+1]
	return (i+1)

def quicksort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)

		quicksort(arr, low, pi - 1)
		quicksort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr,0,n-1)

print("Sorted Array is:")
for i in range(n):
	print ("%d" % arr[i])