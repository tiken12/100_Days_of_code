import numpy as np
import pandas as pd
from scipy.spatial import distance
from scipy.spatial.distance import cosine, euclidean

# Define two random vectors manual input (given vectors)
#p1 = np.array([2, 2, 1, 7, 3])
#p2 = np.array([3, 6, 4, 0, 2])

#Define two random vectors autogenerate
p1 = np.random.randn(20)
p2 = np.random.randn(20)

# Calculate Correlation using corrcoef
correlation = np.corrcoef(p1, p2)[0, 1]

# Calculate Cosine Similarity using dot product
cosine_similarity = np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2))

# Calculate Euclidean Distance using linear algebra for two points
euclidean_distance = np.linalg.norm(p2-p1)

# Printing the two vectors, the correlation, the cosine similarity, and the euclidean distance.
print("p1:", p1)
print("p2:", p2)
print("Correlation:", correlation)
print("Cosine Similarity:", cosine_similarity)
print("Euclidean Distance:", euclidean_distance)