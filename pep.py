from os import remove
import time
from itertools import product

gearsfree = [9,13]
allgears = [8,9,10,13,16]
dynamicshiftercount = 4

h1 = []
for i in gearsfree:
    for j in allgears:
        for ii in gearsfree:
            for jj in allgears: 
                a = [(i, ii), (j, jj)]
                h1.append(a)

total_combos = len(h1)**dynamicshiftercount
histori = []

for i, item in enumerate(product(h1, repeat=dynamicshiftercount)):
    histori.append(list(item))
    
    # Print progress every 1000 items (to avoid slowing down the script)
    if i % 1000 == 0 or i == total_combos - 1:
        percent = (i + 1) / total_combos * 100
        print(f"\rGenerating Histori: {percent:.1f}%", end="")
"""
for i in range(0, len(h1)):
    for j in range(0, len(h1)):
        for l in range(0, len(h1)):
            histori.append([h1[i],h1[j],h1[l]])"""

#histori[i] ~= [[(13, 13), (13, 13)], [(13, 13), (13, 13)], [(13, 13), (13, 13)]]
#[(13, 13), (13, 13)]
#(13, 13)
#print(histori)
gearratios = []
startingrpm = 1.25
#histori[0][0][1] (0,0) 

"""for i in range(0, len(histori)):
    percent = (i + 1) / len(histori) * 100
    print(f"\r{percent:.1f}%", end="")
    t1 = []
    t1.extend([histori[i][0][0][0]/histori[i][0][1][0]*startingrpm])
    t1.extend([histori[i][0][0][1]/histori[i][0][1][1]*startingrpm])
    t2 = []
    for j in range(0,2):
        t2.extend([t1[j]*(histori[i][1][0][0]/histori[i][1][1][0])])
        t2.extend([t1[j]*(histori[i][1][0][1]/histori[i][1][1][1])])
    t3 = []
    for n in range(0,4):
        t3.extend([t2[n]*(histori[i][2][0][0]/histori[i][2][1][0])])
        t3.extend([t2[n]*(histori[i][2][0][1]/histori[i][2][1][1])])
    t3.sort()
    t3 = list(set(t3))
    gearratios.append(t3)"""

for i in range(len(histori)):
    percent = (i + 1) / len(histori) * 100
    print(f"\r{percent:.1f}%", end="")
    
    current_layer = [startingrpm]
    
    for stage in histori[i]:
        next_layer = []
        
        ratio_a = stage[0][0] / stage[1][0]
        ratio_b = stage[0][1] / stage[1][1]
        
        for val in current_layer:
            next_layer.append(val * ratio_a)
            next_layer.append(val * ratio_b)
            
        current_layer = next_layer

    final_gears = sorted(list(set(current_layer)))
    gearratios.append(final_gears)


for i in range(0,len(gearratios)):

    for j in range(0, len(gearratios[i])):
        gearratios[i][j] = round(gearratios[i][j], 3) 
    gearratios[i].sort()

filted = []
histor = []
for i in range(0, len(gearratios)):
    percent = (i + 1) / len(gearratios) * 100
    print(f"\r{percent:.1f}%", end="")
    if(len(gearratios[i]) > 7):
        if True:
            
            filted.append(gearratios[i])
            histor.append(histori[i])
gearratios.clear()
histori.clear()

filted_deduped = []
histor_deduped = []
seen = set()

for i in range(len(filted)):
    percent = (i + 1) / len(filted) * 100
    print(f"\r{percent:.1f}%", end="")
    # Convert list to tuple so it can be checked in a set
    item_tuple = tuple(filted[i])
    
    if item_tuple not in seen:
        seen.add(item_tuple)
        filted_deduped.append(filted[i])
        histor_deduped.append(histor[i])
        



with open("real.txt", "w") as f:
    for i in range(0, len(filted_deduped)):
        percent = (i + 1) / len(filted_deduped) * 100
        print(f"\r{percent:.1f}%", end="")
        f.write(str(filted_deduped[i]) + str(histor_deduped[i]) + "\n")
print(len(filted_deduped))
