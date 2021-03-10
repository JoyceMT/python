print 'Content-type: text/html'
print ''

def sayHello():
  print "Hello!"

sayHello()

def saySomething(string):
  print string

saySomething("Hi there!")

def multiplyTwoNumbers(x, y):
  return x * y

print multiplyTwoNumbers(4, 6)

def highestCommonFactor(x, y):
  for i in range(1, x + 1):
    if x % i == 0 and y % i == 0:
      hcf = i
  return hcf

print highestCommonFactor(4, 6)

a = 5
b = 6

def addTwoNumbers():
  a = 10
  return a + b

print addTwoNumbers()
print a
