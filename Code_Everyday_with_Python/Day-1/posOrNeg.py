#Using Brute force method
num = 2
if num > 0:
    print('it is positive')
elif num < 0:
    print('It is Negative')
else:
    print('zero')
    
#using Nested if-else Statements
num = -2
if num >= 0:
    if num==0:
        print('zero')
    else:
        print("positive")
        
#Using Ternary Operator

num = 4
print("Positive" if num>0 else "Negative")