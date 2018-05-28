#coding=utf-8
#__author__='liufeismart'
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

plt.figure(figsize=(16,8))
# 根据经纬度显示地图内容
# m=Basemap() #世界地图
m=Basemap(llcrnrlon=73,llcrnrlat=18,urcrnrlon=135,urcrnrlat=53)
m.drawcoastlines()
m.drawcountries(linewidth=1.5)
# 中国地图中省描边，导入gadm36_CHN_2，获取省份信息
# https://gadm.org/download_country_v3.html 各国的行政区划Shape文件
m.readshapefile('gadm36_CHN_shp/gadm36_CHN_1','states',drawbounds=True)
# 上色
from matplotlib.patches import Polygon
ax=plt.gca()
for nshape, seg in enumerate(m.states):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)
#台湾上色
m.readshapefile('gadm36_TWN_shp/gadm36_TWN_0','taiwan',drawbounds=True)
for nshape, seg in enumerate(m.taiwan):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)
#获取各省名字
# for shapedict in m.states_info:
#     statename = shapedict['NL_NAME_1']
#     p = statename.split('|')
#     if len(p) > 1:
#         s = p[1]
#     else:
#         s = p[0]
#     print(s)
# for shapedict in m.taiwan_info:
#     s = shapedict['NAME_CHINE']
#     print(s)

plt.show()


