from DNA import QUEEN_BASES, DNA

def isCollision(x1: int, y1: int, x2: int, y2: int):
  # Vertical check (should never occurr)
  if(x1 == x2): return True
  # Horizontal check
  if(y1 == y2): return True

  comp1 = x1 - x2 if (x1 > x2) else x2 - x1
  comp2 = y1 - y2 if (y1 > y2) else y2 - y1

  # Diagonal check
  if(comp1 == comp2): return True

  # No collision
  return False

def fitnessFunc(individual: DNA) -> int:
  DNA = individual.get()
  maxIndex = len(DNA)
  currIndex = 0
  fitness = 0

  for val1 in DNA[:maxIndex]:
    x1 = currIndex
    y1 = val1
    subCurrIndex = currIndex+1

    for val2 in DNA[currIndex+1:maxIndex]:
      x2 = subCurrIndex
      y2 = val2
      if(isCollision(x1, y1, x2, y2)):
        fitness += 1
      subCurrIndex += 1  

    currIndex += 1

  return fitness

def generateChild(parent1, parent2, crossPos):
  child = DNA(parent1.leftSplit(crossPos) + parent2.rightSplit(crossPos), QUEEN_BASES)
  print(child.get())
  child.setFitness(fitnessFunc(child))
  print(child.getFitness())

parent1 = DNA([0, 1, 2, 3, 4, 5, 6, 7], QUEEN_BASES)
parent2 = DNA([4, 5, 7, 0, 4, 3, 2, 5], QUEEN_BASES)

parent1.setFitness(fitnessFunc(parent1))
parent2.setFitness(fitnessFunc(parent2))
print(parent1.getFitness())
print(parent2.getFitness())

print(parent1.get())
print(parent2.get())

x = 3

generateChild(parent1, parent2, x)

