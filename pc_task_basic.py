import numpy as np

tasks = np.array([726, 905, 1886, 1025, 927, 2212, 233, 5050])

fr5994_time = np.array([50294, 10705, 26154, 13722, 8837, 17508, 26711, 24943])
fr5969_time = np.array([50463, 10742, 26243, 13769, 8868, 17570, 26802, 25027])
fr2433_time = np.array([58707, 13534, 33666, 16997, 11312, 23692, 29489, 35919])

print("5994 ", np.array(fr5994_time / tasks * 10, dtype=int))
print("5969 ", np.array(fr5969_time / tasks * 10, dtype=int))
print("2433 ", np.array(fr2433_time / tasks * 10, dtype=int))
