from scipy.integrate import solve_ivp, simpson
from scipy.interpolate import interp1d
from scipy.differentiate import derivative
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
V = 2                   #m/s
alpha = 1E-4            #Ns²/m²
rt = np.array([3,5,1])  #m

to = 0                  #sec
tf = 30                 #sec
h = 0.5                 #pas d'intégration
t_span = np.linspace(to, tf, int(((tf-to)/h)+1))

F0 = (m*g)/4            #N
F1 = []
F2 = []
F3 = []
F4 = []

for n in t_span:
  if (0<=n<5):         #Décollage
    F1.append(F0+1E-3)
    F2.append(F0+1E-3)
    F3.append(F0+1E-3)
    F4.append(F0+1E-3)
  elif (5<=n<7.5):   #Roll + Pitch  
    F1.append(F0-1E-6)
    F2.append(F0-1E-6)
    F3.append(F0+1E-6)
    F4.append(F0+1E-6)
  elif (7.5<=n<10):  #Roll + Pitch
    F1.append(F0+1E-6)
    F2.append(F0+1E-6)
    F3.append(F0-1E-6)
    F4.append(F0-1E-6)
  elif (10<=n<15):   #Ligne Droite
    F1.append(F0)
    F2.append(F0)
    F3.append(F0)
    F4.append(F0)
  elif (15<=n<=30):   #Freinage
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

  F1_t = np.interp(t, t_span, F1)
  F2_t = np.interp(t, t_span, F2)
  F3_t = np.interp(t, t_span, F3)
  F4_t = np.interp(t, t_span, F4)

  dxdt = x_dot
  dydt = y_dot
  dzdt = z_dot

  dvxdt = (alpha * V**2 + (np.sin(phi) * np.sin(psi) * (F1_t+F2_t+F3_t+F4_t) + np.sin(theta) * np.cos(phi) * np.cos(psi) * (F1_t+F2_t+F3_t+F4_t))) / m
  dvydt = (-np.sin(phi) * np.cos(psi) * (F1_t+F2_t+F3_t+F4_t) + np.sin(theta) * np.cos(phi) * np.sin(psi) * (F1_t+F2_t+F3_t+F4_t)) / m
  dvzdt = (m * -g + (np.cos(theta) * np.cos(phi) * (F1_t+F2_t+F3_t+F4_t))) / m

  dtheta_dt = q * np.cos(phi) - r * np.sin(phi)
  dphi_dt = p + (q * np.sin(phi) + r * np.cos(phi)) * np.sin(theta) / np.cos(theta)
  dpsi_dt = (q * np.sin(phi) + r * np.cos(phi)) / np.cos(theta)

  p_dot = (q * r * (Iyy - Izz) + L * (F2_t - F4_t)) / Ixx
  q_dot = (p * r * (Izz - Ixx) + L * (F3_t - F1_t)) / Iyy
  r_dot = (p * q * (Ixx - Iyy) + L * (-F1_t + F2_t - F3_t + F4_t)) / Izz

  return [dxdt,dydt,dzdt,dvxdt,dvydt,dvzdt,dtheta_dt,dphi_dt,dpsi_dt,p_dot,q_dot,r_dot]

def atterissage(t, y):
    x, y, z = y[0], y[1], y[2]
    dist_centre = ((x - 3)**2 + (y - 5)**2)**0.5
    return z - 1 if dist_centre <= 1 else 1

atterissage.terminal = True
atterissage.direction = 0

sol = solve_ivp(drone_IED,t_span=[to,tf], y0=np.zeros(12), method='RK45',t_eval=t_span,events=atterissage)

if sol.status == 1:
  print("Temps de trajet :", sol.t_events[0],"s")
  print("Position d'atterissage :", sol.y_events[0][0][0:3],"m")
else:
  print("Atterissage manqué")
  print("Position finale :", sol.y[0][-1], sol.y[1][-1], sol.y[2][-1], "m")

longueur_traj = ((simpson(sol.y[3],sol.t))**2 + (simpson(sol.y[4],sol.t))**2 + (simpson(sol.y[5],sol.t))**2)**0.5
print("Longueur de la trajectoire :", longueur_traj, "m")

fx = interp1d(sol.t,sol.y[0],'cubic', fill_value="extrapolate")
fy = interp1d(sol.t,sol.y[1],'cubic', fill_value="extrapolate")
fz = interp1d(sol.t,sol.y[2],'cubic', fill_value="extrapolate")

vit_instant = ((derivative(fx,sol.t).df)**2 + (derivative(fy,sol.t).df)**2 + (derivative(fz,sol.t).df)**2)**0.5
plt.plot(sol.t, vit_instant, label='Vitesse instantanée')
plt.xlabel('t (s)')
plt.ylabel('v (m/s)')
plt.legend()

#Graphique 3d de l'évolution du marqueur
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(sol.y[0], sol.y[1], sol.y[2], label='Trajectoire')
theta1 = np.linspace(0, 2*np.pi, 200)
r = 1
x1 = r * np.cos(theta1)
y1 = r * np.sin(theta1)
z1 = np.zeros_like(theta1)
ax.plot(x1+3, y1+5, z1+1, color='blue')

ax.scatter([3],[5],[1], color='r', label="Cible")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("z (m)")
ax.set_title("Trajectoire 3D du drone")
ax.grid(True)
ax.legend()
plt.show()