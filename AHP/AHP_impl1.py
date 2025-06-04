import numpy as np
import pandas as pd

# Define pairwise comparison matrix for criteria
criteria_matrix = np.array([
    [1, 3, 5],
    [1/3, 1, 2],
    [1/5, 1/2, 1]
])

# Normalize the matrix
criteria_weights = criteria_matrix.sum(axis=0)
criteria_normalized = criteria_matrix / criteria_weights
criteria_priority_vector = criteria_normalized.mean(axis=1)

# For each criterion, define pairwise comparison matrix for alternatives
# Example: Climate
climate_matrix = np.array([
    [1, 5, 2],
    [1/5, 1, 1/3],
    [1/2, 3, 1]
])
climate_weights = climate_matrix.sum(axis=0)
climate_normalized = climate_matrix / climate_weights
climate_priority_vector = climate_normalized.mean(axis=1)

# Similarly, define for Sightseeing and Environment

# Combine results (assuming you have all priority vectors)
# Let's say:
# climate_priority_vector = [0.6, 0.1, 0.3]
# sightseeing_priority_vector = [0.3, 0.6, 0.1]
# environment_priority_vector = [0.2, 0.2, 0.6]

# Combine them (for demo, using made-up vectors)
priority_vectors = np.array([
    [0.6, 0.1, 0.3],
    [0.3, 0.6, 0.1],
    [0.2, 0.2, 0.6]
])

# Multiply by criteria weights (for demo, using made-up criteria_priority_vector)
criteria_priority_vector = np.array([0.6, 0.3, 0.1])

final_scores = priority_vectors.T @ criteria_priority_vector

print("Final scores for alternatives:", final_scores)
