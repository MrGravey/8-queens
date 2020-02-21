import random
from DNA import DNA
from Generation import Generation

QUEEN_BASES = [0, 1, 2, 3, 4, 5, 6, 7]
# Maximum number of queens collisions
MAX_FITNESS = 28

# Checks for collisions between points(row, col)
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

# Generates the fitness score of a DNA
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

  return MAX_FITNESS - fitness

# Generates a new child DNA from two parents swapping DNA from both at a DNA cross position.
def generateChild(parent1: DNA, parent2: DNA, crossPos: int, mutChance: float) -> DNA:
  child = DNA(parent1.leftSplit(crossPos) + parent2.rightSplit(crossPos), QUEEN_BASES)
  if(random.random() <= mutChance):
    child.randomMutate()
  child.setFitness(fitnessFunc(child))
  return child

# Generates a random DNA
def generateRandomDNA() -> DNA:
  newDNA = []
  for base in range(0, 8):
    newDNA.append(QUEEN_BASES[random.randint(0, 7)])

  newDNA = DNA(newDNA, QUEEN_BASES)
  newDNA.setFitness(fitnessFunc(newDNA))
  return newDNA

# Prints the queen's board setup
def printBoard(individual: DNA):
  if(individual is not None):
    for row in range(0, len(individual)):
      print("|", end='')
      for col in range(0, len(individual)):
        if(individual[col] == row):
          print("Q|", end='')
        else:
          print("-|", end='')
      print()


# Genetic Algorithm
def solve(oldGen: Generation, populationSize: int, mutChance: float):
  goalDNA = None
  genCount = 0
  isGoal = False
  while(not isGoal):
    print(str(oldGen.getAverageFitness()))
    newGen = Generation([], populationSize)
    while(not newGen.isFull()):
      parent1 = oldGen.get()[oldGen.getSelectionIndex(random.random())]
      parent2 = oldGen.get()[oldGen.getSelectionIndex(random.random())]
      crossPot = random.randint(0, len(QUEEN_BASES)-1)
      child = generateChild(parent1, parent2, crossPot, mutChance)
      if(child.getFitness() >= MAX_FITNESS): 
        goalDNA = child.get()
        isGoal = True
      newGen.add(child) 
      child = generateChild(parent2, parent1, crossPot, mutChance)
      if(child.getFitness() >= MAX_FITNESS): 
        goalDNA = child.get()
        isGoal = True
      newGen.add(child)

    oldGen = newGen
    genCount += 1

  print("Generations: " + str(genCount))
  printBoard(goalDNA)

