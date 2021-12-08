import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as ani
import numpy as np
import time

df = pd.read_csv("Thu Dec  9 01-11-57 2021.csv")

fig= plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(0,50),ylim=(0,50))
coly = df.columns[1::2]
colx = df.columns[2::2]
i = 0
y = list(df[coly[i]])
x = list(df[colx[i]])
scat = plt.scatter(y,x)
def Update(*args):
    global x,y,i
    if i < len(coly)-1:
        i += 1
        y = list(df[coly[i]])
        x = list(df[colx[i]])
        data = [y,x]
        data = np.reshape(data, (len(y),2))
        scat.set_offsets(data)
    return scat

anim = ani.FuncAnimation(fig, Update, interval = 1000/60, save_count=9999)
t = f"{time.asctime()}.mp4".split(":")
new_anim = "-".join(t)
new_anim = "Animation " +new_anim
writergif = ani.FFMpegWriter(fps=60) 
anim.save(new_anim, writer=writergif)


#plt.show()
