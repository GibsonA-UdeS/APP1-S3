import scipy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Programme principal
m = 0.1                 #kg
g = 9.8                 #m/s²
Ixx = 0.6E-3            #kg * m²
Iyy = 1.1E-3            #kg * m²
Izz = 1.5E-3            #kg * m²
L = 0.1                 #m
alpha = 1E-4            #Ns²/m²
rt = np.array([3,5,1])  #m

to = 0                  #sec
tf = 30                 #sec
dt = 0.1                #pas d'intégration
t = np.linspace( to, tf, int(((tf-to)/dt)+1))  #h = 0.1

F0 = (m*g)/4            #N
F1 = []
F2 = []
F3 = []
F4 = []

for n in t:
  if (n<5):         #Décollage
    F1.append(F0+1E-3)
    F2.append(F0+1E-3)
    F3.append(F0+1E-3)
    F4.append(F0+1E-3)
  elif (5<n<7.5):   #Roll + Pitch
    F1.append(F0-1E-6)
    F2.append(F0-1E-6)
    F3.append(F0+1E-6)
    F4.append(F0+1E-6)
  elif (7.5<n<10):  #Roll + Pitch
    F1.append(F0+1E-6)
    F2.append(F0+1E-6)
    F3.append(F0-1E-6)
    F4.append(F0-1E-6)
  elif (10<n<15):   #Ligne Droite
    F1.append(F0)
    F2.append(F0)
    F3.append(F0)
    F4.append(F0)
  elif (15<n<30):   #Freinage
    F1.append(F0-1E-3)
    F2.append(F0-1E-3)
    F3.append(F0-1E-3)
    F4.append(F0-1E-3)

r0 = 0
dr0 = 0
d2r0 = 0

# Couples moteurs
tau_theta = L * (F2 - F4)
tau_phi = L * (F3 - F1)
tau_psi = L * (-F1 + F2 - F3 + F4)

# Équations différentielles
dtheta_dt = p
dphi_dt = q
dpsi_dt = r

# Intégration numérique p_dot, q_dot, r_dot avec la méthode de Simpson
p_dot = (q * r * (Iyy - Izz) + tau_theta) / Ixx
q_dot = (p * r * (Izz - Ixx) + tau_phi) / Iyy
r_dot = (p * q * (Ixx - Iyy) + tau_psi) / Izz

p = (dt/3) * ((p_dot(q[0], r[0]) + np.sum(4*p_dot(q[1:-1:2], r[1:-1:2])) + np.sum(2*p_dot(q[2:-1:2], r[2:-1:2])) + p_dot(q[-1], r[-1])))
