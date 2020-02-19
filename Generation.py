from DNA import DNA

class Generation():
  
  def __init__(self, Generation=[], MaxSize=10):
    self.CurrSize = 0
    self.MaxSize = MaxSize
    self.Generation = []

    if(len(Generation) <= MaxSize):
      self.CurrSize = len(Generation)
      self.Generation = Generation
  
  def add(self, DNA: DNA) -> bool:
    if(self.CurrSize >= self.MaxSize): return False
    
    self.Generation.append(DNA)
    self.CurrSize += 1
    return True

  def get(self):
    return self.Generation

  def size(self):
    return self.CurrSize
       
