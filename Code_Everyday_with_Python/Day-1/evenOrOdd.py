#
  
  
#Using Bitwise Operator
def isEven(num):
  return not num&1

if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')
