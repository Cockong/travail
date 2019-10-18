from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


## -----------------------------------------------
## Function definition, derivatives
## -----------------------------------------------

# fonction f
def f(vect) :
	X = vect[0]
	Y = vect[1]
	return (X-Y)**4 + 2*(X**2)+Y**2-X+2*Y

def g(vect) :
	X = vect[0]
	Y = vect[1]
	return np.array([4*(X-Y)**3 + 4*X- 1, -4*(X-Y)**3 +2*Y +2])

## -----------------------------------------------
## Gradient
## -----------------------------------------------
def methode_gradient(f,g,nb_iter_max,pas,x_init) :
	xcour = x_init
	print ""
	print "--------GRADIENT DESCENT--------"
	tab_parcours_grad = [xcour]
	condition_f = True
	i = 0
	print "iteration ",i , " ; x = ",xcour
	while (i < nb_iter_max and condition_f) :
		xsuiv = xcour - pas*g(xcour) #iteration suivante
		i = i+1
		tab_parcours_grad.append(xsuiv)
		condition_f = f(xsuiv) < f(xcour)
#		print "condition_f =",condition_f
		xcour = xsuiv
		print "iteration ",i , " ; x = ",xcour, " ; norm 1 gradient = ", erreur
	
	return tab_parcours_grad

nb_iter_max = 100
pas = 0.09
x_init = np.array([1,1])
tab_parcours_grad = methode_gradient(f,g,nb_iter_max,pas,x_init)
