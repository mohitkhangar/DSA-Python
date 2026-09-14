import numpy as np
np1 = np.array([10, 20, 30, 40, 50])
np2 = np.array([60, 70, 80, 90, 100])

print(np1)
print(np2)

# traversal
for element in np1:
    print(element, end=' ')

# insertion
np.insert(np1, 2, 35)
print("\nAfter insertion: ", np1)

# deletion
np.delete(np1, 2)
print("After deletion:", np1)

#updation
np1[2] = 30
print(np1)

#sorting

np3 = np.array([4,6,0,4,6,1,5])
print(np3)

print(np.sort(np3))

#merging
np4 = np.concatenate((np1, np2))
print(np4)

#splitting

print(np.array_split(np4, 2))