import matplotlib.pyplot as plt
import numpy as np
import math
import scipy

k_b = 1.3806504E-23 #Boltzmann constant
N1 = int(input("The Number of All Principal Energy Levels 1: ", ))
Q1 = int(input("The Number of Quantum States or q: ", ))
N2 = int(input("The Number of All Principal Energy Levels 2: ", ))
N12 = N1 + N2
Q2 = Q1

set_q1 = []
set_q2 = []
set_q12 = []
for i in range(-1, Q1):
    i += 1
    set_q1.append(i)
set_q2 = set_q1[::-1]
set_q12 = [a + b for a, b in zip(set_q1, set_q2)]
print("Set of quanta", set_q1, set_q2, set_q12)
# Set of q (all quanta) or quantum state in system 1 and system 2. q are number of quntum oscillators.

Ω1_set = []
Ω2_set = []
Ω12_set = []
for q1 in range(0, len(set_q1)):
    Ω1 = (math.factorial(N1 + q1 - 1)) / (math.factorial(q1) * math.factorial(N1 - 1))
    Ω1_set.append(Ω1)
for q2 in range(0, len(set_q2)):
    Ω2 = (math.factorial(N2 + q2 - 1)) / (math.factorial(q2) * math.factorial(N2 - 1))
    Ω2_set.append(Ω2)
Ω12_set = [a * b for a, b in zip(Ω1_set, Ω2_set)]
print("Possible number of repetition combination", Ω1_set, Ω2_set, Ω12_set)


S1_set = []
S2_set = []
S12_set = []
for Ω1 in range(1, len(Ω1_set)):
    S1 = k_b * np.log(Ω1)
    S1_set.append(S1)
for Ω2 in range(1, len(Ω2_set)):
    S2 = k_b * np.log(Ω2)
    S2_set.append(S2)
for Ω12 in range(1, len(Ω12_set)):
    S12 = k_b * np.log(Ω12)
    S12_set.append(S12)
print("Entropies", S1_set, S2_set, S12_set)
print("Dimention check for x-axis", len(set_q1), len(set_q2), len(set_q12))
print("Dimention check for y-axis", len(S1_set), len(S2_set), len(S12_set))

# Assign variables to the y axis part of the curve 
S1 = k_b * np.log(Ω1)
S2 = k_b * np.log(Ω2)
S12 = k_b * np.log(Ω12)

# Plotting both the curves simultaneously 
plt.plot(set_q1, S1, color='r', label='k*ln(Ω1)') 
plt.plot(set_q2, S2, color='g', label='k*ln(Ω2)')
plt.plot(set_q1, S12, color='b', label='k*ln(Ω1*Ω2)')

# Naming the x-axis, y-axis and the whole graph 
plt.xlabel("q: quanta") 
plt.ylabel("S: Entropy") 
plt.title("Entropy plotted as quantum-dependent value") 

# Adding legend, which helps us recognize the curve according to it's color 
plt.legend() 

# To load the display window 
plt.show() 

