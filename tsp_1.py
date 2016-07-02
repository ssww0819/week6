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
visited = True * n

route[1] = random.randint(1, n-1)
x = route[1]

for a in range(2, n):
    if (a + x) == n :
        route[a] = x + 1;
    elif (a + x) > n:
        route[a] = a + x -n;
    else :
        route[a] = a + x;

#print route
for i in range(0, n-1):
    sum_distance += distance(cities[route[i]], cities[route[i+1]])

sum_distance += distance(cities[route[n-1]], cities[route[0]])
d_best = sum_distance
route_best = [0] * n

sum1 = 0
y = 0
for b in range(1, n):
    for a in range(b, n):
        sum1 = 0
        y = route[1]
        route[1] = route[a]
        route[a] = y
        for i in range(0, n):
	    c0 = route[i]
	    if i < n - 1:
                c1 =  route[i+1]
            else:
                c1 = route[0]
	    sum1 += distance(cities[c0], cities[c1])

        if sum1 < d_best :
	    d_best = sum1
	for i in range(0, n) :
	    route_best[i] = route[i]
print route_best
print d_best
