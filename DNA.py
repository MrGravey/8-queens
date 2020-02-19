import random

QUEEN_BASES = [1, 2, 3, 4, 5, 6, 7, 8]

class DNA(): 

  def __init__(self, DNA=[], Bases=set, MaxLen=8):
    self.MaxLen = MaxLen
    self.DNA = []
    self.Bases = Bases
    self.Fitness = -1
    if(len(DNA) == self.MaxLen):
      self.DNA = DNA 
    
  def set(self, DNA: list) -> bool:
    if(len(DNA) != self.MaxLen): return False
    self.DNA = DNA
    return True

  def setFitness(self, Fitness: int) -> bool:
    self.Fitness = Fitness
    return True

  def get(self) -> list:
    return self.DNA

  def getFitness(self) -> int:
    return self.Fitness
  
  def leftSplit(self, index: int) -> list:
    leftSplit = []
    for x in self.DNA[:index]:
      leftSplit.append(x)
    return leftSplit
    
  def rightSplit(self, index: int) -> list:
    rightSplit = []
    for x in self.DNA[index:]:
      rightSplit.append(x)
    return rightSplit

  def randomMutate(self) -> bool:
    if(len(self.Bases) == 0): return False
    randIndex = random.randint(0, self.MaxLen)
    randBase = random.randint(0, len(self.Bases))
    self.DNA[randIndex] = randBase
    return True
