import random
from eightQueens import *
from DNA import DNA
from Generation import Generation

POPULATION_SIZE = 100
MUT_CHANCE = 0.10

oldGen = Generation([], POPULATION_SIZE)
for x in range(0, POPULATION_SIZE):
  oldGen.add(generateRandomDNA())

goalDNA = solve(oldGen, POPULATION_SIZE, MUT_CHANCE)

if(goalDNA != None):
  print("Initial Setup*")
  print(oldGen.get()[0].get())
  printBoard(oldGen.get()[0].get())
  print("Solved Setup")
  print(goalDNA)
  printBoard(goalDNA)
else:
  print("Max iterations succeeded. Failed to find goal setup.")
