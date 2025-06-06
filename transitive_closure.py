# -*- coding: utf-8 -*-
"""transitive_closure.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EuGRTuTTTdWbK3sa4CrZP6hZVYL3uMNX

Transitive closure using Warshall's Algorithm
"""

# Warshall's Algorithm for Transitive Closure
def transitive_closure(graph):
    n = len(graph)

    closure = [[graph[i][j] for j in range(n)] for i in range(n)]


    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure


graph = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]


closure = transitive_closure(graph)


print("Transitive Closure:")
for row in closure:
    print(row)

