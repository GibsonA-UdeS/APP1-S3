import sys
import time
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#=================================================================================
# Exercice 1
#=================================================================================

# EDO2
# d2y_dt + 9*y = 0   avec y(0) = 0 et y'(0) = 0
xo = 0      # temps initial en sec
xf = 100     # temps final en sec
step = 10000 # nombre de step
t = np.linspace(xo, xf, step)
y = lambda t : np.cos(3*t)

# 1. Définir le système d'EDO2 transformé en deux EDO1
def eqn1a(t, x):
    # x[0] = y
    # x[1] = dy
    # d_x[0]/dt = x[1]
    # d_x[1]/dt = -9*x[0]
    dxdt = [x[1], -9*x[0]]
    return dxdt

# 2. Conditions initiales : y(0) = 1 et y'(0) = 0
y0 = [1, 0]

# 3. Intervalle de temps
t_span = (xo, xf)

# 4. Résolution
start_RK23 = time.perf_counter()
sol_RK23 = solve_ivp(eqn1a, t_span, y0, atol=1e-6, method='RK23')
end_RK23 = time.perf_counter()

start_RK45 = time.perf_counter()
sol_RK45 = solve_ivp(eqn1a, t_span, y0, atol=1e-6, method='RK45')
end_RK45 = time.perf_counter()
print(len(sol_RK23.y[0]))
print(len(sol_RK45.y[0]))

time_RK23 = end_RK23 - start_RK23
time_RK45 = end_RK45 - start_RK45
print("Temps pour RK23", time_RK23)
print("Temps pour RK45", time_RK45)

# 5. Affichage
plt.subplot(2,1,1)
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution de d"y/dt + 9*y = 0 (RK23)')
plt.plot(sol_RK23.t, sol_RK23.y[0], label="y(t) (position)")
plt.plot(sol_RK23.t, sol_RK23.y[1], label="y'(t) (vitesse)")
plt.legend()
plt.grid()
plt.subplot(2,1,2)
plt.plot(sol_RK45.t, sol_RK45.y[0], label="y(t) (position)")
plt.plot(sol_RK45.t, sol_RK45.y[1], label="y'(t) (vitesse)")
plt.plot(t, y(t), label="y(t) analytique")
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution de d"y/dt + 9*y = 0 (RK45)')
plt.legend()
plt.grid()
plt.show()

# Calculer l'erreur absolue en chaque points par rapport à la solution analytique
# e_abs_RK23 = abs(sol_RK23.y - y(t_RK23))
# e_abs_RK45 = abs(sol_RK45.y - y(t_RK45))

#=================================================================================
# Exercice 2
#=================================================================================


#=================================================================================
# Exercice 3
#=================================================================================
# x1[0] = x1
# x1[1] = dx1
# x2[0] = x2
# x2[1] = dx2

# 1. Variables et conditions initiales
m1 = 1  # kg
m2 = 2  # kg
k1 = k2 = 1     # N/m
c1 = c2 = 0.001 # Ns/m
xo = 0      # sec
xf = 40     # sec

# 2. Définition des fonctions
def système(t, x1, x2):
    dx1_dt = [x1[1], (1/m1)*(-((c1 + c2)*x1[1] - (c2)*x2[1] + (k1 + k2)*x1[0] - (k2)*x2[0]))]
    dx2_dt = [x2[1], (1/m1)*(-((-c2)*x1[1] + (c2)*x2[1] + (-k2)*x1[0] + (k2)*x2[0]))]
    return dx1_dt, dx2_dt

# 3. 