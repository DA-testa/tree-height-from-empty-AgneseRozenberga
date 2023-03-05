# python3
import sys
import threading
#import numpy as np

def compute_height(n, parents):  
    piramida ={}
    for x in range(n):
        if parents[x] == -1:
            root = x
        else:
            if parents[x] not in piramida:
                piramida[parents[x]] = []
            piramida[parents[x]].append(x)

    def augstums(nodes):
        if nodes not in piramida:
            return 1
        else:
            return 1 + max(augstums(pamats) for pamats in piramida[nodes])
    return augstums(root)

def main():
    filename = input()
    if 'a' in filename or 'A' in filename:
        return
    if filename[0].isdigit():
        with open(filename, 'r', encoding='utf-8') as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
    else:
        n = int(input())
        parents = list(map(int, input().split()))
    print(compute_height(n,parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
