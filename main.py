import matplotlib.pyplot as plt
import numpy as np

stat = []
labels = []

with open('data') as file:
    for line in file:
    	if line in labels:
    		stat[labels.index(line)] += 1
    	else:
    		labels.append(line)
    		stat.append(1)

y = np.array(stat)

plt.pie(y, labels = labels, autopct='%1.1f%%')
plt.title('Diablo 4 Subreddit Post Types')
plt.show()