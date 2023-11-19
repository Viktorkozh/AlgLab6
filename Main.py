#!/usr/bin/env python3 
#coding: utf-8 -*-

import random


a = []
arr = []
solution = []
segLength = 5


def fillArr(numOfEl):
    arr.clear()
    for i in range(numOfEl):
        arr.append(random.randint(0, 100))


def pointscover1(a):
    sol = []
    while len(a) > 0:
        xmin = min(a)
        i = 0
        sol.append([xmin, xmin + segLength])
        while i < len(a):
            if sol[-1][0] <= a[i] <= sol[-1][1]:
                a.pop(i)
            else:
                i += 1
    return sol


def pointscover2(a):
    a.sort()
    i = 0
    sol = []
    while i < len(a):
        sol.append([a[i], a[i] + segLength])
        b = a[i]
        i += 1
        while i < len(a) and a[i] <= b + segLength:
            i += 1
    return sol


if __name__ == '__main__':
    fillArr(20)
    print("Точки: ", sorted(arr))
    arr2 = arr.copy()
    print("Отрезки func 1", pointscover1(arr))
    print("Отрезки func 2", pointscover2(arr2))