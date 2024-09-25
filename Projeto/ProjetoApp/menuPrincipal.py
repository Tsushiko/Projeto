from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from simulationRunner import main
from simulationRunnerCO import mainCO

import warnings
warnings.filterwarnings("error")

values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def retrieve():
    inputValue=text.get("1.0","end-1c")
    values[0] = float(inputValue)
    inputValue=text1.get("1.0","end-1c")
    values[1] = float(inputValue)
    inputValue=text2.get("1.0","end-1c")
    values[2] = float(inputValue)
    inputValue=text3.get("1.0","end-1c")
    values[3] = float(inputValue)
    inputValue=text4.get("1.0","end-1c")
    values[4] = float(inputValue)
    inputValue=text5.get("1.0","end-1c")
    values[5] = float(inputValue)
    inputValue=text6.get("1.0","end-1c")
    values[6] = float(inputValue)
    inputValue=text7.get("1.0","end-1c")
    values[7] = float(inputValue)
    inputValue=text8.get("1.0","end-1c")
    values[8] = float(inputValue)
    inputValue=text9.get("1.0","end-1c")
    values[9] = float(inputValue)
    inputValue=text10.get("1.0","end-1c")
    values[10] = float(inputValue)
    inputValue=text11.get("1.0","end-1c")
    values[11] = float(inputValue)
    inputValue=text12.get("1.0","end-1c")
    values[12] = float(inputValue)
    inputValue=text13.get("1.0","end-1c")
    values[13] = float(inputValue)
    inputValue=text14.get("1.0","end-1c")
    values[14] = float(inputValue)
    inputValue=text15.get("1.0","end-1c")
    values[15] = float(inputValue)
    inputValue=text16.get("1.0","end-1c")
    values[16] = float(inputValue)
    inputValue=text17.get("1.0","end-1c")
    values[17] = float(inputValue)

def simulateCO():
    global values
    retrieve()
    try:
        mainCO(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11], [values[12],values[13],values[14],values[15],values[16]],values[17])
    except Warning:
        messagebox.showwarning( "!!ERRO!!", "Não foi possível criar a simulação, verifique novamente os valores inseridos.")
    values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def simulate():
    global values
    retrieve()
    try:
        main(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[10],values[11],[values[12],values[13],values[14],values[15]])
    except Warning:
        messagebox.showwarning( "!!ERRO!!", "Não foi possível criar a simulação, verifique novamente os valores inseridos.")
    values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


root = Tk()
root.title("MenuInputs")
root.geometry("1100x600")

label = Label(root, text="----------- INFO -----------", font = "Verdana 10 bold")
label.grid(row=14,column=3)
label = Label(root, text="Variáveis começando por p indicam valores de proliferação", font = "Verdana 7")
label.grid(row=15,column=3)
label = Label(root, text="Variáveis começando por d indicam valores de destruição", font = "Verdana 7")
label.grid(row=16,column=3)
label = Label(root, text="Os números encontrados nos nomes das variáveis representam entre que células está a haver interação", font = "Verdana 7")
label.grid(row=17,column=3)
label = Label(root, text="A relação dos números para as células é a seguinte:", font = "Verdana 7")
label.grid(row=18,column=3)
label = Label(root, text="1 - A, 2 - R, 3 - S, 4 - I", font = "Verdana 7")
label.grid(row=19,column=3)
label = Label(root, text="* Apenas afetam a simulação com controlo ótimo", font = "Verdana 7", foreground= "blue")
label.grid(row=20,column=3)

label = Label(root, text="Valor de p12: ", font = "Verdana 10")
label.grid(row=0,column=0)

text = Text(root,height=2,width=10)
text.insert('1.0', '1')
text.grid(row=0,column=1)

label = Label(root, text="Valor de p21: ", font = "Verdana 10")
label.grid(row=1,column=0)

text1 = Text(root,height=2,width=10)
text1.insert('1.0', '19')
text1.grid(row=1,column=1)

label = Label(root, text="Valor de p31: ", font = "Verdana 10")
label.grid(row=2,column=0)

text2 = Text(root,height=2,width=10)
text2.insert('1.0', '20')
text2.grid(row=2,column=1)

label = Label(root, text="Valor de p34: ", font = "Verdana 10")
label.grid(row=3,column=0)

