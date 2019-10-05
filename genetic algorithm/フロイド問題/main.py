from Population import Population
from Individual import Individual
from datetime import datetime
import random

if __name__ == "__main__":
    for j in range(4):
        if j == 0:
            print("順位に基づくランキング選択")
        elif j == 1:
            print("確率に基づくランキング選択")
        elif j == 2:
            print("ルーレット選択")
        else:
            print("トーナメント選択")
        pop = Population()
        random.seed(datetime.now())
        for i in range(1, Individual.GEN_MAX+1):
            pop.alternate(j)
            # print("第{}世代: 最良適応度{}".format(i, pop.ind[0].fitness))
        pop.printResult()