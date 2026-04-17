#to implement KNN and K means clustering for supervised and unsupervised learning.

import math #KNN 
from collections import Counter

data = [
    (40, 36, 'viral'),
    (30, 30, 'viral'),
    (32, 45, 'viral'),
    (37, 55, 'viral'),
    (40, 47, 'viral'),
    (52, 40, 'viral'),
    (48, 59, 'bacterial'),
    (60, 67, 'bacterial'),
    (68, 50, 'bacterial'),
    (40, 65, 'bacterial'),
    (55, 55, 'bacterial'),
    (58, 58, 'bacterial')
]

def euclidean(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def knn_predict(new_point, k=3):
    distances = []

    for point in data:
        dist = euclidean(new_point, (point[0], point[1]))
        distances.append((dist, point[2]))

    distances.sort(key=lambda x: x[0])

    neighbors = distances[:k]

    labels = [label for _, label in neighbors]
    return Counter(labels).most_common(1)[0][0]

new_patient = (62, 50)
print(knn_predict(new_patient, k=3))


#K means

import math
import random

points = [
    (40, 36),
    (30, 30),
    (32, 45),
    (37, 55),
    (40, 47),
    (52, 40),
    (48, 59),
    (60, 67),
    (68, 50),
    (40, 65),
    (55, 55),
    (58, 58)
]

points = [(x, y) for x, y, _ in data]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def mean(points):
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)
    return (x, y)

def kmeans(points, k=2, iterations=10):
    centroids = random.sample(points, k)

    for _ in range(iterations):
        clusters = [[] for _ in range(k)]

        for p in points:
            distances = [distance(p, c) for c in centroids]
            idx = distances.index(min(distances))
            clusters[idx].append(p)
        new_centroids = []

        for i in range(k):
            if clusters[i]: 
                new_centroids.append(mean(clusters[i]))
            else:
                new_centroids.append(centroids[i]) # Keep old centroid if cluster is empty

        if new_centroids == centroids :
         break
        centroids = new_centroids


    return centroids, clusters

centroids, clusters = kmeans(points, k=2)
print(f"final centers : {centroids}")
print(f"number of points in cluster 1 : {len(clusters[0])}")
print(f"number of points in cluster 2 : {len(clusters[1])}")