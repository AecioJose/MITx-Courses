"""
Exercise 1

developed by: Aecio Jose 

code created just for testing to be able to solve the questions in exercise 1 of Unit 1 of MITx 6.00.2x
"""

class Thing:
  def __init__(self, name, weight, value):
    self.value = value
    self.weight = weight
    self.name = name

def metric1(item):
  return item.value / item.weight

def metric2(item):
  return -item.weight

def metric3(item):
  return item.value

dirt = Thing('dirt', 4, 0)
computer = Thing('computer', 10, 30)
fork = Thing('fork', 5, 1)
problemSet = Thing('problemSet', 0, -10)

mylist = [dirt, computer, fork, problemSet]

print(" Metric1 \n")
print("The metric 1 does not run becaus cannot divide by 0")
#for item in mylist:
#  print(item.name, metric1(item))

print("\n\n Metric2 \n")
for item in mylist:
  print(item.name, metric2(item))

print("\n\n Metric3 \n")
for item in mylist:
  print(item.name, metric3(item))