import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap

def TEC_plot(data):

    plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置整体的字体为Times New Roman
    plt.figure(figsize=(10, 6), dpi=300)  # 设置大小和分辨率

    # 创建底图，分辨率为高分辨率，地图范围为全球
    m = Basemap(projection='cyl', resolution='l', llcrnrlon=-180, llcrnrlat=-90, urcrnrlon=180, urcrnrlat=90)

    # 设置地图经纬线，并只在左端和底端显示
    m.drawmeridians(np.arange(-180, 181, 30), labels=[0, 0, 0, 1], fontsize=10, linewidth=0.3, color='grey', )  # 经线
    m.drawparallels(np.arange(-90, 90, 30), labels=[1, 0, 0, 0], fontsize=10, linewidth=0.3, color='grey')  # 纬线


    # 创建经纬度网格
    lon = np.linspace(-180, 180, 73)
    lat = np.linspace(-87.5, 87.5, 71)
    lon, lat = np.meshgrid(lon, lat)

    # 绘制全球TEC图像
    levels = [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150]  # 创建分级
    color = ['#1e33b8', '#1e5cb3', '#3068a7', '#658d81', '#779a74', '#9ab25b', '#becb42', '#d0d736', '#e1e42a',
            '#f3f01d']  # 设置色带
    m.contourf(lon, lat, data,colors=color,levels=levels)  # 绘图，并设置图例两端显示尖端
    m.drawcoastlines(linewidth=0.5)
    cb = m.colorbar(location='right', pad=0.1, size = 0.2)  # 图例在右侧显示
    cb.ax.tick_params(labelsize=10)  # 刻度字号大小
    cb.set_label('TECU', fontsize=10)  # 设置图例名称和字体大小
    plt.title('Global TEC')