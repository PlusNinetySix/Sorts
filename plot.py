import sort
import matplotlib.pyplot as plt
from random import sample
from time import perf_counter

#Generates numbers up to 20000.
randnum = sample(range(20000), k=20000)

#This function starts the timer, and is measured in milliseconds.
def timer(algorithm, randnum):
    start = perf_counter()
    algorithm(randnum)
    stop = perf_counter()
    timer = ((stop - start) * 1000)
    return timer

#All of these put the numbers from the algorithms in an array.
y=[]
quick=[]
selection=[]
merge=[]
bubble=[]
insertion=[]

#These for loops put the arrays into a plottable form.
for n in range (1000,20001,1000): 
    y.append(n)
for n in range (1000,20001,1000):
    quick.append(timer(sort.quicksort, randnum[0:n]))
for n in range (1000,20001,1000):
    selection.append(timer(sort.selection_sort, randnum[0:n]))
for n in range (1000,20001,1000):
    merge.append(timer(sort.merge_sort, randnum[0:n]))
for n in range (1000,20001,1000):
    bubble.append(timer(sort.bubble_sort, randnum[0:n]))
for n in range (1000,20001,1000):
    insertion.append(timer(sort.insertion_sort, randnum[0:n]))

#This plots all of the sorting algortihms
plt.plot(quick, y, marker="^", color="purple", label="quick sort")
plt.plot(selection, y, marker="*", color="blue", label="selection sort")
plt.plot(merge, y, marker="p", color="green", label="merge sort")
plt.plot(bubble, y, marker="D", color="yellow", label="bubble sort")
plt.plot(insertion, y, marker="s", color="red", label="insertion sort")

#This sets the labels and turns on the grid, then shows the graph.
plt.xlabel("Time (ms)")
plt.ylabel("Number of Elements")
plt.title("Time of Various Sorting Algorithms")
plt.grid(b='on', which='major', axis='both')
plt.minorticks_on()
plt.legend()
plt.show()
