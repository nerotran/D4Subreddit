import matplotlib.pyplot as plt
import numpy as np

stat = [0,0,0]
labels = ['Actual complaints\n', 'Complaints about complaints\n', "Others"]

with open('data') as file:
    for line in file:
    	if line in labels:
    		stat[labels.index(line)] += 1
    	else:
    		stat[2] += 1

y = np.array(stat)

plt.pie(y, labels = labels, autopct='%1.1f%%')
plt.title('Diablo 4 Subreddit Post Types (Out of 200+ top posts)')
plt.show()