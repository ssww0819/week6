import math
import sys
import random

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


if __name__ == "__main__":
    param = sys.argv

cities = read_input (param[1])
n = len(cities)
route = [0] * n
sum_distance = 0
notvisited = [True] * n
notvisited[0] = False

x = route[0]
MAX = 50000
for i in range(1, n):
    mini = MAX
    for a in range(1, n):
        if notvisited[a] == True:
            if distance(cities[a], cities[route[i-1]]) < mini:
                route[i] = a
                mini = distance(cities[a], cities[route[i-1]])
    notvisited[route[i]] = False
                
for i in range(0, n-1):
    sum_distance += distance(cities[route[i]], cities[route[i+1]])

sum_distance += distance(cities[route[n-1]], cities[route[0]])

d_best = sum_distance
route_best = route[:]
print route
print d_best
while True:
    flag = 0
    for i in range(0, n-2):
        #i1 = i + 1
        for j in range(i + 2, n - 1):
            l1 = distance(cities[route_best[i]], cities[route_best[i+1]])
            l2 = distance(cities[route_best[j]], cities[route_best[j+1]])
            l3 = distance(cities[route_best[i]], cities[route_best[j]])
            l4 = distance(cities[route_best[i+1]], cities[route_best[j+1]])
            if l1 + l2 >  l3 + l4 :
                flag = 1
                route_tmp = route_best[i+1:j+1]
                route_best[i+1:j+1] = route_tmp[::-1]
                d_best = 0
                for a in range(0, n-1):
                    d_best += distance(cities[route_best[a]], cities[route_best[a+1]])
                    d_best += distance(cities[route_best[n-1]], cities[route_best[0]])

    if flag == 0: break
    
#print route
#print sum_distance

print route_best
print d_best
