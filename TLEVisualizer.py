from sgp4.api import Satrec
from sgp4.api import jday
import numpy as np
import matplotlib.pyplot as plt

s = []
t= []
tmp= "lorem"

file_loc = input("Enter the file location of the TFL file: ")
with open(file_loc, 'r') as f:
    while(True):
        tmp = f.readline().rstrip('\n')
        if(tmp != ''):
            s.append(f.readline().rstrip('\n'))
            t.append(f.readline().rstrip('\n'))
        else:
            break

satellite = []
for i in range(len(s)):
    satellite.append(Satrec.twoline2rv(s[i], t[i]))


year = int(input("Please enter the year: "))
month = int(input("Please enter the month: "))
day = int(input("Please enter the day: "))
hour = int(input("Please enter the hour: "))
min = int(input("Please enter the min: "))
sec = int(input("Please enter the sec: "))
jd, fr = jday(year, month, day, hour, min, sec)

e= np.zeros(len(satellite))
r= np.zeros((len(satellite), 3))
v= np.zeros((len(satellite), 3))
for t in range(len(satellite)):
    e[t], r[t], v[t] = satellite[t].sgp4(jd, fr)

print(r)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for n in range(len(r)):
    ax.scatter(r[n][0], r[n][1], r[n][2])

plt.show