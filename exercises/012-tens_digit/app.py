# Complete the function to return the tens digit of a given integer
def tens_digit(num):
  aux=num//10
  aux_1= aux%10

  return aux_1


# Invoke the function with any integer
print(tens_digit(100))
