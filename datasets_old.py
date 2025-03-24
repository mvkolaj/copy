import numpy as np


print("Datasets Available")
print("-" * 20)
# ################### Binary Tree
depth = 5
N = sum(2 ** i for i in range(depth))
mat = np.zeros((N, N))
for i in range(N):
    j = 2 * i + 1
    if j + 1 >= N:
        break
    mat[i, j] = 1
    mat[i, j + 1] = 1
binary_tree = mat
print("Binary Tree      : binary_tree")


# ################### Quad Tree
depth = 4
N = sum(4 ** i for i in range(depth))
mat = np.zeros((N, N))
for i in range(N):
    j = 4 * i + 1
    if j + 3 >= N:
        break
    mat[i, j] = 1
    mat[i, j + 1] = 1
    mat[i, j + 2] = 1
    mat[i, j + 3] = 1
quad_tree = mat
print("Quad Tree        : quad_tree")


# ################### Co-occurrence matrix (100 playlists)
co_occurrence_100 = np.load("enoa/co_occurrence_mat_100.npy")
print("Co-occurrence    : co_occurrence_100")

# ################### Co-occurrence matrix (100 playlists)
adjacency = np.load("enoa/no_auto_adjacency.npy")
print("Adjacency    : adjacency")

# ################## Co-occurrence matrix (all playlists)
full_adjacency = np.load("enoa/full_adjacency.npy")
full_adjacency = sparse.csr_matrix(full_adjacency)
print("Full adjacency: full_adjacency")

print("-" * 20)

