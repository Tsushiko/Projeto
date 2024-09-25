import numpy as np
from scipy.integrate import odeint
from menuGraphs import graphs

# Sistema de equações
def model(x,t,p12,p21,p31,p34,d1,d2,d3,d13,d23):
 # Constantes
  A = x[0]
  R = x[1]
  S = x[2]
  I = x[3]

  dAdt = p12 * A * R - d13 * A * S - A * d1
  dRdt = p21 * R * A - d23 * R * S - R * d2
  dSdt = p31 * S * A + p34 * S * I - S * d3
  dIdt = 0
   
  return [dAdt,dRdt,dSdt,dIdt]

# Valores iniciais

def main(p12,p21,p31,p34,d1,d2,d3,d13,d23,values0):
  # Intervalos de tempo
  t = np.linspace(0,30,201)
  x = odeint(model,values0,t, args=(p12,p21,p31,p34,d1,d2,d3,d13,d23))

  A = x[:,0]
  R = x[:,1]
  S = x[:,2]
  I = x[:,3]

  graphs(A,R,S,I,t)