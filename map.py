#coding=utf-8
#__author__='liufeismart'
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(16,8))
m=Basemap(llcrnrlon=73,llcrnrlat=18,urcrnrlon=135,urcrnrlat=53)
m.drawcoastlines()
m.drawcountries(linewidth=1.5)
m.readshapefile('/gadm36_CHN_shp/gadm36_CHN_0','states',drawbounds=True)
plt.show()


from matplotlib.patches import Polygon
ax=plt.gca()
for nshape, seg in enumerate(m.states):
    poly = Polygon(seg, facecolor='r')
    ax.add_patch(poly)