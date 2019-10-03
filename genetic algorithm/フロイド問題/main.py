from Population import Population
from Individual import Individual
from datetime import datetime
import random

if __name__ == "__main__":
    pop = Population()
    random.seed(datetime.now())
    for i in range(1, Individual.GEN_MAX+1):
        pop.alternate()
        print("第{}世代: 最良適応度{}\n".format(i, pop.ind[0].fitness))
    pop.printResult()
    