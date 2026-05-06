import scipy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Exercice 1 : Dérivation numérique
def differentiate(x, f, step, dir):
  match dir:
    case -1: #Dérivation-arrière
      df = (f(x[1:])-f(x[:-1]))/step
      return np.array(df) 
    case 0: #Dérivation-centrée
      df = (f(x[2:])-f(x[:-2]))/(2*step)
      return np.array(df) 
    case 1: #Dérivation-avant
      df = (f(x[1:])-f(x[:-1]))/step
      return np.array(df)
    case _:
      df=[]
      df.append((f(x[0]+step)-f(x[0]))/step)
      df.extend((f(x[1:-1]+step)-f(x[1:-1]-step))/(2*step))
      df.append((f(x[-1])-f(x[-1]-step))/step)
      return np.array(df)
    
h = 1 #Pas de temps
start = -3
stop = 3
x = np.linspace(start,stop,(int((stop-start)/h))+1)
f = lambda x : np.exp(x) + x**2
df = lambda x : np.exp(x) + 2*x

abs_error_bwd = []
abs_error_cen = []
abs_error_fwd = []
abs_error_best1 = []
abs_error_best2 = []
abs_error_best3 = []
abs_error_best4 = []
rel_error_bwd = []
rel_error_cen = []
rel_error_fwd = []
rel_error_best1 = []
rel_error_best2 = []
rel_error_best3 = []
rel_error_best4 = []

df_bwd = differentiate(x,f,h,-1)
abs_error_bwd.append(abs(df_bwd - df(x[1:])))
rel_error_bwd.append(abs(df_bwd - df(x[1:]))/abs(df(x[1:])))

df_cen = differentiate(x,f,h,0)
abs_error_cen.append(abs(df_cen - df(x[1:-1])))
rel_error_cen.append(abs(df_cen - df(x[1:-1]))/abs(df(x[1:-1])))

df_fwd = differentiate(x,f,h,1)
abs_error_fwd.append(abs(df_fwd - df(x[:-1])))
rel_error_fwd.append(abs(df_fwd - df(x[:-1]))/abs(df(x[:-1])))

df_best1 = differentiate(x,f,h,2)
abs_error_best1.append(abs(df_best1 - df(x)))
rel_error_best1.append(abs(df_best1 - df(x))/abs(df(x)))

df_best2 = differentiate(x,f,(h/2),2)
abs_error_best2.append(abs(df_best2 - df(x)))
rel_error_best2.append(abs(df_best2 - df(x))/abs(df(x)))

df_best3 = differentiate(x,f,(h/4),2)
abs_error_best3.append(abs(df_best3 - df(x)))
rel_error_best3.append(abs(df_best3 - df(x))/abs(df(x)))

df_best4 = differentiate(x,f,(h/8),2)
abs_error_best4.append(abs(df_best4 - df(x)))
rel_error_best4.append(abs(df_best4 - df(x))/abs(df(x)))

abs_error_bwd = np.array(abs_error_bwd)
abs_error_cen = np.array(abs_error_cen)
abs_error_fwd = np.array(abs_error_fwd)
abs_error_best1 = np.array(abs_error_best1)
abs_error_best2 = np.array(abs_error_best2)
abs_error_best3 = np.array(abs_error_best3)
abs_error_best4 = np.array(abs_error_best4)

rel_error_bwd = np.array(rel_error_bwd)
rel_error_cen = np.array(rel_error_cen)
rel_error_fwd = np.array(rel_error_fwd)
rel_error_best1 = np.array(rel_error_best1)
rel_error_best2 = np.array(rel_error_best2)
rel_error_best3 = np.array(rel_error_best3)
rel_error_best4 = np.array(rel_error_best4)

#Plot 1 : Comparaison des dérivées approximatives vs la vraie dérivée trouvée analytiquement
plt.figure(1)
plt.title(f'Comparaison entre la différentiation analytique et numérique avec un pas de temps variable')
# plt.plot(x[1:], (df_bwd).T, label='Approx. df (backward)', marker='x')
# plt.plot(x[1:-1], (df_cen).T, label='Approx. df (central)', marker='*')
# plt.plot(x[:-1], (df_fwd).T, label='Approx. df (forward)', marker='o')
plt.plot(x, (df_best1).T, label=f'Approx. df with h={h}', marker='x')
plt.plot(x, (df_best2).T, label=f'Approx. df with h={h/2}', marker='*')
plt.plot(x, (df_best3).T, label=f'Approx. df with h={h/4}', marker='o')
plt.plot(x, (df_best4).T, label=f'Approx. df with h={h/8}', marker='.')
plt.plot(x, df(x).T, label='True df')
plt.plot(x, f(x).T, label='f(x) function')
plt.xlabel('x-values')
plt.ylabel("Approximations of f'(x)")
plt.legend()

