def printDivisors(n=int(input("please enter a number:\n"))) :
    
    i = 1
    while i <= n :
        if (n % i==0) :
            print (i,end=" ")
        i = i + 1
         
# Driver method
print ("The divisors within a range are: ")
printDivisors()