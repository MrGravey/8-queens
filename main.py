import sys
import random
from eightQueens import *
from DNA import DNA
from Generation import Generation

POPULATION_SIZE = 100
MUT_CHANCE = 0.10

# Command line argument checking and assignment
if len(sys.argv) > 1:
    if len(sys.argv) == 3:
        if float(sys.argv[2]) < 0.0 or float(sys.argv[2]) > 1.0:
            print("main: invalid entry for MUTATION_CHANCE. Valid entries: 0 <= x <= 1")
            sys.exit(1)
        else:
            POPULATION_SIZE = int(sys.argv[1])
            MUT_CHANCE = float(sys.argv[2])
    else:
        print("main: invalid number of arguments.")
        print("main: python3 main.py int float.")
        print("main: python3 main.py POPULATION_SIZE MUTATION_CHANCE")
        sys.exit(1)

# Generate random DNAs for a initial generation
oldGen = Generation([], POPULATION_SIZE)
for x in range(0, POPULATION_SIZE):
    oldGen.add(generateRandomDNA())

# Solve for 8queens
goalDNA = solve(oldGen, POPULATION_SIZE, MUT_CHANCE)

# Print results
if goalDNA != None:
    print("Initial Setup*")
    print(oldGen.get()[0].get())
    printBoard(oldGen.get()[0].get())
    print("Solved Setup")
    print(goalDNA)
    printBoard(goalDNA)
else:
    print("Max iterations succeeded. Failed to find goal setup.")
