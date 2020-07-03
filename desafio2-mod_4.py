#Desafio 2 - Criando Diretórios
import os

class Bot:
    def __init__(self):
        pass
    
    def criarDiretorio(self,nome):
        if  not os.path.isdir(nome):
            os.mkdir(nome)
        else:
            print('O diretório já foi criado')
        
    def criarDiretorios(self,nome1,nome2):
        caminho = nome1 + os.sep + nome2
        if  not os.path.isdir(caminho):
            os.makedirs(caminho)
        else:
            print('O diretório já foi criado')  

    def acessandoDiretorio(self,endereco):
        os.chdir(endereco)

bot = Bot()  
bot.criarDiretorio('Arquivos')
bot.acessandoDiretorio('Arquivos')
bot.criarDiretorio('Arquivos pdf')
bot.criarDiretorios('Fotos','Fotos de verão')



