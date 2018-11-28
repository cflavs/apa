import numpy as np
from kmeans import *
from sklearn import datasets
def vns(centroid,X,num_clusters,distances,classes,y):
    d = np.array([[0 for _ in range(x)] for x in [sum(y == (i)) for i in range(num_clusters)]])
    print(d.shape)
    k = 0
    ssd = []
    ssd_ = []
    media = []
    media_ = []
    index = np.zeros(X.shape[0])
    for i in range(num_clusters):
        ssd.append(np.sum((X-centroid[i])**2))
        ssd_.append(0)
        media.append(np.mean(distances[:,i]))
        media_.append(0)
    for i in range(100):
        k=0
        while k < num_clusters:
            centroids = initialize_clusters(X, num_clusters)
            for i, c in enumerate(centroids):
                d[i] = get_distances(c, X[y==i])
                media_[i] = np.mean(d[i])
            for i in range(num_clusters):
                if media_[i] < media[i]:
                    media[i] = media_[i]
                    centroid[i] = centroids[i]
                    k=0
            else: 
                k +=1
    distances = np.zeros([X.shape[0], k], dtype=np.float64)
    for i, c in enumerate(centroids):
        distances[:, i] = get_distances(c, X)
    classes = np.argmin(distances, axis=1)
    return classes, centroid


classes, centroids,distances,X,k,y = main()
classes, centroids = vns(centroids,X,k,distances,classes,y)
group_colors = ['blue', 'red', 'green','violet','yellow', 'purple','grey','olive','navy', 'cyan']
colors = [group_colors[j] for j in classes]

fig, ax = plt.subplots(figsize=(4,4))
ax.scatter(X[:,0], X[:,1], color=colors)
ax.scatter(centroids[:,0], centroids[:,1], color='black', marker='o', lw=2)
ax.set_xlabel('$x_0$')
ax.set_ylabel('$x_1$');
plt.show()