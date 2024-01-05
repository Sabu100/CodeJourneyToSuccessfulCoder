#finding a leap year
def leap(year):
  if (year % 4==0) or (year%400==0 and year%100!=0):
    print("yeah, It is a leap year")
  else:
    print("No, It is not a leap year")
year=int(input("Please Enter a year:"))
leap(year)

#this can also be solved by calander module and lambda function.