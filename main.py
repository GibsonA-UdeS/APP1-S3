from scipy.integrate import solve_ivp
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
V = 1                   #m/s
alpha = 1E-4            #Ns²/m²
rt = np.array([3,5,1])  #m

to = 0                  #sec
tf = 30                 #sec
h = 0.1                 #pas d'intégration
t = np.linspace(to, tf, int(((tf-to)/h)+1))

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

F1 = np.array(F1)
F2 = np.array(F2)
F3 = np.array(F3)
F4 = np.array(F4)

r0 = 0
dr0 = 0
d2r0 = 0

var_etats = np.empty(12)
def drone_IED(t, var_etats):
  x = var_etats[0]
  y = var_etats[1]
  z = var_etats[2]

  x_dot = var_etats[3]
  y_dot = var_etats[4]
  z_dot = var_etats[5]

  theta = var_etats[6]
  phi = var_etats[7]
  psi = var_etats[8]

  p = var_etats[9]
  q = var_etats[10]
  r = var_etats[11]

  dxdt = x_dot
  dydt = y_dot
  dzdt = z_dot

  dvxdt = (alpha * V**2 + (np.sin(phi) * np.sin(psi) * (F1+F2+F3+F4) + np.sin(theta) * np.cos(phi) * np.cos(psi) * (F1+F2+F3+F4))) / m
  dvydt = (-np.sin(phi) * np.cos(psi) * (F1+F2+F3+F4) + np.sin(theta) * np.cos(phi) * np.sin(psi) * (F1+F2+F3+F4))/m
  dvzdt = (m * g + (np.cos(theta) * np.cos(phi) * (F1+F2+F3+F4)))/m

  dtheta_dt = p
  dphi_dt = q
  dpsi_dt = r

  p_dot = (q * r * (Iyy - Izz) + L * (F2 - F4)) / Ixx
  q_dot = (p * r * (Izz - Ixx) + L * (F3 - F1)) / Iyy
  r_dot = (p * q * (Ixx - Iyy) + L * (-F1 + F2 - F3 + F4)) / Izz
  
  return [dxdt,dydt,dzdt,dvxdt,dvydt,dvzdt,dtheta_dt,dphi_dt,dpsi_dt,p_dot,q_dot,r_dot]

sol = solve_ivp(drone_IED,[to,tf], y0=np.zeros(12), method='RK45',t_eval=t)

print(sol.y[0], sol.y[1], sol.y[2])