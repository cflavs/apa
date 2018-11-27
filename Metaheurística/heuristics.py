import numpy as np
from kmeans import *

def vnd(classes, centroids,distances,X,r):
    #centroids = initialize_clusters(X, r)
    #maxiter = 300
    #classes = np.zeros(X.shape[0], dtype=np.int)
    #distances = np.ones([X.shape[0], r], dtype=np.float64)
    d = np.ones([X.shape[0], r], dtype=np.float64)
    #d*=1000
    k = 0
    s = np.zeros((r,2))
    ds = np.zeros(r)
    sindex = np.zeros(r)
    s_ = np.zeros((r,2))
    ds_ = np.zeros(r)
    s_index = np.zeros(r) 
    s_ = centroids
    #for i, c in enumerate(centroids):
    #    d[:, i] = get_distances(c, X)
    #for i in range(r):
    #    s[i] = X[np.argmin(d[:,i])]
    #    ds[i] = d[np.argmin(d[:,i]),i]
    #    sindex[i] = np.argmin(d[:,i])
    while k < r:
        classes,centroids,d = k_means(centroids,X,d,classes,k)
        for i, c in enumerate(centroids):
            d[:, i] = get_distances(c, X)
        for i in range(r):
            s_[i] = X[np.argmin(d[:,i])]
            ds_[i] = d[np.argmin(d[:,i]),i]
            s_index[i] = np.argmin(d[:,i])
        if(ds_[k]<ds[k]):
            aux = s[k]
            X[sindex[k]] = s_[k]
            X[s_inndex[k]] = aux
            centroids[k] = s_[k]
            k = 0
    #    if (d[:,k] < distances[:,k]).any():
    #        distances[:,k] = d[:,k]
    #        centroids = cent
    #        k = 0
        else: 
            k+=1
    group_colors =  ['blue', 'red', 'green','violet','yellow', 'purple','grey','olive','navy', 'cyan']
    colors = [group_colors[j] for j in classes]

    fig, ax = plt.subplots(figsize=(4,4))
    ax.scatter(X[:,0], X[:,1], color=colors)
    ax.scatter(centroids[:,0], centroids[:,1], color='black', marker='o', lw=2)
    ax.set_xlabel('$x_0$')
    ax.set_ylabel('$x_1$');
    plt.show()
centers = [[1, 1], [-1, -1], [1, -1]]
X, y = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
k = 3
classes, centroids,distances,X,k = main()
vnd(classes, centroids,distances,X,k)