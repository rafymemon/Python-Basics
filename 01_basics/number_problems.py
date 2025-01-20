
print(0.1 + 0.1 + 0.1 - 0.3) # the output will give error value 

# to mitigate this issue we import (decimal) library to solve decimal problems
from decimal import Decimal

#process 1
number_one = Decimal('0.1')
number_two = Decimal('0.1')
number_three = Decimal('0.1')
number_four = Decimal('0.3')

print((number_one + number_two + number_three) - number_four)

#process 2
print((Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3'))

# Solving Fraction problems using fraction library
from fractions import Fraction

myFra = Fraction(2, 5)
myFra2 = Fraction(3, 7)

print(myFra/myFra2)


