import random

QUEEN_BASES = [0, 1, 2, 3, 4, 5, 6, 7]

class DNA(): 

  def __init__(self, DNA=[], Bases=set, MaxLen=8):
    self.MaxLen = MaxLen
    self.DNA = []
    self.Bases = Bases
    self.Fitness = -1

    # check if Bases exist in given DNA
      
    if(len(DNA) == self.MaxLen and self._containsBases(DNA)):
      self.DNA = DNA
     
  def _containsBases(self, DNA) -> bool:
    for x in DNA:
      if(x not in self.Bases): return False
    return True

  def set(self, DNA: list) -> bool:
    if(len(DNA) == self.MaxLen and self._containsBases(DNA)):
      self.DNA = DNA
      return True
    return False

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
    randIndex = random.randint(0, self.MaxLen-1)
    randBase = random.randint(0, len(self.Bases)-1)
    self.DNA[randIndex] = randBase
    return True
