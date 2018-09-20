def fibonacci(n):
	if n == 1 or n == 0:
		return 1
	elif n > 1:
		result = fibonacci(n-1) + fibonacci(n-2)
		return result

i = 0; even_sum = 0;
while fibonacci(i) < 4000000:
	i += 1
	
	if (fibonacci(i) % 2 == 0):
		even_sum += fibonacci(i)
print(even_sum)