#Plot 2 : Erreur absolue des trois méthodes d'approximations
plt.figure(2)
plt.subplot(2,1,1)
plt.title(f'Erreur absolue des différentes méthodes de différentiation numérique avec un pas de temps h={h}')
# plt.plot(x[1:], (abs_error_bwd).T, label='Error of backward df Approx.', marker='x')
# plt.plot(x[1:-1], (abs_error_cen).T, label='Error of central df Approx.', marker='*')
# plt.plot(x[:-1], (abs_error_fwd).T, label='Error of forward df Approx.', marker='o')
plt.plot(x, (abs_error_best1).T, label=f'Error of df Approx. with h={h}', marker='x')
plt.plot(x, (abs_error_best2).T, label=f'Error of df Approx. with h={h/2}', marker='*')
plt.plot(x, (abs_error_best3).T, label=f'Error of df Approx. with h={h/4}', marker='o')
plt.plot(x, (abs_error_best4).T, label=f'Error of df Approx. with h={h/8}', marker='.')
plt.xlabel('x-values')
plt.ylabel("Absolute error values of f'(x) approximations")
plt.legend()

#Plot 3 : Erreur relative des trois méthodes d'approximations
plt.subplot(2,1,2)
plt.title(f'Erreur relative des différentes méthodes de différentiation numérique avec un pas de temps h={h}')
# plt.plot(x[:-1], (rel_error_bwd).T, label='Error of backward df Approx.', marker='x')
# plt.plot(x[1:-1], (rel_error_cen).T, label='Error of central df Approx.', marker='*')
# plt.plot(x[1:], (rel_error_fwd).T, label='Error of forward df Approx.', marker='o')
plt.plot(x, (rel_error_best1).T, label=f'Error of df Approx. with h={h}', marker='x')
plt.plot(x, (rel_error_best2).T, label=f'Error of df Approx. with h={h/2}', marker='*')
plt.plot(x, (rel_error_best3).T, label=f'Error of df Approx. with h={h/4}', marker='o')
plt.plot(x, (rel_error_best4).T, label=f'Error of df Approx. with h={h/8}', marker='.')
plt.xlabel('x-values')
plt.ylabel("Relative error values of f'(x) approximations")
plt.legend()

#Exercice 2 : Intégration numérique
h1 = np.pi/6
h2 = np.pi/12

x1 = np.linspace((np.pi/3),np.pi,int((np.pi-(np.pi/3))/h1)+1)
x2 = np.linspace((np.pi/3),np.pi,int((np.pi-(np.pi/3))/h2)+1)

f = lambda x : (np.cos(2*x))**2

I = ((3**0.5)/16)+(np.pi/3)

I1_rect = (h1*np.sum(f(x1[:-1])))
I2_rect = (h2*np.sum(f(x2[:-1])))

abs_err_I1_rect = abs(I-I1_rect)
abs_err_I2_rect = abs(I-I2_rect)
rel_err_I1_rect = abs(I-I1_rect)/abs(I)
rel_err_I2_rect = abs(I-I2_rect)/abs(I)

print("Intégration numérique : Méthode des rectangles")
print(f"h = {h1}")
print("Approx. de l'intégrale :", I1_rect)
print("Erreur absolue :", abs_err_I1_rect)
print("Erreur relative :", rel_err_I1_rect)
print(f"h = {h2}")
print("Approx. de l'intégrale :", I2_rect)
print("Erreur absolue :", abs_err_I2_rect)
print("Erreur relative :", rel_err_I2_rect)
print("\n")

I1_trap = ((h1/2)*(f(x1[0])+np.sum(2*f(x1[1:-1]))+f(x1[-1])))
I2_trap = ((h2/2)*(f(x2[0])+np.sum(2*f(x2[1:-1]))+f(x2[-1])))

abs_err_I1_trap = abs(I-I1_trap)
abs_err_I2_trap = abs(I-I2_trap)
rel_err_I1_trap = abs(I-I1_trap)/abs(I)
rel_err_I2_trap = abs(I-I2_trap)/abs(I)

print("Intégration numérique : Méthode des trapèzes")
print(f"h = {h1}")
print("Approx. de l'intégrale :", I1_trap)
print("Erreur absolue :", abs_err_I1_trap)
print("Erreur relative :", rel_err_I1_trap)
print(f"h = {h2}")
print("Approx. de l'intégrale :", I2_trap)
print("Erreur absolue :", abs_err_I2_trap)
print("Erreur relative :", rel_err_I2_trap)
print("\n")

