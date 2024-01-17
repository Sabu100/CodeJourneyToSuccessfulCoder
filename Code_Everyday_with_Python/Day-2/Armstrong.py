number=int(input("enter a numbers\n"))
num = number
digit, sum, = 0,0
length=len(str(num))
for i in range(length):
    digit = int(num%10)
    num = num/10
    sum+=pow(digit, length)
if sum == number:
    print("Its an ArmStrong")
else:
    print("its not an armstrong")
