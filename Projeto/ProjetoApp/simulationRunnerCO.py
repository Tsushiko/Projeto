from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import minimize
from menuGraphs import graphsCO

def model(values0,t,x,ks,p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23):
   A,R,S,I = values0[:4]
   # Equações diferenciais
   dAdt = p12 * A * R - d13 * A * S - A * d1
   dRdt = p21 * R * A - d23 * R * S - R * d2
   dSdt = p31 * S * A + p34 * S * I - S * d3
   dIdt = x[ks] - d4 * I
   dYdt = beta * R + alpha * x[ks]
   
   return [dAdt,dRdt,dSdt,dIdt,dYdt]

def objective(x,p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23,values0,nStage,timeStage):
    newValues0 = values0
    for ks in range(nStage):
        sol = odeint(model, newValues0, [timeStage[ks], timeStage[ks+1]], args=(x,ks,p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23,))
        newValues0 = sol[-1, :]
    Y = sol[-1,4]
    return Y

def dispopt(values0,nStage,timeStage,x,p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23):
    z0 = values0
    topt = [0]
    Copt = []
    Aopt = []
    Ropt = []
    Sopt = []
    Iopt = []
    for ks in range(0,nStage):
        values, infodict = odeint(model, z0,[timeStage[ks],timeStage[ks+1]], full_output = True, args=(x,ks,p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23,))
        z0 = values[-1, :]
        topt.append(infodict['tcur'][0])
        for i in values:
            Copt.append(list(i))
    for i in Copt:
        Aopt.append(i[0])
        Ropt.append(i[1])
        Sopt.append(i[2])
        Iopt.append(i[3])

    Aopt2 = []    
    [Aopt2.append(x) for x in Aopt if x not in Aopt2]
    Ropt2 = []    
    [Ropt2.append(x) for x in Ropt if x not in Ropt2]
    Sopt2 = []    
    [Sopt2.append(x) for x in Sopt if x not in Sopt2]
    Iopt2 = []    
    [Iopt2.append(x) for x in Iopt if x not in Iopt2]

    graphsCO(Aopt2,Ropt2,Sopt2,Iopt2,np.insert(x,0,1),topt)

# Time Horizon and Initial State
timeI = 0        # Initial time
timeF = 30        # Final time
cons = [{'type': 'ineq', 'fun': lambda x: 1 - x},
        {'type': 'ineq', 'fun': lambda x: x}]

def mainCO(p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23,values0,h):

    nStage = int(timeF/h)
    timeStage = np.linspace(timeI, timeF, nStage+1)
    w0 = np.zeros((nStage, 1))  

    res = minimize(objective, w0, method='SLSQP', constraints=cons, args=(p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23,values0,nStage,timeStage))

    dispopt(values0,nStage,timeStage,res.x,p12,p21,p31,p34,d1,d2,d3,d4,alpha,beta,d13,d23)