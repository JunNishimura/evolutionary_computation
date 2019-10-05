import numpy as np 

class Individual:
    # define class variable
    GEN_MAX = 1000 # 世代交代数
    POP_SIZE = 100 # 個体群のサイズ
    ELITE = 1 
    MUTATE_PROB = 0.01
    N = 64 # 最大数の平方数
    TOURNAMENT_SIZE = 30 # トーナメントサイズ

    def __init__(self):
        self.chrom = []
        for _ in range(Individual.N):
            self.chrom.append(np.random.randint(100) % 2)
        self.fitness = 0.0

    # 評価
    def evaluate(self):
        self.fitness = 0.0
        for i in range(Individual.N):
            self.fitness += (self.chrom[i] * 2 - 1) * np.sqrt(i + 1)
        self.fitness = abs(self.fitness)
        
    # 1点交叉
    def crossover_onepoint(self, p1, p2):
        point = np.random.randint(Individual.N-1) #0以上N-2以下から１つ
        for i in range(point+1):
            self.chrom[i] = p1.chrom[i]
        for i in range(point+1, Individual.N):
            self.chrom[i] = p2.chrom[i]

    # 2点交叉
    def crossover_twopoint(self, p1, p2):
        point1 = np.random.randint(Individual.N-1)
        point2 = (point1 + 1 + np.random.randint(Individual.N-2)) % (Individual.N-1)
        if point1 > point2:
            t = point1
            point1 = point2
            point2 = t
        for i in range(point1+1):
            self.chrom[i] = p1.chrom[i]
        for i in range(point1+1, point2+1):
            self.chrom[i] = p2.chrom[i]
        for i in range(point2+1, Individual.N):
            self.chrom[i] = p1.chrom[i]
            
    # 一様交叉
    def crossover_uniform(self, p1, p2):
        for i in range(Individual.N):
            if np.random.randint(2) == 1:
                self.chrom[i] = p1.chrom[i]
            else:
                self.chrom[i] = p2.chrom[i]

    # 突然変異を起こす
    def mutate(self):
        for i in range(Individual.N):
            if np.random.rand() < Individual.MUTATE_PROB:
                self.chrom[i] = 1 - self.chrom[i]