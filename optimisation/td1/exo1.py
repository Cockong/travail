#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:53:29 2019

@author: rthiebaut
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from numpy.linalg import inv

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
X = np.arange(-2, 2, 0.25) #x range
Y = np.arange(-2, 2, 0.25) #y range
X, Y = np.meshgrid(X, Y) #creates a rectangular grid on which to plot the function values (Z)
Z = (X-Y)**4 + 2*X**2 + Y**2 -X +2*Y #defines the function values
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False) #plot definition and options

#Runs the plot command
plt.show()


def f(vector):
  x=vector[0]
  y=vector[1]
  return ( (x-y)**4 + 2*x**2 + y**2 -x +2*y )

def g(vector):
  x=vector[0]
  y=vector[1]
  return [ 4*(x-y)**3 + 4*x -1 , -4*(x-y)**3 + 2*y + 2 ]

def norme(vector):
  x=vector[0]
  y=vector[1]
  return((x**2+y**2)**(1/2))

def unitary(vector):
  x=vector[0]
  y=vector[1]
  n=norme(vector)
  return([x/n,y/n])

def descent(firstvector,f,g,maxiter=100,pas=0.9):
  tab_descent=[(firstvector,f(firstvector))]
  vector=firstvector
  condition_f = True
  i=0
  while (i < maxiter and condition_f) :# maxiter gradiant norme or convergence step norme
    d=  unitary(g(vector))
    nextvector = (vector[0]-pas*d[0], vector[1]-pas*d[1])
    condition_f = f(nextvector) < f(vector)
    vector=nextvector
    tab_descent.append((vector,f(vector)))
    i+=1
  return tab_descent

print(descent((1,1),f,g))


#EXO6

tab=descent((1,1),f,g)

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
x = np.array([tab[i][0][0] for i in range(len(tab))]) #defines the x variable
y = np.array([tab[i][0][1] for i in range(len(tab))])#defines the y variable
z = np.array([tab[i][1] for i in range(len(tab))]) #creates a linear interval
ax.plot(x, y, z, label='parametric curve') #plot definition and options
ax.legend() #adds a legend
mpl.rcParams['legend.fontsize'] = 10 #sets the legend font size

#Runs the plot command
plt.show()


#exo7
"""
(12(x-y)² + 4  -12(x-y)²  )
(-12(x-y)²     12(x-y)²+2 )
"""
#exo 8
"""

Choose k = 0 and x 0 . As long as not convergence:
Calculate the quadratic model at x k : m x k (x)
∇f (x k )
Calculate d k = min d [m x k (x k + d)] = − ∇
2 f (x )
k
x k +1 = x k + d k
k = k + 1
"""
def h(vector):
  x=vector[0]
  y=vector[1]
  return(np.array(((12*(x-y)**2 + 4, -12*(x-y)**2  ),(-12*(x-y)**2, 12*(x-y)**2+2 ))))

def newton(firstvector,f,g,h,maxiter=100,pas=0.9):
  tab_descent=[(firstvector,f(firstvector))]
  vector=firstvector
  condition_f = True
  i=0
  while (i < maxiter and condition_f) :# maxiter gradiant norme or convergence step norme
    d=-np.dot(inv(h(vector)),g(vector))
    nextvector = vector+d
    condition_f = f(nextvector) < f(vector)
    vector=nextvector
    tab_descent.append((vector,f(vector)))
    i+=1
  return tab_descent


#exo9

tab_newton=newton(np.array((1,1)),f,g,h)

#exo11

#Definition of what to plot
fig = plt.figure() #opens a figure environment
ax = fig.gca(projection='3d') #to perform a 3D plot
x = np.array([tab_newton[i][0][0] for i in range(len(tab))]) #defines the x variable
y = np.array([tab_newton[i][0][1] for i in range(len(tab))])#defines the y variable
z = np.array([tab_newton[i][1] for i in range(len(tab))]) #creates a linear interval
ax.plot(x, y, z, label='parametric curve') #plot definition and options
ax.legend() #adds a legend
mpl.rcParams['legend.fontsize'] = 10 #sets the legend font size

#Runs the plot command
plt.show()

