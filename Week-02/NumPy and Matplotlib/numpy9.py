import numpy1 as np
matrix = np.random.randint(1, 100, size = (3,3))
print("Eigenvalues:", np.linalg.eigvals(matrix))
print("Eigenvectors:", np.linalg.eig(matrix))
