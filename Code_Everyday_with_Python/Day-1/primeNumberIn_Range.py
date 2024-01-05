#finding a prime number within a range
low, high = 2, 100
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)
  
#1 is not a prime number because it doesnt meets the definition of prime number 
#and also 1 is not a composite number,the number of positive divisors or factors is only one i.e. 1 itself
#The prime numbers between 1 and 10 are 2, 3, 5, and 7
# Note: 2 is the smallest number that satisfies the definition of prime numbers.