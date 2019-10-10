import sys, os 
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
from City import City
from Individual import Individual
from Population import Population

def visualize_evolution(fitness):
    _, axes = plt.subplots(1, 3, figsize=(8, 8))
    for i in range(3):
        x = [i for i in range(0, Individual.GEN_MAX)]
        print(len(x), len(fitness[i]))
        axes[0, i].plot(x, fitness[i])
        axes[0, i].set_xticks(np.arange(0, Individual.GEN_MAX+1, 100))
        axes[0, i].set_xlabel('世代')
        axes[0, i].set_ylabel('最短距離')
        axes[0, i].grid(True)
    plt.tight_layout()
    plt.show()
    
def main():
    # get data from dataset directory
    base = os.path.dirname(os.path.abspath(__file__))
    dataset = os.path.normpath(os.path.join(base, '../../dataset/world_city_data/s55h29megacities_utf8.csv'))

    # 巡回する都市を設定
    df = pd.read_table(dataset, sep='\t', usecols=lambda x: x is not 'note_jp') # column "note_jp"は欠損しているからスキップ
    df.query('country_code == "JP"', inplace=True)
    cities = []
    for name, lat, lon in zip(df['city_en'], df['lat'], df['lon']):
        cities.append(City(name, lat, lon))

    # 最短距離を求める
    fitness = []
    for j in range(3):
        pop = Population(cities)
        tmp = []
        for i in range(1, Individual.GEN_MAX+1):
            pop.alternate(j)
            tmp.append(pop.ind[0].fitness)
            # print("第{}世代: 最短距離{}(km)".format(i, pop.ind[0].fitness)) # 各世代の最短距離を表示
        pop.printResult()
        fitness.append(tmp)
    visualize_evolution(fitness) # matplotlibで可視化する

if __name__ == "__main__":
    main()