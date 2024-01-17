num=int(input("enter a number:\n")) 
pows=int(input("enter a power:\n"))
def findpow(num, pows):
    if pows == 0:
        return 1
    return num * findpow(num, pows-1)
print(findpow(num, pows))
#this can also be done using an inbuilt function called pow()
# num, power = 3, 2
# print(pow(num,power))