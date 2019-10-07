import sys, os 
import pandas as pd 

def main():
    # num_cities = 10
    base = os.path.dirname(os.path.abspath(__file__))
    dataset = os.path.normpath(os.path.join(base, '../../dataset/world_city_data/s55h29megacities_utf8.csv'))
    df = pd.read_table(dataset, sep='\t', usecols=lambda x: x is not 'note_jp') # column "note_jp"は欠損しているからスキップ
    

if __name__ == "__main__":
    main()