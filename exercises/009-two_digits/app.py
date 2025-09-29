# Complete the function to return the tens digit and the units digit of any interger
def two_digits(number):
  number = str(number)
  numero_1 = number[0]
  numero_2 = number[1]
  return int(numero_1), int(numero_2)
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))

def two_digits1(number):
  numero_1 = number//10
  numero_2 = number%10
  return (numero_1), (numero_2)

print(two_digits1(79))