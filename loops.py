print 'Content-type: text/html'
print ''

for i in range(11):
  print i

favouriteFoods = ["pizza", "chocolate", "burger"]

for food in favouriteFoods:
  print "I like eating " + food + "."

x = 0
while x <= 10:
  print x
  x += 1

# Dictorary containing 4 names and ages of people
# Create loop name and age
ages = {}
ages["Sam"] = 45
ages["Bob"] = 19
ages["Rob"] = 24
ages["Tom"] = 30

for age in ages:
  print age + "is" + str(ages[age])




