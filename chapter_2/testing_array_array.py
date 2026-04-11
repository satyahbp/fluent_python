from array import array
from time import time

from pympler import asizeof


a = array("I", [])
b = []

for i in range(10_000_000):
    a.append(i)
    b.append(i)


print(f"\n\nSize of array.array for 10 million ints: {asizeof.asizeof(a)/(1024*1024):.2f}MB")
print(f"Size of list for 10 million ints: {asizeof.asizeof(b)/(1024*1024):.2f}MB\n\n")