import random
from DNA import DNA
from Generation import Generation

QUEEN_BASES = [0, 1, 2, 3, 4, 5, 6, 7]
MUT_CHANCE = 0.10
POPULATION_SIZE = 10

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

def generateChild(parent1: DNA, parent2: DNA, crossPos: int) -> DNA:
  child = DNA(parent1.leftSplit(crossPos) + parent2.rightSplit(crossPos), QUEEN_BASES)
  child.setFitness(fitnessFunc(child))
  if(random.random() <= MUT_CHANCE):
    child.randomMutate()

  return child

def generateRandomDNA() -> DNA:
  newDNA = []
  for base in range(0, 8):
    newDNA.append(QUEEN_BASES[random.randint(0, 7)])

  newDNA = DNA(newDNA, QUEEN_BASES)
  newDNA.setFitness(fitnessFunc(newDNA))
  return newDNA


Gen0 = Generation([], POPULATION_SIZE)
for x in range(0, POPULATION_SIZE):
  Gen0.add(generateRandomDNA())

rand = random.random()
print(rand)
print(Gen0.getSelectionIndex(rand))
print(Gen0.getFitness())
print(Gen0.getAverageFitness())

