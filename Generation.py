from DNA import DNA

class Generation():
  
  def __init__(self, Generation=[], MaxSize=10):
    self.CurrSize = 0
    self.MaxSize = MaxSize
    self.Generation = []
    self.SelectionChance = []

    if(len(Generation) <= MaxSize):
      self.CurrSize = len(Generation)
      self.Generation = Generation
      self._generateSelectionChance()
  
  def _generateSelectionChance(self):
    self.SelectionChance =  []
    generationFitness = self.getFitness()
    for x in self.Generation:
      chance = x.getFitness()/generationFitness
      self.SelectionChance.append(chance)
      

  def add(self, DNA: DNA) -> bool:
    if(self.CurrSize >= self.MaxSize): return False
    
    self.Generation.append(DNA)
    self._generateSelectionChance()
    self.CurrSize += 1
    return True

  def get(self):
    return self.Generation

  def size(self):
    return self.CurrSize
       
  def getSelectionChance(self):
    return self.SelectionChance

  def getSelectionIndex(self, chance: int) -> int:
    index = 0
    currSum = 0
    for x in self.SelectionChance:
      currSum += self.SelectionChance[index]
      print(str(currSum) +": @ind_" + str(index))
      if(currSum <= chance):
        index += 1
      else: break
    return index

  def getFitness(self):
    fitness = 0
    for x in self.Generation:
      fitness += x.getFitness()

    return fitness

  def getAverageFitness(self) -> float:
    return self.getFitness()/self.CurrSize
