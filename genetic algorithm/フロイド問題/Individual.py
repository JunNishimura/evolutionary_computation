import numpy as np 

class Individual:
    # define class variable
    GEN_MAX = 1000 # 世代交代数
    POP_SIZE = 1000 # 個体群のサイズ
    ELITE = 1 
    MUTATE_PROB = 0.01
    N = 64 # 最大数の平方数
    TOURNAMENT_SIZE = 30 # トーナメントサイズ

    def __init__(self):
        self.chrom = []
        for _ in range(Individual.N):
            self.chrom.append(np.random.randint(100) % 2)
        self.fitness = 0.0

    def evaluate(self):
        fitness = 0.0
        

    def crossover(self, p1, p2):
        pass

    def mutate(self):
        pass
    
    