from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

def getSubinx(row, col):
    #return [int(str(row)+str(col)+str(i)) for i in xrange(1,row*col+1)]
    return [(row, col, i) for i in xrange(1,row*col+1)]

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']

pairs = [(i,j) for i in range(4) for j in range(4) if i < j]
inx = getSubinx(2, 3) 
subs = map(lambda x:plt.subplot(*x), inx)

print subs
print pairs

for i in xrange(6):
    plt.sca(subs[i])
    m = pairs[i]
    for t,marker,c in zip(xrange(3),">ox","rgb"):
        plt.scatter(features[target == t,m[0]],
            features[target == t,m[1]],
            marker=marker,
            c=c)
plt.show()

