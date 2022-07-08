from cProfile import label
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def discharging(V0, t, R, C):
    tau = R * C
    return V0 * math.exp(-t / tau)



np_discharging = np.vectorize(
    discharging, excluded=['V0, R, C'], otypes=[float])

V0 = 3.3
C_VEC = [1e-5, 2e-5] # 10uF, 20uF and 40uF
R_FR5994 = [6050, 4370, 2900] # Minimum resistance at 1MHz, 2MHz and 4MHz.
R_FR5969 = [8518, 6012, 3962]
R_FR2433 = [6484, 4820, 3360]

time_range_start = 0
time_range_stop = 0.12
time_gap = (time_range_stop - time_range_start) / 30

x_ticks = np.arange(
    time_range_start, time_range_stop + time_gap, time_gap)

y_FR5994_R1 = [[discharging(V0, x, R_FR5994[0], c) for x in x_ticks] for c in C_VEC]
y_FR5994_R2 = [[discharging(V0, x, R_FR5994[1], c) for x in x_ticks] for c in C_VEC]
y_FR5994_R3 = [[discharging(V0, x, R_FR5994[2], c) for x in x_ticks] for c in C_VEC]

y_FR5969_R1 = [[discharging(V0, x, R_FR5969[0], c) for x in x_ticks] for c in C_VEC]
y_FR5969_R2 = [[discharging(V0, x, R_FR5969[1], c) for x in x_ticks] for c in C_VEC]
y_FR5969_R3 = [[discharging(V0, x, R_FR5969[2], c) for x in x_ticks] for c in C_VEC]

y_FR2433_R1 = [[discharging(V0, x, R_FR2433[0], c) for x in x_ticks] for c in C_VEC]
y_FR2433_R2 = [[discharging(V0, x, R_FR2433[1], c) for x in x_ticks] for c in C_VEC]
y_FR2433_R3 = [[discharging(V0, x, R_FR2433[2], c) for x in x_ticks] for c in C_VEC]


plt.subplot(2, 3, 1)
plt.plot(x_ticks * 1e3, y_FR5994_R1[0], 'o-',  label="MSP430FR5994")
plt.plot(x_ticks * 1e3, y_FR5969_R1[0], 'o-', label="MSP430FR5969")
plt.plot(x_ticks * 1e3, y_FR2433_R1[0], 'o-', label="MSP430FR2433")
plt.xlim(0, 60)
plt.ylim(1.8, 3.4)
plt.title("Frequency=1MHz, Cap=10uF")
plt.ylabel("Voltage(V)")
plt.xlabel("Time(ms)")
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(x_ticks * 1e3, y_FR5994_R1[1], 'o-', label="MSP430FR5994")
plt.plot(x_ticks * 1e3, y_FR5969_R1[1], 'o-', label="MSP430FR5969")
plt.plot(x_ticks * 1e3, y_FR2433_R1[1], 'o-', label="MSP430FR2433")
plt.xlim(0, 120)
plt.ylim(1.8, 3.4)
plt.title("Frequency=1MHz, Cap=20uF")
plt.ylabel("Voltage(V)")
plt.xlabel("Time(ms)")
plt.legend()


plt.subplot(2, 3, 2)
plt.plot(x_ticks * 1e3, y_FR5994_R2[0], 'o-',  label="MSP430FR5994")
plt.plot(x_ticks * 1e3, y_FR5969_R2[0], 'o-', label="MSP430FR5969")
plt.plot(x_ticks * 1e3, y_FR2433_R2[0], 'o-', label="MSP430FR2433")
plt.xlim(0, 40)
plt.ylim(1.8, 3.4)
plt.title("Frequency=2MHz, Cap=10uF")
plt.ylabel("Voltage(V)")
plt.xlabel("Time(ms)")
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(x_ticks * 1e3, y_FR5994_R2[1], 'o-', label="MSP430FR5994")
plt.plot(x_ticks * 1e3, y_FR5969_R2[1], 'o-', label="MSP430FR5969")
plt.plot(x_ticks * 1e3, y_FR2433_R2[1], 'o-', label="MSP430FR2433")
plt.xlim(0, 80)
plt.ylim(1.8, 3.4)
plt.title("Frequency=2MHz, Cap=20uF")
plt.ylabel("Voltage(V)")
plt.xlabel("Time(ms)")
plt.legend()


plt.subplot(2, 3, 3)
plt.plot(x_ticks * 1e3, y_FR5994_R3[0], 'o-',  label="MSP430FR5994")
plt.plot(x_ticks * 1e3, y_FR5969_R3[0], 'o-', label="MSP430FR5969")
plt.plot(x_ticks * 1e3, y_FR2433_R3[0], 'o-', label="MSP430FR2433")
plt.xlim(0, 30)
plt.ylim(1.8, 3.4)
plt.title("Frequency=4MHz, Cap=10uF")
plt.ylabel("Voltage(V)")
plt.xlabel("Time(ms)")
plt.legend()

plt.subplot(2, 3, 6)
plt.plot(x_ticks * 1e3, y_FR5994_R3[1], 'o-', label="MSP430FR5994")
plt.plot(x_ticks * 1e3, y_FR5969_R3[1], 'o-', label="MSP430FR5969")
plt.plot(x_ticks * 1e3, y_FR2433_R3[1], 'o-', label="MSP430FR2433")
plt.xlim(0, 50)
plt.ylim(1.8, 3.4)
plt.title("Frequency=4MHz, Cap=20uF")
plt.ylabel("Voltage(V)")
plt.xlabel("Time(ms)")
plt.legend()

plt.show()
