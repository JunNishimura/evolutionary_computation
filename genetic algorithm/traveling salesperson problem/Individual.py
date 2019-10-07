class Individual:

    GEN_MAX = 500 # 世代交代数
    POP_SIZE = 100 # 個体群数
    ELITE = 1 # エリート保存戦略
    MUTATION_PROB = 0.01 # 突然変異の確率
    def __init__(self, num_cities):
        self.chrom = []
        self.order_list = [i for i in range(1, num_cities+1)]
        for i in range(num_cities):
            self.chrom[i] = i+1 # 染色体には(1 ~ 都市の数)が入っている

    # 評価
    def evaluate(self):
        pass

    # 交叉
    def crossover(self):
        pass

    # 突然変異
    def mutate(self):
        pass
