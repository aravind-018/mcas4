import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

data, _ = make_blobs(n_samples=300)
data

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init="auto"
).fit(data)

labels = kmeans.labels_
set(labels)

import matplotlib.pyplot as plt

centroids = kmeans.cluster_centers_

plt.scatter(
    data[:, 0],
    data[:, 1],
    c=labels,
    cmap='viridis'
)

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    color="red",
    marker="x"
)

plt.legend(list(labels))

plt.scatter(
    [2, 6],
    [-4, 6],
    color="red"
)

plt.show()

kmeans.predict([[2, -4], [6, 6], [6, -2]])