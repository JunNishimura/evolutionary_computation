import numpy as np
from City import City

'''
解の表現方法には順序表現(order representation)を用いる
'''
class Individual:

    GEN_MAX = 500 # 世代交代数
    POP_SIZE = 100 # 個体群数
    ELITE = 1 # エリート保存戦略
    MUTATION_PROB = 0.01 # 突然変異の確率

    def __init__(self, cities):
        self.chrom = []
        self.cities = cities
        # 順序表現
        # i番目の遺伝子は1以上N-(i-1)以下の数字が入っている
        for i in range(len(self.cities)):
            self.chrom[i] = np.random.randint(1, len(self.cities)-i+1)
        self.fitness = 0.0
    
    # 評価
    def evaluate(self):
        order_list = [i for i in range(1, len(self.cities)+1)] # 順序リスト
        visit_order = [] # 実際の巡回順
        for i in range(len(self.cities)):
            t = self.chrom[i]
            visit = order_list[t-1]
            visit_order.append(visit)
            order_list.remove(visit)
        
        # 適応度は訪れる都市間の距離の総和
        for i in range(len(self.cities)-1): # 順番に次の歳までの距離を計算していく
            self.fitness += self.cities[visit_order[i]].Hubeny_distance(self.cities[visit_order[i+1]])
        return self.fitness

    # 交叉
    # とりあえず一点交叉
    def crossover(self, p1, p2):
        point = np.random.randint(len(self.cities)-1)
        for i in range(point+1):
            self.chrom = p1.chrom[i]
        for i in range(point+1, len(self.cities)):
            self.chrom = p2.chrom[i]

    # 突然変異
    def mutate(self):
        for i in range(len(self.cities)):
            if np.random.rand() < Individual.MUTATION_PROB:
                self.chrom[i] = np.random.randint(1, len(self.cities)-i+1)