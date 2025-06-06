# -*- coding: utf-8 -*-
"""binary_search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fpflOgz3rtCqNibyrTlHdT0YHZ2gVsIY
"""

import random
import time
import matplotlib.pyplot as plt

def bin_search(data, target):  #method searching for the target
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


def measure_time(data, target):   #method for measuring time taken for the process each time
    start_time = time.time()
    bin_search(data, target)
    end_time = time.time()
    return end_time - start_time

data = [1000, 2000, 3000, 4000, 5000]   #different data sizes for each iteration
times = []

for i in data:
    search_data = [random.randint(0, 10000) for _ in range(i)]    #generating n(data) random numbers between 1 - 10000
    search_data.sort()
    target = random.randint(0, 10000)
    time_taken = measure_time(search_data, target)
    times.append(time_taken)

plt.plot(data, times, marker='o')
plt.xlabel('Data Size')
plt.ylabel('Time Taken')
plt.title('Binary Search')
plt.show()

