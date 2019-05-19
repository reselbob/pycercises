#Here's the lambda
def myfunc(n):
  return lambda a : a * n

const = 11

print("The constant is: ", const)

mydoubler = myfunc(2)

print("Let's double: ", mydoubler(const))

mytripler = myfunc(3)

print("Let's triple: ", mytripler(const))