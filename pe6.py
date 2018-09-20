print("Enter the range:")
n = int(input())

def sum_func(n):
	square_sum = 0
	sum_of_squares = 0
	for i in range(n+1):
		sum_of_squares += pow(i,2)
		square_sum += i
		
	diff = pow(square_sum,2) - sum_of_squares
	return diff

print(sum_func(n))