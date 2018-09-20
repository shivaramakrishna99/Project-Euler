prime = []
n = 200000
for num in range(n):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,int(pow(num,0.5)+1)):
           if (num % i) == 0:
               break
       else:
           prime.append(num)

print(prime[10000])
		 
		