from DNA import QUEEN_BASES, DNA

def generateChild(parent1, parent2, crossPos):
  child = DNA(parent1.leftSplit(crossPos) + parent2.rightSplit(crossPos), QUEEN_BASES)
  print(child.get())
  child.setFitness(12)
  print(child.getFitness())

parent1 = DNA([1, 2, 3, 4, 5, 6, 7 ,8], QUEEN_BASES)
parent2 = DNA([4, 5, 7, 8, 4, 3, 2, 5], QUEEN_BASES)

print(parent1.get())
print(parent2.get())

x = 3

generateChild(parent1, parent2, x)


  

