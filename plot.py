import sort
import matplotlib.pyplot as plt
from random import sample
from time import perf_counter

randnum = sample(range(20000), k=20000)

def timer(algorithm, randnum):
    start = perf_counter()
    algorithm(randnum)
    stop = perf_counter()
    timer = stop - start
    return timer

y=[]
x=[]
z=[]
w=[]
u=[]
o=[]

for n in range (1000,20001,1000): 
    y.append(n)
for n in range (1000,20001,1000):
    x.append(timer(sort.quicksort, randnum[0:n]))
for n in range (1000,20001,1000):
    z.append(timer(sort.selection_sort, randnum[0:n]))
for n in range (1000,20001,1000):
    w.append(timer(sort.merge_sort, randnum[0:n]))
for n in range (1000,20001,1000):
    u.append(timer(sort.bubble_sort, randnum[0:n]))
for n in range (1000,20001,1000):
    o.append(timer(sort.insertion_sort, randnum[0:n]))

plt.plot(x, y, marker="^", color="purple", label="quick sort")
plt.plot(z, y, marker="*", color="blue", label="selection sort")
plt.plot(w, y, marker="p", color="green", label="merge sort")
plt.plot(u, y, marker="D", color="yellow", label="bubble sort")
plt.plot(o, y, marker="s", color="red", label="insertion sort")

plt.xlabel("Time (ms)")
plt.ylabel("Number of Elements")
plt.title("Time of Various Sorting Algorithms")
plt.legend()
plt.show()
