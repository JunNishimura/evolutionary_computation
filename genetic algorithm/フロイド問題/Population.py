# import Individual as ind
from Individual import Individual

class Population:
    def __init__(self):
        self.ind = []
        self.nextInd = []
        for _ in range(Individual.POP_SIZE):
            self.ind.append(Individual())
            self.nextInd.append(Individual())
        self.evaluate()

    def alternate(self):
        # エリート保存戦略
        for i in range(Individual.ELITE):
            for j in range(Individual.N):
                self.nextInd[i].chrom[j] = self.ind[i].chrom[j]

        # 親を選択して交叉する
        for i in range(Individual.ELITE, Individual.POP_SIZE):
            p1 = self.select()
            p2 = self.select()
            self.nextInd[i].crossover(self.ind[p1], self.ind[p2])

        # 突然変異を起こす
        for i in range(Individual.ELITE, Individual.POP_SIZE):
            self.nextInd[i].mutate()

        # 次世代と現世代を交代
        tmp = self.ind
        self.ind = self.nextInd
        self.nextInd = tmp

        # 評価する
        self.evaluate()

    def printResult(self):
        pass

    def evaluate(self):
        for i in range(Individual.POP_SIZE):
            self.ind[i].evaluate()
        self.quick_sort(0, Individual.POP_SIZE-1)

    def select(self):
        pass

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