import sys, os 
import pandas as pd 
from City import City
from Individual import Individual
from Population import Population

def main():
    # num_cities = 10
    base = os.path.dirname(os.path.abspath(__file__))
    dataset = os.path.normpath(os.path.join(base, '../../dataset/world_city_data/s55h29megacities_utf8.csv'))
    df = pd.read_table(dataset, sep='\t', usecols=lambda x: x is not 'note_jp') # column "note_jp"は欠損しているからスキップ
    df.query('country_code == "JP"', inplace=True)

    # 都市を設定
    cities = [] 
    for name, lat, lon in zip(df['city_en'], df['lat'], df['lon']):
        cities.append(City(name, lat, lon))

    # 最短距離を求める
    pop = Population(cities)
    for i in range(1, Individual.POP_SIZE+1):
        print("第{}世代: 最短距離{}(km)".format(i, pop.ind[0].fitness)) # 各世代の最短距離を表示
    pop.printResult()

if __name__ == "__main__":
    main()