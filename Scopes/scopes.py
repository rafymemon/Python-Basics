x = 99


def func1(y):
    z = x + y
    return z


print(func1(4))

# def func2() :
#   global x
#  x = 12

# func2
# print(x)


#def func3():
 #   x = 88

  #  def func4():
   #     print(x)

    #func4()


#func3()

def func1() :
    x = 88
    def funct2() :
        print(x)
    return funct2 # return the definition of function 2 only and the veriable assossiated with the function 2(bag theory/ closure property)
myResult = func1()
myResult()


def power(num) :
    def actual(x) :
        return x ** num
    return actual


f = power(2)
g = power(3)

print(f(3))
print(g(3))