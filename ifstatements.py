print 'Content-type: text/html'
print ''

name = "Rob"

if name == "Rob" or name == "Kirsten":
  print "Hello" + name
else:
  print "I do not know you"

# Create a program which displays the first 50 prime numbers

numberOfPrimes = 0
number = 2

while numberOfPrimes < 50:
  isPrime = True

  for i in range(2, number):
    if number % i == 0:
      isPrime = False

  if isPrime == True:
    print number
    numberofPrimes += 1

  number += 1
