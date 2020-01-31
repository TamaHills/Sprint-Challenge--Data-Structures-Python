import time
import pathlib
from binary_search_tree import BinarySearchTree


# for name_1 in names_1: O(n)
#     for name_2 in names_2:O(K)
#         if name_1 == name_2:
#             duplicates.append(name_1)
# the runtime complexity of this O(nk) 
# where n is the length of list 1 and k is the length of list 2

start_time = time.time()

directory = pathlib.Path(__file__).parent.absolute()

f = open(f'{directory}/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open(f'{directory}/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

tree = BinarySearchTree(names_2[0])
for name in names_2:
    tree.insert(name)

for name in names_1:
    if tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

start_time = time.time()

directory = pathlib.Path(__file__).parent.absolute()

duplicates = set(names_1) & set(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
