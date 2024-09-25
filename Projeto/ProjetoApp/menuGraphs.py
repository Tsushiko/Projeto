from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt

def GerarUm(C,time,name):
  plt.plot(time,C,'b-',label='A(t)')
  plt.title("Evolução de " + name, loc = 'left')
  plt.ylabel('Valores')
  plt.xlabel('Tempo')
  plt.show()

def GerarTodos(A,R,S,I,time):
  figure, axis = plt.subplots(2, 2)
  axis[0,0].plot(time, A, 'b-', label='A(t)')
  axis[0,0].set_title("Evolução das células A")
  axis[0,1].plot(time, R, 'r-', label='R(t)')
  axis[0,1].set_title("Evolução das células R")
  axis[1,0].plot(time, S, 'g-', label='S(t)')
  axis[1,0].set_title("Evolução das células S")
  axis[1,1].plot(time, I, 'y-', label='I(t)')
  axis[1,1].set_title("Evolução das células I")
  plt.show()

def graphsCO(A,R,S,I,X,time):
  root = Tk()
  root.title("MenuGraphs")
  root.geometry("290x240")

  buttonA=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células A", 
                    command=lambda: GerarUm(A,time,"A")).grid(row=0,column=0)
  buttonR=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células R", 
                    command=lambda: GerarUm(R,time,"R")).grid(row=1,column=0)
  buttonS=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células S", 
                    command=lambda: GerarUm(S,time,"S")).grid(row=2,column=0)
  buttonI=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células I", 
                    command=lambda: GerarUm(I,time,"I")).grid(row=3,column=0)
  buttonX=Button(root, height=2, width=40, text="Gerar gráfico de evolução de X", 
                    command=lambda: GerarUm(X,time,"X")).grid(row=4,column=0)
  buttonAll=Button(root, height=2, width=40, text="Gerar gráfico todas as células", 
                    command=lambda: GerarTodos(A,R,S,I,time)).grid(row=5,column=0)
  root.mainloop()

def graphs(A,R,S,I,time):
  root = Tk()
  root.title("MenuGraphs")
  root.geometry("280x210")

  buttonA=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células A", 
                    command=lambda: GerarUm(A,time,"A")).grid(row=0,column=0)
  buttonR=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células R", 
                    command=lambda: GerarUm(R,time,"R")).grid(row=1,column=0)
  buttonS=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células S", 
                    command=lambda: GerarUm(S,time,"S")).grid(row=2,column=0)
  buttonI=Button(root, height=2, width=40, text="Gerar gráfico de evolução das células I", 
                    command=lambda: GerarUm(I,time,"I")).grid(row=3,column=0)
  buttonAll=Button(root, height=2, width=40, text="Gerar gráfico todas as células", 
                    command=lambda: GerarTodos(A,R,S,I,time)).grid(row=5,column=0)
  root.mainloop()
