import numpy as np

class City:
    equatorial_r = 6378137 # 赤道半径(m)
    polar_r = 6356752 # 極半径(m)
    ecc = np.sqrt(1 - (polar_r/equatorial_r)**2) # 離心率

    def __init__(self, name, lat, lon):
        self.name = name # 都市の名前
        self.lat = lat   # 緯度
        self.lon = lon   # 経度

    # 2都市の距離はヒュベニの公式を用いて計算する
    def Hubeny_distance(self, target_city):
        diff_lat = np.abs(np.deg2rad(self.lat) - np.deg2rad(target_city.lat)) # 緯度の差(ラジアン)
        diff_lon = np.abs(np.deg2rad(self.lon) - np.deg2rad(target_city.lon)) # 経度の差(ラジアン)

        ave_lat = (np.deg2rad(self.lat) + np.deg2rad(target_city.lat)) / 2 # 緯度の平均
        
        w = np.sqrt(1 - pow(City.ecc, 2) * np.sin(ave_lat) * np.sin(ave_lat)) # 子午線曲率半径、卯酉線曲率半径を求める計算で使う
        mr_curv = (City.equatorial_r * (1 - pow(City.ecc, 2))) / np.power(w, 3) # 子午線曲率半径
        pvr_curv = City.equatorial_r / w # 卯酉線曲率半径

        distance = np.sqrt( pow(diff_lat * mr_curv, 2) + pow(diff_lon * pvr_curv * np.cos(ave_lat), 2) ) #2都市間の距離
        return round(distance) # 小数点は切り捨てる