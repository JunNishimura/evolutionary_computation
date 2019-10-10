import numpy as np
from City import City

'''
解の表現方法には順序表現(order representation)を用いる
'''
class Individual:
    GEN_MAX = 200 # 世代交代数
    POP_SIZE = 100 # 個体群数
    ELITE = 1 # エリート保存戦略
    MUTATION_PROB = 0.01 # 突然変異の確率

    def __init__(self, cities):
        self.chrom = []
        self.cities = cities
        # 順序表現
        # i番目の遺伝子は1以上N-(i-1)以下の数字が入っている
        for i in range(len(self.cities)):
            self.chrom.append(np.random.randint(1, len(self.cities)-i+1))
        self.fitness = 0.0
    
    # 評価
    def evaluate(self):
        self.fitness = 0.0
        order_list = [i for i in range(1, len(self.cities)+1)] # 順序リスト
        visit_order = [] # 実際の巡回順
        for i in range(len(self.cities)):
            t = self.chrom[i]
            visit = order_list[t-1]
            visit_order.append(visit)
            order_list.remove(visit)
        
        # 適応度は訪れる都市間の距離の総和
        for i in range(len(self.cities)-1): # 順番に次の都市までの距離を計算していく
            self.fitness += self.cities[visit_order[i]-1].Hubeny_distance(self.cities[visit_order[i+1]-1])
        return round(self.fitness * 1000) # 単位はkmに変換して、小数点以下切り捨て

    # 一点交叉
    def onepoint_crossover(self, p1, p2):
        point = np.random.randint(len(self.cities)-1)
        for i in range(point+1):
            self.chrom[i] = p1.chrom[i]
        for i in range(point+1, len(self.cities)):
            self.chrom[i] = p2.chrom[i]

    # 二点交叉
    def twopoint_crossover(self, p1, p2):
        point1 = np.random.randint(len(self.cities)-1) # 1~都市数-2 の中からランダムに選ぶ
        point2 = (point1 + 1 + np.random.randint(len(self.cities)-2)) % (len(self.cities) - 1) # point1以外の数からランダムに選ぶ
        if point1 > point2: # point1 < point2にする
            tmp = point1
            point1 = point2
            point2 = tmp
        for i in range(point1+1):
            self.chrom[i] = p1.chrom[i]
        for i in range(point1+1, point2+1):
            self.chrom[i] = p2.chrom[i]
        for i in range(point2+1, len(self.cities)):
            self.chrom[i] = p1.chrom[i]
    
    # 一様交叉
    def uniform_crossover(self, p1, p2):
        for i in range(len(self.cities)):
            if np.random.randint(2) == 0:
                self.chrom[i] = p1.chrom[i]
            else:
                self.chrom[i] = p2.chrom[i]

    # 突然変異
    def mutate(self):
        for i in range(len(self.cities)):
            if np.random.rand() < Individual.MUTATION_PROB:
                self.chrom[i] = np.random.randint(1, len(self.cities)-i+1)