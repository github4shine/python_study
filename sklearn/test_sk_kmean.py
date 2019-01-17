from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('data\skmean_data.xls')
x_value = df['x_data']
y_value = df['y_data']
x_data=[]
y_data=[]
dataset=[]
for x1,y1 in zip(x_value,y_value):
        x_data.append(x1)
        y_data.append(y1)
        dataset.append([x1,y1])
        
km = KMeans(n_clusters=5)
cc= km.fit(dataset)

#样本中心
ct=km.cluster_centers_

#每个样本所属的簇
lb=km.labels_

#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
it=km.inertia_

#print(dataset)
print(ct)
print(lb)
print(it)

datasets=[[],[],[],[],[]]
colors=['red','blue','green','black','orange']

for l1,x1,y1 in zip(lb,x_value,y_value):
    datasets[l1].append([x1,y1])

#print(datasets)


#plt.plot(x_data,y_data,'go',label='orgdata')


#绘制散点图，x1，y1，设置颜色，标记点样式和透明度等参数
#plt.scatter(x_data,y_data,color='#9b59b6',marker='.',s=60)

#plt.plot(ct[:,0],ct[:,1],'go',label='ct',color='red')

zset = zip(range(5),colors, datasets) 

for i,col,ad in zip(range(5),colors, datasets):
    print(ad)
    nd = np.array(ad)
    plt.scatter(nd[:,0],nd[:,1],color=col,marker='.',s=60)
    plt.scatter(ct[i,0],ct[i,1],color=col,marker='^',s=60)
    #plt.scatter(ad[:][0],ad[:][1],color=col,marker='.',s=60)
#plt.plot(ct[:,0],ct[:,1],'go',label='ct',color='#9b59b6',marker='^')
#plt.legend()
plt.show()
