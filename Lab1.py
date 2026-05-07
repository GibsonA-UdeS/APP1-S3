import scipy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#=================================================================================
# Exercice 1.1
#=================================================================================

# Fonction de différentiation
def differentiation(x, f):
    df_fwd_bwd = (f(x[1:]) - f(x[:-1])) / h         # Pour la dérivée avant et arrière
    df_ctd = (f(x[2:]) - f(x[:-2])) / 2 * h     # Pour la dérivée centrée
    df_app = []
    df_app.append(df_fwd_bwd[0])
    df_app.extend(df_ctd)
    df_app.append(df_fwd_bwd[-1])
    return np.array(df_app)

# Variables
h = 1       # pas d'intégration
xo = -3
xf = 3
nb = int((xf-xo)/h)+1       # nombre de point pour obtenir une courbe avec 6 segments
x = np.linspace(xo, xf, nb)

# a) Représentation graphique de f(x) = exp(x) + x^2 pour différentes valeurs de x entre -3 et 3
f = lambda x : np.exp(x) + x**2

# b) Calculer analytiquement f'(x) et la représenter graphiquement
df = lambda x : np.exp(x) + 2*x

# On cherche maintenant à approximer f'(x) de manière numérique et comprendre la précision de ce calcul en fonction du pas h.

# c) Approximer f'(x) avec la méthode en amont/aval (fwd)
df_fwd = (f(x[1:]) - f(x[:-1]))/h

# d) Approximer f'(x) avec la méthode en aval/arrière (bwd)
df_bwd = (f(x[1:]) - f(x[:-1]))/h

# e) Approximer f'(x) avec la méthode centrée (ctd)
df_ctd = (f(x[2:]) - f(x[:-2]))/(2*h)

# f) Créer une fonction de differentiation
df_app = differentiation(x, f)

# g) Représenter en fonction de x l'erreur absolue et l'erreur relative entre la valeur exacte de f'(x) et celle estimée numériquement
e_abs_df_app = abs(df_app - df(x))
e_rel_df_app = abs((df_app - df(x))/df(x))

# h) Refaire la dernière étape avec différents pas h=1/0.5/0.25/0.125 pour le vecteur x et conclure sur l'évolution de l'erreur en fonction de h
# À FINIR

# # Affichage du plot pour la partie 1.1
# plt.figure(1)
# plt.plot(x, f(x), 'o-', label="f(x)")
# plt.plot(x, df(x), 'o-', label="f'(x)")
# plt.plot(x[:-1], df_fwd, 'o-', label="df_fwd")
# plt.plot(x[1:], df_bwd, 'o-', label="df_bwd")
# plt.plot(x[1:-1], df_ctd, 'o-', label="df_ctd")
# plt.plot(x, df_app, 'o-', label="df_app")
# plt.xlim(xo, xf)
# plt.title("Dérivée de la fonction exp(x)+x^2")
# plt.xlabel("x")
# plt.ylabel("f'(x)")
# plt.legend()

# # Affichage des plot d'erreur
# plt.figure(2)

# # Plot d'erreur relative
# plt.subplot(2,1,2)
# plt.plot(x, e_rel_df_app, 'o-', label="e_rel_df_app")
# plt.xlim(xo, xf)
# plt.title("Erreurs sur les dérivations")
# plt.xlabel("x")
# plt.ylabel("Erreur")
# plt.legend()
# # Plot d'erreur absolue
# plt.subplot(2,1,1)
# plt.plot(x, e_abs_df_app, 'o-', label="e_abs_df_app")
# plt.xlim(xo, xf)
# plt.title("Erreurs sur les dérivations")
# plt.xlabel("x")
# plt.ylabel("Erreur")
# plt.legend()
# plt.show()

#=================================================================================
# Exercice 2.1
#=================================================================================
I = (np.sqrt(3)/16) + (np.pi/3)
xo = np.pi/3
xf = np.pi
h1 = np.pi/6
h2 = np.pi/12
nb1 = int((xf-xo)/h1)+1
nb2 = int((xf-xo)/h2)+1
x1 = np.linspace(xo, xf, nb1)
x2 = np.linspace(xo, xf, nb2)
f = lambda x : (np.cos(2*x))**2

#2.1 a) Estimer I par la méthode des rectangles (h1=pi/6 et h2=pi/12)
I1_rect = h1*np.sum(f(x1[:-1]))
I2_rect = h2*np.sum(f(x2[:-1]))

#2.1 b) Estimer I par la méthode des trapèzes (h1=pi/6 et h2=pi/12)
I1_trap = (h1/2)*(np.sum(2*f(x1[1:-1])) + f(xo) + f(xf))
I2_trap = (h2/2)*(np.sum(2*f(x2[1:-1])) + f(xo) + f(xf))

#2.1 c) Estimer I par la méthode de Simpson (h1=pi/6 et h2=pi/12)
I1_Simp = (h1/3) * ((f(x1[0]) + np.sum(4*f(x1[1:-1:2])) + np.sum(2*f(x1[2:-1:2])) + f(x1[-1])))
I2_Simp = (h2/3) * ((f(x2[0]) + np.sum(4*f(x2[1:-1:2])) + np.sum(2*f(x2[2:-1:2])) + f(x2[-1])))

