# Complete the function to return the respective number of the century
def century(year):
  if 0< year <= 100:
    siglo=1
  elif year % 100 == 0:
    siglo= year//100
  else:
    siglo= (year//100)+1
  return siglo


# Invoke the function with any given year
print(century(2001))
