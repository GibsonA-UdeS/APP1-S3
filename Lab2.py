from time import perf_counter
import scipy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Exercice 1 : Solveurs MATLAB
x = [1,0]
y = lambda t : np.cos(3*t)
dy = lambda t : -3*np.sin(3*t)

eqn1a = lambda t, x : [x[1],-9*x[0]]

start_sol1 = perf_counter()
sol1 = scipy.integrate.solve_ivp(eqn1a, [0,100], x, method='RK23', atol=1E-6) #, atol=1E-6
temps_sol1 = perf_counter() - start_sol1
print("Temps de calcul avec Runge-Kutta d'ordre 2 : ", f"{temps_sol1}s")

start_sol2 = perf_counter()
sol2 = scipy.integrate.solve_ivp(eqn1a, [0,100], x, method='RK45', atol=1E-6) #, atol=1E-6
temps_sol2 = perf_counter() - start_sol2
print("Temps de calcul avec Runge-Kutta d'ordre 4 : ", f"{temps_sol2}s")

print(len(sol1.y[0]))
t1 = np.linspace(0,100,len(sol1.y[0]))
err_sol1_y = abs(y(t1)-sol1.y[0])
err_sol1_dy = abs(dy(t1)-sol1.y[1])
print(len(sol2.y[0]))
t2 = np.linspace(0,100,len(sol2.y[0]))
err_sol2_y = abs(y(t2)-sol2.y[0])
err_sol2_dy = abs(dy(t2)-sol2.y[1])

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(sol1.t, sol1.y[0],label='y1(t) with RK23')
plt.plot(sol1.t, sol1.y[1],label='y2(t) with RK23')
plt.xlabel('t(s)')
plt.ylabel('y(t) et y\'(t)')
plt.legend()
plt.subplot(3,1,2)
plt.plot(sol2.t, sol2.y[0],label='y1(t) with RK45')
plt.plot(sol2.t, sol2.y[1],label='y2(t) with RK45')
plt.xlabel('t(s)')
plt.ylabel('y(t) et y\'(t)')
plt.legend()
plt.subplot(3,1,3)
plt.plot(t2, y(t2),label='y(t)')
plt.plot(t2, dy(t2),label='dy(t)/dt')
plt.xlabel('t(s)')
plt.ylabel('y(t) et y\'(t)')
plt.legend()

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(sol1.t, err_sol1_y,label='error of y1(t) with RK23')
plt.plot(sol2.t, err_sol2_y,label='error of y1(t) with RK45')
plt.xlabel('t(s)')
plt.ylabel('error of y1(t)')
plt.legend()
plt.subplot(2,1,2)
plt.plot(sol1.t, err_sol1_dy,label='error of y2(t) with RK23')
plt.plot(sol2.t, err_sol2_dy,label='error of y2(t) with RK45')
plt.xlabel('t(s)')
plt.ylabel('error of y2(t)')
plt.legend()

plt.show()

#Exercice 2 : Prédateurs / Proies



#Exercice 3 : Problème intégrateur - Système masse-ressort à 2 ddl
m1 = 1 #kg
m2 = 2 #kg

k1 = k2 = 1 #N/m
c1 = c2 = 0.001 #Ns/m

t = np.linspace(0,40,100)

for n in t:
  eqn31 = lambda x1, x2 : (1/m1)*(-((c1+c2)*x1[1]-c2*x2[1]+(k1+k2)*x1[0]-k2*x2[0]))
  if n > 10:
    f2 = 1
  else:
    f2 = 0
  eqn32 = lambda x1, x2 : (1/m2)*(-((-c2)*x1[1]+c2*x2[1]+(-k2)*x1[0]+k2*x2[0])+f2)

d2x = np.array([eqn31, eqn32])

