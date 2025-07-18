import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
batsman=pd.read_csv('sharma-kohli.csv')
batsman

plt.plot(batsman['index'],batsman['V Kohli'],c='green',linestyle='dotted',linewidth=4,marker='+',markersize=10)
plt.plot(batsman['index'],batsman['RG Sharma'],c='black',linestyle='dotted',linewidth=4,marker='o',markersize=10)
plt.title('Rohit sharma vs virat kohli')
plt.xlabel('season')
plt.ylabel('runs')
plt.show()