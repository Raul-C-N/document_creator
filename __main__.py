import sys
import os
from peticionantes import peticionantes_list
from requeridos import requeridos_list
from modelos_doc import *

#funcao adicionar peticionantes
def incluir_peticionante():
    """Adiciona nomes na lista de peticionantes
    """
    print('Insira o nome do peticionante:')
    new_peticionante = input(str)
    peticionantes_list.append(new_peticionante)
    print('Adicionado, ' + new_peticionante)
    print (peticionantes_list)
    
#funcao adicionar requeridos
def incluir_requerido():
    """Adiciona nomes na lista de requeridos
    """
    print('Insita o nome do requerido:')
    new_requerido = input(str)
    requeridos_list.append(new_requerido)
    print('Adicionado, ' + new_requerido)
    print (requeridos_list)
#funcao reset todas as listas
def reset_listas():
    peticionantes_list=[]
    requeridos_list=[] ##nao funciona - voltar depois
#funcao listar os peticionantes
def listar_peticionantes():
    print('A lista de peticionantes contém os seguintes itens: ')
    for i in peticionantes_list:
        if i != peticionantes_list[len(peticionantes_list)-1]:
            print(i+';')
        else:
            print(i+'.')
#funcao listar os requeridos
def listar_requeridos():
    print('A lista de requeridos contém os seguintes itens: ')
    for i in requeridos_list:
        if i != requeridos_list[len(requeridos_list)-1]:
            print(i+';')
        else:
            print(i+'.')

    
#MODELOS DE DOCUMENTOS (modelos_doc.py)

#funcao para ler o modelo

#funcao para selecionar o peticionante

#funcao para selecionar o requerido


##############################
#test area
"""with open('readme.txt', 'w') as f:
    f.write('readme')
###abrir arquivo txt ou modelo de texto    
f = open(PATH,'r')"""