# d) Dans chaque cas, comparer l'erreur absolue par rapport à la valeur théorique
e_abs_rect1 = I1_rect - I
e_abs_rect2 = I2_rect - I

e_rel_rect1 = e_abs_rect1/I
e_rel_rect2 = e_abs_rect2/I

e_abs_trap1 = I1_trap - I
e_abs_trap2 = I2_trap - I

e_rel_trap1 = e_abs_trap1/I
e_rel_trap2 = e_abs_trap2/I

e_abs_simp1 = I1_Simp - I
e_abs_simp2 = I2_Simp - I

e_rel_simp1 = e_abs_simp1/I
e_rel_simp2 = e_abs_simp2/I

print("I1_rect =", I1_rect)
print("Erreur Abs:", e_abs_rect1)
print("Erreur Rel:", e_rel_rect1)
print("\n")

print("I2_rect =", I2_rect)
print("Erreur Abs:", e_abs_rect2)
print("Erreur Rel:", e_rel_rect2)
print("\n")

print("I1_trap =", I1_trap)
print("Erreur Abs:", e_abs_trap1)
print("Erreur Rel:", e_rel_trap1)
print("\n")

print("I2_trap =", I2_trap)
print("Erreur Abs:", e_abs_trap2)
print("Erreur Rel:", e_rel_trap2)
print("\n")

print("I1_Simp =", I1_Simp)
print("Erreur Abs:", e_abs_simp1)
print("Erreur Rel:", e_rel_simp1)
print("\n")

print("I2_Simp =", I2_Simp)
print("Erreur Abs:", e_abs_simp2)
print("Erreur Rel:", e_rel_simp2)
print("\n")

#=================================================================================
# Exercice 3.1
#=================================================================================
x = lambda t : 10 * np.cos(5 * t)
y = lambda t : 5 * np.sin(10 * t)
z = lambda t : 10 * t ** 2
h = 0.01        # sec
to = 0          # sec
tf = 60         # sec
t = np.linspace(to, tf, int((tf-to)/h))

# a) Représenter les coordonnées du vecteur position de l'objet en coordonnées cylindriques et sphériques.
r_cyl = (x(t)**2 + y(t)**2)**0.5
theta = np.atan2(y(t),x(t))

r_sph = (x(t)**2 + y(t)**2 + z(t)**2)**0.5
phi = np.acos(z(t)/r_sph)

plt.figure(3)
plt.subplot(3,1,1)
plt.plot(t, r_cyl, '-', label="r_cyl")
plt.xlabel("t")
plt.ylabel("r_cyl")
plt.subplot(3,1,2)
plt.plot(t, theta, '-', label="theta")
plt.xlabel("t")
plt.ylabel("theta")
plt.subplot(3,1,3)
plt.plot(t, z(t), '-', label="z")
plt.xlabel("t")
plt.ylabel("z")

plt.figure(4)
plt.subplot(3,1,1)
plt.plot(t, r_sph, '-', label="r_sph")
plt.xlabel("t")
plt.ylabel("r_sph")
plt.subplot(3,1,2)
plt.plot(t, theta, '-', label="theta")
plt.xlabel("t")
plt.ylabel("theta")
plt.subplot(3,1,3)
plt.plot(t, phi, '-', label="phi")
plt.xlabel("t")
plt.ylabel("phi")

# b) Représenter l'évolution du marqueur dans le temps entre t = 0 et t = 60 avec un pas de temps dt = 0.01s

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(x(t), y(t), z(t))

# c) Déterminer les amplitudes des vecteurs vitesse et accélération en fonction du temps t.
dx_dt = lambda t : -50 * np.sin(5*t)    # Pourrait être fait par diff numériquement o7
dy_dt = lambda t : 50 * np.cos(10*t)
dz_dt = lambda t : 20*t
v_vitesse = (dx_dt(t)**2 + dy_dt(t)**2 + dz_dt(t)**2)**0.5

d2x_dt = -250*np.cos(5*t)       # Pourrait être faite par diff numériquement o7
d2y_dt = -500*np.sin(10*t)
d2z_dt = 20
v_accel = (d2x_dt**2 + d2y_dt**2 + d2z_dt**2)**0.5

plt.figure(6)
plt.subplot(2,1,1)
plt.plot(t, v_vitesse, '-')
plt.title("Vitesse")
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.subplot(2,1,2)
plt.plot(t, v_accel, '-')
plt.title("Accélération")
plt.xlabel("t (s)")
plt.ylabel("a (m/s²)")
plt.show()

# d) Calculer la longueur parcourue par l'objet entre les instants t = 0 et t = 60s en utilisant la méthode des trapèzes et un pas d'intégration de h = 0.01s
L_trap = (h/2)*(np.sum(2*v_vitesse[1:-1]) + v_vitesse[0] + v_vitesse[-1])
print("Longueur parcourue par l'objet entre 0 et 60 sec (m):", L_trap)
