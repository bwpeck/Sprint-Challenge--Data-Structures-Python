import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('/Users/benjaminwade/Documents/Git/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('/Users/benjaminwade/Documents/Git/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
tree = BinarySearchTree(names_1[0])
for name_1 in names_1:
    tree.insert(name_1)

for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)

# Time Complexity of original solution is O(n^2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
