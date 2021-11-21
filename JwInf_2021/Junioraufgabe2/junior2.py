file = open("praeferenzen5.txt")
firstLine = file.readline().strip().split()

""" n Mitglieder """
n = int(firstLine[0])
""" m Termine """
m = int(firstLine[1])
""" nxm Präferenzen """
p = file.read().splitlines()
for i in range(len(p)):
    p[i] = p[i].split()
    p[i] = [int(x) for x in p[i]]

""" Berechnet für jedes Mitglied den Value für den beliebtesten Termin """
minValues = [0 for i in range(n)]
for i in range(len(p)):
    minValues[i] = min(p[i])

""" Zählt wie viele Änderungen pro Termin gemacht werden müssen, sodass Termin für jedes Mitglied am besten gefällt """
changes = [0 for i in range(m)]
for termin in range(m):
    for mitglied in range(n):
        if p[mitglied][termin] > minValues[mitglied]:
            changes[termin] += 1

result = min(changes)

minTerminIndex = changes.index(result)
resultTermin = []
for i in range(n):
    resultTermin.append(p[i][minTerminIndex])

print("Es müssen mindestens " + str(result) + " Einträge verändert werden.")
print("Der Termin dafür lautet:")
print(resultTermin)
