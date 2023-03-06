# python3
import sys
import threading
#import numpy as np
import os.path

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
    try:
        veids = input
        if veids == 'F':
            filename = input()
            
            if 'a' in filename or 'A' in filename:
                return
            if filename[0].isdigit():
                if not os.path.exists(filename):
                    return
                with open(filename, 'r', encoding='utf-8') as file:
                    n = int(file.readline().strip())
                    parents = list(map(int, file.readline().strip().split()))
        elif veids == 'I':
                n = int(input())
                parents = list(map(int, input().split()))
        else:
            return
        if n < 1 or n > 105:
            return
        if any(p < -1 or p >= n for p in parents):
            return
        print(compute_height(n,parents))

    except EOFError:
        return 1

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