I1_simpson = (h1/3)*(f(x1[0])+4*np.sum(f(x1[1:-1:2]))+2*np.sum(f(x1[2:-1:2]))+f(x1[-1]))
I2_simpson = (h2/3)*(f(x2[0])+4*np.sum(f(x2[1:-1:2]))+2*np.sum(f(x2[2:-1:2]))+f(x2[-1]))

abs_err_I1_simpson = abs(I-I1_simpson)
abs_err_I2_simpson = abs(I-I2_simpson)
rel_err_I1_simpson = abs(I-I1_simpson)/abs(I)
rel_err_I2_simpson = abs(I-I2_simpson)/abs(I)

print("Intégration numérique : Méthode de Simpson")
print(f"h = {h1}")
print("Approx. de l'intégrale :", I1_simpson)
print("Erreur absolue :", abs_err_I1_simpson)
print("Erreur relative :", rel_err_I1_simpson)
print(f"h = {h2}")
print("Approx. de l'intégrale :", I2_simpson)
print("Erreur absolue :", abs_err_I2_simpson)
print("Erreur relative :", rel_err_I2_simpson)
print("\n")

#Exercice 3 : Fonction vectorielles
t = np.linspace(0,60,int(60/0.01))
#Coordonnées cartésiennes
x = lambda t : 10*np.cos(5*t)
y = lambda t : 5*np.sin(10*t)
z = lambda t : 10*(t**2)
# print("x(t) :\n", x(t))
# print("y(t) :\n", y(t))
# print("z(t) :\n", z(t))

#Coordonnées cylindriques
r = ((x(t)**2)+(y(t)**2))**0.5
theta = np.arctan2(y(t),x(t))
# print("r :\n", r)
# print("theta :\n", theta)

#Coordonnées sphériques
R = ((x(t)**2)+(y(t)**2)+(z(t)**2))**0.5
phi = np.arccos(z(t)/R)
# print("R :\n", R)
# print("phi :\n", phi)

plt.figure(3)
plt.title("Coordonnées cartésiennes")
plt.subplot(3,1,1)
plt.plot(t,x(t),label='x(t)')
plt.xlabel('t-values')
plt.ylabel("x-values")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t,y(t),label='y(t)')
plt.xlabel('t-values')
plt.ylabel("y-values")
plt.legend()
plt.subplot(3,1,3)
plt.plot(t,z(t),label='z(t)')
plt.xlabel('t-values')
plt.ylabel("z-values")
plt.legend()

plt.figure(4)
plt.title("Coordonnées cylindrique")
plt.subplot(3,1,1)
plt.plot(t,r,label='r(t)')
plt.xlabel('t-values')
plt.ylabel("r-values")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t,theta,label='theta(t)')
plt.xlabel('t-values')
plt.ylabel("theta-values")
plt.legend()
plt.subplot(3,1,3)
plt.plot(t,z(t),label='z(t)')
plt.xlabel('t-values')
plt.ylabel("z-values")
plt.legend()

plt.figure(5)
plt.title("Coordonnées sphériques")
plt.subplot(3,1,1)
plt.plot(t,R,label='R(t)')
plt.xlabel('t-values')
plt.ylabel("R-values")
plt.legend()
plt.subplot(3,1,2)
plt.plot(t,theta,label='theta(t)')
plt.xlabel('t-values')
plt.ylabel("theta-values")
plt.legend()
plt.subplot(3,1,3)
plt.plot(t,phi,label='phi(t)')
plt.xlabel('t-values')
plt.ylabel("phi-values")
plt.legend()

#Graphique 3d de l'évolution du marqueur
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(x(t), y(t), z(t))

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

#vitesse et accélération
dx = lambda t : -50 * np.sin(5*t)
dy = lambda t : 50 * np.cos(10*t)
dz = lambda t : 20*t
d2x = lambda t : -250 * np.cos(5*t)
d2y = lambda t : -500 * np.sin(10*t)
d2z = lambda t : 0*t + 20

v = (dx(t)**2 + dy(t)**2 + dz(t)**2)**0.5
a = (d2x(t)**2 + d2y(t)**2 + d2z(t)**2)**0.5

plt.figure(7)
plt.subplot(2,1,1)
plt.title('Vitesse en fonction du temps')
plt.plot(t, v)
plt.xlabel('t (s)')
plt.ylabel("v (m/s)")

plt.subplot(2,1,2)
plt.title('Accélération en fonction du temps')
plt.plot(t, a)
plt.xlabel('t (s)')
plt.ylabel("a (m/s²)")
plt.show()

#Longueur de la trajectoire
l = ((0.01/2)*(v[0]+np.sum(2*v[1:-1])+v[-1]))
print("Longueur de la trajectoire = ", l)