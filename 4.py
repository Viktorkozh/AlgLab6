#!/usr/bin/env python3 
#coding: utf-8 -*-

import random


a = []
list = []
solution = []
totalcost = []


def filllist(numOfEl):
    list.clear()
    for _ in range(numOfEl):
        w = random.randint(10, 500)
        c = random.randint(1, 200)  # Генерируем правый конец отрезка
        list.append((w, c))


def knapsack(a):
    a.sort(key=lambda x: x[1]/x[0])
    for i in range(len(a)):
        freeSpace = 5000
        cnt, tc = 0, 0
        while freeSpace > (0 + a[i][0]):
            freeSpace -= a[i][0]
            cnt += 1
            tc += a[i][1]
        solution.append(cnt)
        totalcost.append(tc)
    return solution, totalcost


if __name__ == '__main__':
    filllist(12)
    print("Предметы (вес, стоимость): ", sorted(list, key=lambda x: x[1] / x[0]))
    sol, total = knapsack(list)
    list.sort(key=lambda x: x[1]/x[0])
    print("\nМесто в рюкзаке = 5000 грамм")
    print("Вес (грамм)\tКоличество поместившихся предметов\tЦена")
    for i in range(len(sol)):
        print(f"{list[i][0]}\t\t\t\t{sol[i]}\t\t\t{total[i]}")