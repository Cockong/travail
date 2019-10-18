#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:52:17 2019

@author: rthiebaut
"""
from math import exp
from numpy.random import randn
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from numpy.linalg import inv

def g(x,a):
  return exp(-a*x)

x=[0.01*i for i in range(301)]
y=[]
a=2
b=10**(-2)
N=randn(301)
for i in range(len(x)):
  y.append(g(x[i],a)+b*N[i])

#4
plt.plot(x,y)


#5

def f(x,y,a):
  return ( 0.5* sum([ (y[i]-g(x[i],a))**2 for i in range(301)] ) )

print(f(x,y,a))
print(sum(b*b*N[i]**2 for i in range(301))) #verification que f correspond a la somme du carré des bruits

#6

def derive_g(x,a):
  return (-x*g(x,a))

def gradient_f(x,y,a):
  return(- sum([ (y[i]-g(x[i],a))*derive_g(x[i],a)  for i in range(301)] ))

print(gradient_f(x,y,a))

#7

def h_sansapro(x,y,a):
    return( sum([ derive_g(x[i],a)**2-(y[i]-g(x[i],a))*(x[i]**2)*g(x[i],a)  for i in range(301)] ))

def h(x,y,a):
    return( sum([ derive_g(x[i],a)**2  for i in range(301)] ))

#8



#DONT WORK
"""

def norme(vector):
  x=vector[0]
  y=vector[1]
  return((x**2+y**2)**(1/2))

def unitary(vector):
  x=vector[0]
  y=vector[1]
  n=norme(vector)
  return([x/n,y/n])

a=1.5
l=0.001


def levenberg(firstvector,gradient_f,g,maxiter=100,pas=0.9):
  tab_descent=[(firstvector,f(firstvector))]
  vector=firstvector
  condition_f = True
  i=0
  while (i < maxiter and condition_f) :# maxiter gradiant norme or convergence step norme
    d=  unitary(gradient_f(vector))


    Calcul de H LM : Hlm= H(x,a)+l
    nextvector = (vector[0]-pas*d[0], vector[1]-pas*d[1])
    condition_f = f(nextvector) < f(vector)
    vector=nextvector
    tab_descent.append((vector,f(vector)))
    i+=1
  return tab_descent

print(descent((1,1),f,g))

"""





