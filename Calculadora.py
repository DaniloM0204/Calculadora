from tkinter import *
"Times New Roman" == "TNR"

class App:
    def __init__(self,master = None):
        self.master = master
        self.master.title("Calculadora Básica") #Título da calculadora
        self.master.geometry("400x500") # Tamanho
        self.master.configure(bg = "#f0f0f0")

        # Criando os widgets
        self.criar_widget()

    def criar_widget(self):
        #Criando a tela
        self.tela =  Entry(self.master,
                           width=20,
                           font=("TNR", 20),
                           justify="left",
                           bd = 10,
                           relief=RIDGE,
                           fg="#00fc22",
                           bg="#000000")
        self.tela.grid(row=0,
                       column=0,
                       columnspan=4,
                       padx=30,
                       pady=30)

        # Botões
        botoes = ['7','8','9','/',
                  '4','5','6','*',
                  '1','2','3','-',
                  '0','.','=','+']

        # Posicionando botões
        linha = 1
        coluna = 0
        for botao in botoes:
            if botao == '=':
                Button(self.master,
                        text=botao,
                        width=10,
                        height=2,
                        font = ("TNR",14,"bold"),
                        fg="black",
                        command=self.calcular).grid(row=linha,
                                                    column=coluna,
                                                    columnspan=2)
                coluna += 1
            else:
                Button(self.master,
                       text=botao,
                       width=5,
                       height=2,
                       font = ("TNR",14,"bold"),
                       bg="#f0f0f0",
                       command=lambda b=botao: self.add_caractere(b)).grid(row=linha, column=coluna)
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1
        # Limpando a tela
        Button(self.master,text="Limpar", width=8,height=4,command=self.limpar).grid(row=linha,column=coluna)

    def add_caractere(self,c):
        self.tela.insert(END,c)

    def calcular(self):
        try: # Analisa expressão e exibe resultado
                resultado = eval(self.tela.get())
                self.tela.delete(0,END)
                self.tela.insert(0,str(resultado))
        except: # Mesagem para erros
                self.tela.delete(0,END)
                self.tela.insert(0,"0/0 ∄")

    def limpar(self): #Limpa oque foi escrito
        self.tela.delete(0,END)


root = Tk() #Permite que os widgets possam ser utilizados
app = App(root) #Parametro do metodo construtor de classe
root.mainloop()
