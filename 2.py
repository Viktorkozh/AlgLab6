#!/usr/bin/env python3 
#coding: utf-8 -*-

import random


a = []
list = []
solution = []
segLength = 5


def filllist(numOfEl):
    list.clear()
    for _ in range(numOfEl):
        first = random.randint(0, 100)
        second = first + random.randint(1, 40)  # Генерируем правый конец отрезка
        list.append((first, second))


def actsel(s):
    solution = []
    while len(s) > 0:
        lmin, rmin = s[0][0], s[0][1] 
        for seg in s:
            if seg[1] < rmin:
                lmin, rmin = seg[0], seg[1]
                
        solution.append([lmin, rmin])
        
        s = [x for x in s if x[0] > rmin or x[1] < lmin]
    return solution


def actsel1(s):
    s.sort(key=lambda x: x[1])
    sol = []
    while len(s) > 0:
        lmin, rmin = s[0]
        sol.append([lmin, rmin])
        # удаление отрезков, пересекающиеся с [lmin, rmin]
        s = [x for x in s if x[0] > rmin]
    return sol


if __name__ == '__main__':
    filllist(20)
    print("Отрезки: ", sorted(list))
    list1 = list.copy()
    print("Отрезки непересекающиеся", actsel(list))
    print("Отрезки непересекающиеся", actsel1(list1))