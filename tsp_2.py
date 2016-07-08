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

print route
print sum_distance
