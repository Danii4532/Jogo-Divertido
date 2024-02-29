#criar um jogo de pedra, papel, tesoura 
from PIL import ImageTk
from tkinter import *
import tkinter
import time
import random
global lista_jogador
global lista_computador
#lista para adicionar quantas vezes computador venceu
lista_computador=['']

#lista para adicionar quantas vezes jogador venceu
lista_jogador=['']

#lista para adicionar o historico de jogadas de cada um
lista_jogadas = []

global lista_jogador_novo
global lista_computador_novo
lista_computador_novo = 0
lista_jogador_novo = 0

def jogo_com_interface():
    def analise_vencedor():
        
        escolhido = escolha_computador.cget("text")
        vcomputador = 'COMPUTADOR VENCEU'
        vjogador = 'JOGADOR VENCEU'
        resultado1 = resultado.cget("text")
        global op
        
        op = 1

        if resultado1 == 'PEDRA':
            if escolhido == 'TESOURA':
                vencedor.config(text=vjogador,height=1,font=('Arial black',16))
                lista_jogador.append('1')
                lista_jogadas.append('jogador: '+str(resultado1)+' Computador: '+ str('TESOURA'))
                
            elif escolhido == 'PEDRA':
                vencedor.config(text='EMPATE')
                lista_jogadas.append('jogador: '+str('EMPATE')+' Computador: '+ str('EMPATE'))
                
            elif escolhido == 'PAPEL':
                vencedor.config(text=vcomputador,height=1,font=('Arial black',16))
                lista_jogadas.append('jogador: '+str(resultado1)+' Computador: '+ str('PAPEL'))
                lista_computador.append('1')
                
        elif resultado1 == 'PAPEL':
            if escolhido == 'TESOURA':
                vencedor.config(text=vcomputador,height=1,font=('Arial black',16))
                lista_jogadas.append('jogador: '+str(resultado1)+' Computador: '+ str('TESOURA'))
                lista_computador.append('1')
                
            elif escolhido == 'PEDRA':
                vencedor.config(text=vjogador,height=1,font=('Arial black',16))
                lista_jogadas.append('jogador: '+str(resultado1)+' Computador: '+ str('PEDRA'))
                lista_jogador.append('1')
                
            elif escolhido == 'PAPEL':
                vencedor.config(text='EMPATE')
                lista_jogadas.append('jogador: '+str('EMPATE')+' Computador: '+ str('EMPATE'))
                
        elif resultado1 == 'TESOURA':
            if escolhido == 'TESOURA':
                vencedor.config(text='EMPATE')
                lista_jogadas.append('jogador: '+str('EMPATE')+' Computador: '+ str('EMPATE'))
                
            elif escolhido == 'PEDRA':
                vencedor.config(text=vcomputador,height=1,font=('Arial black',16))
                lista_jogadas.append('jogador: '+str(resultado1)+' Computador: '+ str('PEDRA'))
                lista_computador.append('1')
                
            elif escolhido == 'PAPEL':
                vencedor.config(text=vjogador,height=1,font=('Arial black',16))      
                lista_jogadas.append('jogador: '+str(resultado1)+' Computador: '+ str('PAPEL'))
                lista_jogador.append('1')
      
        pedra.config(state=ACTIVE)
        papel.config(state=ACTIVE)
        tesoura.config(state=ACTIVE)  
 
        tentar_denovo()
            
    def limpar_campos():
        resultado.config(text='')
        escolha_computador.config(text='')
        vencedor.config(text='')
        
    
    def escolha_jogador(escolha):
        
        resultado.config(text=escolha,font=('Arial',16))
        resultado.place(x=100, y=90)
        pedra.config(state=DISABLED)
        papel.config(state=DISABLED)
        tesoura.config(state=DISABLED)
        
        if resultado != '':
            Escolha_computador()
        else:
            pass 
        
    def Escolha_computador():
        lista = ['PEDRA','PAPEL','TESOURA']
        escolhido = random.choice(lista)
        for _ in range(10):
            escolha_computador.config(text=random.choice(lista),font=('Arial',16))
            janela.update()
            time.sleep(0.1)
        escolha_computador.config(text=escolhido,font=('Arial',16))

        if escolha_computador != '' and resultado != '':
            analise_vencedor()                      
              
    
    def Novajanela():
        
        global janela_historico
        janela_historico = tkinter.Tk()
        janela_historico.geometry('350x500')
        janela_historico.title('Histórico de Jogadas')
        janela_historico.minsize(350,500)
        janela_historico.maxsize(350,500)


        cor = 'green'
        janela_historico.config(background=cor)
        
        computador1 = tkinter.Label(janela_historico, text='COMPUTADOR',font=('Arial black',16))
        computador1.config(background=cor)
        computador1.place(x=4,y=10)
        
        jogador1 = tkinter.Label(janela_historico,text='JOGADOR',font=('Arial black',16))
        jogador1.config(background=cor)
        jogador1.place(x=210,y=10)
        
        
        texto_computador = tkinter.Label(janela_historico,text=lista_computador_novo, font=('Arial',24))
        texto_computador.place(x=80,y=40)
        texto_computador.config(background=cor)
        
        
        texto_jogador = tkinter.Label(janela_historico,text=lista_jogador_novo, font=('Arial',24))
        texto_jogador.config(background=cor)
        texto_jogador.place(x=260,y=40)
        
        x1 = 5
        y1 = 60
        jogadas = tkinter.Label(janela_historico,text='ÚLTIMAS JOGADAS',font=('Arial',16),background=cor)
        jogadas.place(x=70,y=100)
        
        rolagem = Scrollbar(janela_historico, orient='vertical')
        rolagem.pack(side='right', fill='y')

        # Criando um widget Listbox para exibir as últimas jogadas
        lista_jogadas1 = tkinter.Listbox(janela_historico, yscrollcommand=rolagem.set, width=33, height=22,background='green',bd='1',highlightbackground='green',font=('Arial black',11))
        lista_jogadas1.place(x=1, y=140)

        # Associando a barra de rolagem à Listbox
        rolagem.config(command=lista_jogadas1.yview)
        tamanho = str(len(lista_jogadas))
        for j in range(len(lista_jogadas)):
            lista_jogadas1.insert(tkinter.END,f'{j+1}° partida: ', lista_jogadas[j])
            lista_jogadas1.insert(tkinter.END, '\n')
            
       
        janela_historico.mainloop()
  
    janela = tkinter.Tk()
    janela.geometry('350x530')
    janela.minsize(350,530)
    janela.maxsize(350,500)
    janela.title('PEDRA, PAPEL, TESOURA')
    cor_fundo = '#19b52c'
    janela.config(background=cor_fundo)
    pedra1 = tkinter.Label(janela,text='PEDRA')
    pedra1.config(background=cor_fundo,font=('Arial Black',18))
    pedra1.place(x=10,y=2)
    
    papel1 = tkinter.Label(janela,text='PAPEL')
    papel1.config(background=cor_fundo,font=('Arial Black',18))
    papel1.place(x=115,y=35)
    
    tesoura1 = tkinter.Label(janela,text='TESOURA')
    tesoura1.config(background=cor_fundo,font=('Arial Black',18))
    tesoura1.place(x=200,y=2)
    
    resultado = tkinter.Label(janela,text='',font=('Arial',16))
    resultado.config(width=10,height=1)
    resultado.place(x=100,y=90)
    
    escolher = tkinter.Label(janela,text='Escolha uma opção',font=('Arial black',16),background=cor_fundo)
    escolher.place(x=60,y=140)
    
    papel = tkinter.Button(janela,text='PAPEL' ,command= lambda: escolha_jogador('PAPEL'),font=('Arial',16))
    papel.place(x=10,y=190)
    
    pedra = tkinter.Button(janela,text='PEDRA',command= lambda: escolha_jogador('PEDRA'),font=('Arial',16))
    pedra.place(x=120,y=190)
    
    tesoura = tkinter.Button(janela,text='TESOURA',command= lambda: escolha_jogador('TESOURA'),font=('Arial',16))
    tesoura.place(x=230,y=190)
    
    computador = tkinter.Label(janela,text='COMPUTADOR')
    computador.config(font=('Arial',16))
    computador.place(x=10,y=260)
    
    escolha_computador = tkinter.Label(janela,text='',width=20)
    escolha_computador.config(font=('Arial',16))
    escolha_computador.place(x=180,y=260)
    
    exibir_vencedor =  tkinter.Label(janela,text='VENCEDOR',font=('Arial Black',16))
    exibir_vencedor.config(background=cor_fundo)
    exibir_vencedor.place(x=100,y=290)
    
    vencedor = tkinter.Label(janela,text='',width=20)
    vencedor.config(height=1,font=('Arial black',16),background='yellow')
    vencedor.place(x=20,y=330)
        
    def sair():
        exit()
        
    def tentar_denovo():    
        tentar = tkinter.Label(janela,text='Deseja Tentar Novamente',font=('Arial Black',16))
        tentar.config(background=cor_fundo)
        global tentar_sim
        global tentar_nao
        tentar.place(x=20,y=370)
        tentar_sim = tkinter.Button(janela,text='SIM',font=('Arial',16),command=limpar_campos)
        tentar_sim.place(x=70,y=410)
        tentar_nao = tkinter.Button(janela,text='NÃO',font=('Arial',16),command=sair)
        
        global lista_jogador_novo
        global lista_computador_novo
        
        lista_computador_novo = sum(int(x) for x in lista_computador if x.isdigit())
        lista_jogador_novo = sum(int(x) for x in lista_jogador if x.isdigit())
        tentar_nao.place(x=190,y=410)
        
        exibir_historico = tkinter.Button(janela,text='HISTÓRICO',command=Novajanela,font=('Arial black',16))
        exibir_historico.place(x=90,y=470)    
    
    janela.mainloop()
    
    
    
jogo_com_interface()
