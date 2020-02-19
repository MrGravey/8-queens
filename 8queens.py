import random

QUEEN_BASES = [1, 2, 3, 4, 5, 6, 7, 8]

class DNA(): 

  def __init__(self, DNA=[], Bases=set, MaxLen=8):
    self.MaxLen = MaxLen
    self.DNA = []
    self.Bases = Bases
    if(len(DNA) == self.MaxLen):
      self.DNA = DNA 
    
  def set(self, DNA: list) -> bool:
    if(len(DNA) != self.MaxLen): return False
    self.DNA = DNA
    return True

  def get(self) -> list:
    return self.DNA
  
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

def generateChild(parent1, parent2, crossPos):
  child = DNA(parent1.leftSplit(crossPos) + parent2.rightSplit(crossPos), QUEEN_BASES)
  print(child.get())

parent1 = DNA([1, 2, 3, 4, 5, 6, 7 ,8], QUEEN_BASES)
parent2 = DNA([4, 5, 7, 8, 4, 3, 2, 5], QUEEN_BASES)

print(parent1.get())
print(parent2.get())

x = 3

generateChild(parent1, parent2, x)


  

