import numpy1 as np
array1 = np.random.randint(1, 100, size = 5)
array2 = np.random.randint(1, 100, size = (2,2))
print(array1)
print(array2)
con = np.concatenate((array1, array2), axis = None)
print(con)