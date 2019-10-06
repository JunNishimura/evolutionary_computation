from Population import Population
from Individual import Individual
from datetime import datetime
import random
import matplotlib.pyplot as plt 
import numpy as np

n_rows = 2
n_cols = 2
graph = (n_rows, n_cols)

# 進化過程でのfitnessの更新具合を可視化する
# title: graph title
# fitness: best fitness of each generation
# start: start generation to draw a graph
# order: order to draw a graph
def visualize_evolution(title, fitness, titles, start): 
    _, axes = plt.subplots(nrows=graph[0], ncols=graph[1], figsize=(10, 8))
    
    for i in range(graph[0]):
        for j in range(graph[1]):
            x = np.arange(start, Individual.GEN_MAX)
            axes[i, j].plot(x, fitness[i*2+j])
            axes[i, j].set_title(titles[i*2+j])
            axes[i, j].set_xticks(np.arange(0, Individual.GEN_MAX+1, 100))
            axes[i, j].set_xlabel('世代')
            axes[i, j].set_ylabel('最良適応度') 
            # axes[i, j].set_xlim(0, Individual.GEN_MAX+1)
            # axes[i, j].set_ylim(0, fitness[i*2+j][start])
            axes[i, j].text(Individual.GEN_MAX+1-Individual.GEN_MAX//10, fitness[i*2+j][-1]*2.25, "best fitness\n{0:.8f}".format(fitness[i*2+j][-1]))
            axes[i, j].grid(True)
    plt.tight_layout()
    plt.show()
    # plt.savefig('ouput.png')

def main():
    g_start = 0 # starting generation to draw a graph
    fitness = []
    titles = ["順位に基づくランキング選択", "確率に基づくランキング選択", "ルーレット選択", "トーナメント選択"]
    for j in range(4):
        tmp = []
        pop = Population()
        random.seed(datetime.now())
        for i in range(1, Individual.GEN_MAX+1):
            pop.alternate(j)
            if i > g_start:
                tmp.append(pop.ind[0].fitness)
            # print("第{}世代: 最良適応度{}".format(i, pop.ind[0].fitness))
        pop.printResult()
        fitness.append(tmp)
    # visualize evolution
    visualize_evolution(titles, fitness, titles, g_start)

if __name__ == "__main__":
    main()