text3 = Text(root,height=2,width=10)
text3.insert('1.0', '0.05')
text3.grid(row=3,column=1)

label = Label(root, text="Valor de d13: ", font = "Verdana 10")
label.grid(row=4,column=0)

text10 = Text(root,height=2,width=10)
text10.insert('1.0', '0.45')
text10.grid(row=4,column=1)

label = Label(root, text="Valor de d23: ", font = "Verdana 10")
label.grid(row=5,column=0)

text11 = Text(root,height=2,width=10)
text11.insert('1.0', '0.01')
text11.grid(row=5,column=1)

label = Label(root, text="Valor de d1: ", font = "Verdana 10")
label.grid(row=6,column=0)

text4 = Text(root,height=2,width=10)
text4.insert('1.0', '0.001')
text4.grid(row=6,column=1)

label = Label(root, text="Valor de d2: ", font = "Verdana 10")
label.grid(row=7,column=0)

text5 = Text(root,height=2,width=10)
text5.insert('1.0', '0.001')
text5.grid(row=7,column=1)

label = Label(root, text="Valor de d3: ", font = "Verdana 10")
label.grid(row=8,column=0)

text6 = Text(root,height=2,width=10)
text6.insert('1.0', '0.001')
text6.grid(row=8,column=1)

label = Label(root, text="Valor de d4: ", font = "Verdana 10")
label.grid(row=9,column=0)

label = Label(root, text="*", font = "Verdana 10", foreground= "blue")
label.grid(row=9,column=2)

text7 = Text(root,height=2,width=10)
text7.insert('1.0', '1')
text7.grid(row=9,column=1)

label = Label(root, text="Valor de alpha: ", font = "Verdana 10")
label.grid(row=10,column=0)

label = Label(root, text="*", font = "Verdana 10", foreground= "blue")
label.grid(row=10,column=2)

text8 = Text(root,height=2,width=10)
text8.insert('1.0', '1')
text8.grid(row=10,column=1)

label = Label(root, text="Valor de beta: ", font = "Verdana 10")
label.grid(row=11,column=0)

label = Label(root, text="*", font = "Verdana 10", foreground= "blue")
label.grid(row=11,column=2)

text9 = Text(root,height=2,width=10)
text9.insert('1.0', '1')
text9.grid(row=11,column=1)

label = Label(root, text="Valores iniciais: ", font = "Verdana 10")
label.grid(row=0,column=5)

label = Label(root, text="A: ", font = "Verdana 10")
label.grid(row=1,column=4)

text12 = Text(root,height=2,width=10)
text12.insert('1.0', '0.01')
text12.grid(row=1,column=5)

label = Label(root, text="R: ", font = "Verdana 10")
label.grid(row=2,column=4)

text13 = Text(root,height=2,width=10)
text13.insert('1.0', '0.01')
text13.grid(row=2,column=5)

label = Label(root, text="S: ", font = "Verdana 10")
label.grid(row=3,column=4)

text14 = Text(root,height=2,width=10)
text14.insert('1.0', '0.01')
text14.grid(row=3,column=5)

label = Label(root, text="I: ", font = "Verdana 10")
label.grid(row=4,column=4)

text15 = Text(root,height=2,width=10)
text15.insert('1.0', '0.001')
text15.grid(row=4,column=5)

label = Label(root, text="Y: ", font = "Verdana 10")
label.grid(row=5,column=4)

text16 = Text(root,height=2,width=10)
text16.insert('1.0', '0')
text16.grid(row=5,column=5)

label = Label(root, text="*", font = "Verdana 10", foreground= "blue")
label.grid(row=5,column=6)

label = Label(root, text="Nível de precisão (h): ", font = "Verdana 10")
label.grid(row=10,column=4)

text17 = Text(root,height=2,width=10)
text17.insert('1.0', '0.5')
text17.grid(row=10,column=5)

label = Label(root, text="*", font = "Verdana 10", foreground= "blue")
label.grid(row=10,column=6)


buttonCO=Button(root, height=2, width=40, text="Simular com controlo ótimo", 
                        command=lambda: simulateCO()).grid(row=5,column=3)
button=Button(root, height=2, width=40, text="Simular sem controlo ótimo", 
                        command=lambda: simulate()).grid(row=7,column=3)
root.mainloop()

