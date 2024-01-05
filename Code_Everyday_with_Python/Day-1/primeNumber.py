#finding a prime number
num = 2
def checkPrime(num,iter=2):
  if num == iter:
    return True
  if num%iter==0:
    return False
  if num<2:
    return False
  return checkPrime(num,iter+1)
if checkPrime(num)==True:
  print("Prime")
else:
  print("Not Prime")
  
#1 is not a prime number because it doesnt meets the definition of prime number 
#and also 1 is not a composite number,the number of positive divisors or factors is only one i.e. 1 itself
#The prime numbers between 1 and 10 are 2, 3, 5, and 7
# Note: 2 is the smallest number that satisfies the definition of prime numbers.