import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
def largest_eigenvector(probability_matrix):
    #Start with random vector and get largest eigenvector out of probability
    vec = np.zeros(len(probability_matrix)) + 1
    for i in range(5):
        vec = probability_matrix@vec
        vec = vec/(la.norm(vec))
    return vec

xs = np.random.random(50)
ys = np.random.random(50)

xs = np.concatenate((xs, np.random.random() + np.random.random(20)/5))
ys = np.concatenate((ys, np.random.random() + np.random.random(20)/5))

coords = []
for i in range(70):
    coords.append([xs[i],ys[i]])
coords = np.array(coords)

plt.scatter(xs,ys)
plt.show()

adj = np.zeros((70,70))
for i in range(70):
    for j in range(i):
        adj[i][j] = 1/la.norm(coords[i]-coords[j])
        adj[j][i] = 1/la.norm(coords[i]-coords[j])

maxc = coords[np.argmax(largest_eigenvector(adj))]
plt.scatter(xs,ys)
plt.scatter([maxc[0]],[maxc[1]],c='red')
plt.show()