from Individual import Individual
import numpy as np

class Population:
    def __init__(self, cities):
        self.ind = []
        self.nextInd = []
        self.cities = cities
        for _ in range(Individual.POP_SIZE):
            self.ind.append(Individual(cities))
            self.nextInd.append(Individual(cities))
        self.evaluate()

    # 世代交代
    def alternate(self):
        # 親を選択して交叉する
        for i in range(Individual.POP_SIZE):
            p1 = self.select()
            p2 = self.select()
            self.nextInd[i].crossover(self.ind[p1], self.ind[p2])
        
        for i in range(Individual.POP_SIZE):
            self.nextInd[i].mutate()

        tmp = self.ind
        self.ind = self.nextInd
        self.nextInd = tmp

        self.evaluate()

    # 結果表示
    def printResult(self):
        order_list = [i for i in range(1, len(self.cities)+1)] # 順序リスト
        visit_order = [] # 実際の巡回順
        for i in range(len(self.cities)):
            t = self.ind[0].chrom[i]
            visit = order_list[t-1]
            visit_order.append(visit)
            order_list.remove(visit)

        # 巡回順に都市を表示する
        for i in range(len(visit_order)):
            print('{}: {}'.format(i+1, self.cities[visit_order[i]-1].name))
        print('総距離: {}(km)'.format(self.ind[0].fitness))

    # 親個体の選択
    # 確率に基づくランキング選択
    def select(self):
        denom = Individual.POP_SIZE * (Individual.POP_SIZE + 1) / 2
        r = np.random.rand()
        for rank in range(1, Individual.POP_SIZE+1):
            prob = (Individual.POP_SIZE - (rank-1)) / denom
            if r <= prob:
                break
            r -= prob
        return rank-1

    # 評価
    def evaluate(self):
        for i in range(Individual.POP_SIZE):
            self.ind[i].evaluate()
        self.quick_sort(0, Individual.POP_SIZE-1) # 距離が短い順(昇順)に並び替える

    # 昇順にクイックソート
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