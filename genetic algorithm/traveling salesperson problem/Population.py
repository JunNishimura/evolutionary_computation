from Individual import Individual

class Population:
    def __init__(self, num_cities):
        self.ind = []
        self.nextInd = []
        for _ in range(Individual.POP_SIZE):
            self.ind.append(Individual(num_cities))
        self.evaluate()

    # 世代交代
    def alternate(self):
        pass

    # 結果表示
    def printResult(self):
        pass

    # 親個体の選択
    def select(self):
        pass

    def evaluate(self):
        pass