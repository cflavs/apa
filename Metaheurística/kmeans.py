import imp 
import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import datasets
def initialize_clusters(points, k):
    return points[np.random.randint(points.shape[0], size=k)]
    
def get_distances(centroid, points):
    return np.linalg.norm(points - centroid, axis=1)
def k_means(centroids,X,distances, classes,k):
    for i, c in enumerate(centroids):
        distances[:, i] = get_distances(c, X)
    classes = np.argmin(distances, axis=1)
    for c in range(k):
        centroids[c] = np.mean(X[classes == c], 0)
    return classes, centroids,distances
def main():
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, y = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
    k = 3
    iris = datasets.load_iris()
    #X = iris.data
    #y = iris.target
    group_colors = ['blue', 'red', 'green','violet','yellow', 'purple','grey','olive','navy', 'cyan']
    colors = [group_colors[j] for j in y]

    fig, ax = plt.subplots(figsize=(4,4))
    ax.scatter(X[:,0], X[:,1], color=colors)
    #ax.scatter(centroids[:,0], centroids[:,1], color='black', marker='o', lw=2)
    ax.set_xlabel('$x_0$')
    ax.set_ylabel('$x_1$');
    plt.show()
    maxiter = 3
    classes = np.zeros(X.shape[0], dtype=np.int)
    distances = np.zeros([X.shape[0], k], dtype=np.float64)
    centroids = initialize_clusters(X, k)
    for i in range(maxiter):
        classes,centroids,distances = k_means(centroids,X,distances,classes,k)
    group_colors = ['blue', 'red', 'green','violet','yellow', 'purple','grey','olive','navy', 'cyan']
    colors = [group_colors[j] for j in classes]

    fig, ax = plt.subplots(figsize=(4,4))
    ax.scatter(X[:,0], X[:,1], color=colors)
    ax.scatter(centroids[:,0], centroids[:,1], color='black', marker='o', lw=2)
    ax.set_xlabel('$x_0$')
    ax.set_ylabel('$x_1$');
    plt.show()
    return classes, centroids,distances,X,k
#main()