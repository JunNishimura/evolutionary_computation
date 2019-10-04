# import Individual as ind
from Individual import Individual
import sys
import numpy as np 

class Population:
    def __init__(self):
        self.ind = []
        self.nextInd = []
        for _ in range(Individual.POP_SIZE):
            self.ind.append(Individual())
            self.nextInd.append(Individual())
        self.evaluate()

    def alternate(self):

        # ルーレット選択のための処理
        self.trFit = [] # traversed fitness array
        self.denom = 0.0

        for i in range(Individual.POP_SIZE):
            self.trFit.append( (self.ind[Individual.POP_SIZE-1].fitness - self.ind[i].fitness) \
                                / self.ind[Individual.POP_SIZE-1].fitness - self.ind[0].fitness )
            self.denom += self.trFit[i]

        # エリート保存戦略
        for i in range(Individual.ELITE):
            for j in range(Individual.N):
                self.nextInd[i].chrom[j] = self.ind[i].chrom[j]

        # 親を選択して交叉する
        for i in range(Individual.ELITE, Individual.POP_SIZE):
            p1 = self.select_rank_order()
            p2 = self.select_rank_order()
            self.nextInd[i].crossover_onepoint(self.ind[p1], self.ind[p2])

        # 突然変異を起こす
        for i in range(Individual.ELITE, Individual.POP_SIZE):
            self.nextInd[i].mutate()

        # 次世代と現世代を交代
        tmp = self.ind
        self.ind = self.nextInd
        self.nextInd = tmp

        # 評価する
        self.evaluate()

    # 結果を表示する
    def printResult(self):
        s_a = "集合A: "
        for i in range(Individual.N):
            if self.ind[0].chrom[i] == 1:
                s_a += "√{} ".format(i+1)
        s_b = "集合B: "
        for i in range(Individual.N):
            if self.ind[0].chrom[i] == 0:
                s_b += "√{} ".format(i+1)
        print(s_a)
        print(s_b)
        print("差: {}".format(self.ind[0].fitness))


    def evaluate(self):
        for i in range(Individual.POP_SIZE):
            self.ind[i].evaluate()
        self.quick_sort(0, Individual.POP_SIZE-1)

    # 順位に基づくランキング選択で親個体を１つ選択する
    def select_rank_order(self):
        denom = Individual.POP_SIZE * (Individual.POP_SIZE + 1) / 2
        r = np.random.randint(denom) + 1 # random variable
        for num in range(Individual.POP_SIZE, 0, -1):
            if r <= num:
                break
            r -= num
        return Individual.POP_SIZE - num

    # 確率に基づくランキング選択で親個体を１つ選択する
    def select_rank_prob(self):
        denom = Individual.POP_SIZE * (Individual.POP_SIZE + 1) / 2
        r = np.random.rand()
        for rank in range(1, Individual.POP_SIZE+1):
            prob = (Individual.POP_SIZE - (rank-1)) / denom
            if r <= prob:
                break
            r -= prob
        return rank - 1

    # ルーレット選択で親個体を１つ選ぶ
    def select_roulette(self):
        r = np.random.rand()
        for rank in range(1, Individual.POP_SIZE+1):
            prob = self.trFit[rank-1] / self.denom
            if r <= prob: 
                break
            r -= prob
        return rank - 1

    # トーナメント選択で親個体を１つ選ぶ
    def select_tournament(self):
        tmp = [0] * Individual.POP_SIZE
        bestFit = (-1, sys.maxsize)
        num = 0
        while True:
            r = np.random.randint(Individual.POP_SIZE)
            if tmp[r] == 0:
                tmp[r] = 1
                if self.ind[r].fitness < bestFit[1]:
                    bestFit = (r, self.ind[r].fitness)
                num += 1
                if num == Individual.TOURNAMENT_SIZE:
                    break
        return bestFit[0]

    def quick_sort(self, lb, ub):
        if lb < ub:
            k = (lb + ub) // 2
            pivot = self.ind[k].fitness
            i = lb
            j = ub
            while i <= j:
                while self.ind[i].fitness < pivot:
                    i += 1
                while self.ind[j].fitness > pivot:
                    j -= 1
                if i <= j:
                    tmp = self.ind[i]
                    self.ind[i] = self.ind[j]
                    self.ind[j] = tmp
                    i += 1
                    j -= 1
            self.quick_sort(lb, j)
            self.quick_sort(i, ub)