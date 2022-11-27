import random

# Returns index of x in arr if present, else -1
def ricerca_binaria(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2 #divisione in virgola mobile

		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return ricerca_binaria(arr, low, mid - 1, x)
		else:
			return ricerca_binaria(arr, mid + 1, high, x)

	else:
		return -1

#test
v = []
for _ in range(5):
	v.append( random.randint(0, 10) )
v.sort()

x = random.randint(1,10)

print("cercando ",x, "in: ",v)

# Function call
result = ricerca_binaria(v, 0, len(v)-1, x)

if result != -1:
	print(":-) Trovato ",x," in posizione: (", str(result),")" )
else:
	print("Non trovato :-( ")
