# Complete the function to return the amount of days it will take to cover a route
import math

def car_route(n,m):
    dia=1
    aux=(m*dia)/n
    return math.ceil(aux)
  




# Invoke the function with two integers
print(car_route(20,40))

# asi tambien se puede hacer
"""calculo=int((m*1)/n)
  return calculo """