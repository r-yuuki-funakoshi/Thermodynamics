import matplotlib.pyplot as plt
import numpy as np
import math

k_b = 1.3806504E-23 # Boltzmann constant
N1 = int(input("The Number of All Principal Energy Levels 1: "))
Q1 = int(input("The Number of All Quantum States or q: "))
N2 = int(input("The Number of All Principal Energy Levels 2: "))
N12 = N1 + N2
Q2 = Q1

set_q1 = [i for i in range(Q1 + 1)]
set_q2 = set_q1[::-1]
set_q12 = [a + b for a, b in zip(set_q1, set_q2)]
print("Set of quanta:", set_q1, set_q2, set_q12)

Ω1_set = [(math.factorial(N1 + q1 - 1)) / (math.factorial(q1) * math.factorial(N1 - 1)) for q1 in set_q1]
Ω2_set = [(math.factorial(N2 + q2 - 1)) / (math.factorial(q2) * math.factorial(N2 - 1)) for q2 in set_q2]
Ω12_set = [a * b for a, b in zip(Ω1_set, Ω2_set)]
print("Possible number of repetition combinations:", Ω1_set, Ω2_set, Ω12_set)

S1_set = [k_b * np.log(Ω1) for Ω1 in Ω1_set]
S2_set = [k_b * np.log(Ω2) for Ω2 in Ω2_set]
S12_set = [k_b * np.log(Ω12) for Ω12 in Ω12_set]
print("Entropies:", S1_set, S2_set, S12_set)
print("")

# Plotting the curves
fig, ax = plt.subplots(layout = 'constrained')
x = set_q1
y1 = S1_set
y2 = S2_set
y3 = S12_set

ax.plot(x, y1, color='r', label='S1 = k*ln(Ω1)')
ax.plot(x, y2, color='g', label='S2 = k*ln(Ω2)')
ax.plot(x, y3, color='b', label='S12 = k*ln(Ω1*Ω2)')

# Naming the x-axis, y-axis, and the whole graph
ax.set_xlabel("q1: quanta 1 (red)")
ax.set_ylabel("S: Entropy")
ax.set_title("Entropy plotted as quantum-dependent value", fontsize = 20)

# Function to map q1 to q2
def q1_to_q2(q1):
    return Q1 - q1

# Function to map q2 to q1
def q2_to_q1(q2):
    return Q1 - q2

secax = ax.secondary_xaxis(-0.2, functions = (q1_to_q2, q2_to_q1)) #Position of the secondary axis must be indicated using float values or 'top, bottow, left, right'
secax.set_xlabel('q2: quanta 2 (green)')

# Adding legend
plt.legend()

# Finding the max value and Display the plot
max_index = Ω12_set.index(max(Ω12_set))
max_q1 = set_q1[max_index]
max_q2 = set_q2[max_index]
print("The most probable value of q1:", max_q1)
print("The most probable value of q2:", max_q2)
max_S12 = max(S12_set)
print("")
print("Maximum value of the entropy of the system:", max_S12)

plt.show()
