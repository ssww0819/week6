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

T = 1500000
rate = 0.9
MIN_TMP = 0.000001
MAX_RANDOM = 10000
d_best = sum_distance
route_best = route
while True:
    sum1 = 0
    exp1 = 0
    T = T*rate
    p = random.randint(0, n-1)
    q = random.randint(0, n-1)
    while p == q :
      q = random.randint(0, n-1)
      
    y = route[p]
    route[p] = route[q]
    route[q] = y
    for i in range(0, n):
        c0 = route[i]
        if i < n-1 :
            c1 = route[i+1]
        else :
            c1 = route[0]
        sum1 += distance(cities[c0], cities[c1])
    print 2

    if (sum1 - d_best)/T <= 800:
        exp1 = math.exp((sum1 - d_best) /float(T))
        randomm = random.randint(0, MAX_RANDOM) + 1
        if exp1 < randomm:
                d_best = sum1
                for i in range(0, n):
	            route_best[i] = route[i]
        
        if sum1 - d_best < 0:
            print 1
            d_best = sum1
            for i in range(0, n):
	        route_best[i] = route[i]

    if T * rate <=MIN_TMP :break 
      
print route
print sum_distance

print route_best
print d_best
