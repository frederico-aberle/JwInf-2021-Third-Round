import math

file = open("landkreis4.txt")
firstLine = file.readline().strip().split()

""" n Häuser """
n = int(firstLine[0])
""" m Windräder """
m = int(firstLine[1])
""" n Positionen der Häuser """
h = []
for i in range(n):
    temp = file.readline().strip().split()
    h.append([int(temp[0]), int(temp[1])])
# print(h)
""" m Positionen der Windräder """
w = []
for i in range(m):
    temp = file.readline().strip().split()
    w.append([int(temp[0]), int(temp[1])])
# print(w)
""" Berechnen der maximalen Höhe der Windräder """
result = []
for x in w:
    minD = float('inf')
    for y in h:
        d = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2) # Berechnen des Abstands zwischen einem Haus und dem Windrad
        if d < minD:
            minD = d
            temp = y
    result.append(minD/10.0)
print("Liste der maximalen Höhe aller Windräder:")
print(result)
