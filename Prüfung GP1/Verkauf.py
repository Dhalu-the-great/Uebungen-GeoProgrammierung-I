import matplotlib.pyplot as plt
from math import *
import numpy as np
import matplotlib.dates as mdates



monate=np.linspace(1,12,12)
verkaufszahlen=[1500, 1800, 2000, 2200, 2100, 1900, 2300, 2400, 2500, 2800, 2700, 2900]
locator=mdates.MonthLocator()
monate=["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
print(monate)

plt.plot(monate,verkaufszahlen,"k-")
plt.xlabel("Monat")
plt.ylabel("Verkaufszahlen in CHF")
plt.title("Verkaufszahlen im Jahr 2022")


plt.show()