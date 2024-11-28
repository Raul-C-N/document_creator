import os
from peticionantes import peticionantes_list 
from requeridos import requeridos_list

#funcao pegar nomes peticionantes

#funcao pegar nomes requeridos

#funcao entregar nome peticionantes

#funcao entregar nomes requeridos

#funcao adicionar peticionantes
def incluir_peticionante():
    
    print('Insita o nome do peticionante:')
    new_peticionante = input(str)
    peticionantes_list.append(new_peticionante)
    print('Adicionado, ' + new_peticionante)
    print (peticionantes_list)
    
#funcao adicionar requeridos
    #normatizar como str
def incluir_requerido():
    
    print('Insita o nome do requerido:')
    new_requerido = input(str)
    requeridos_list.append(new_requerido)
    print('Adicionado, ' + new_requerido)
    print (requeridos_list)
#funcao reset todas as listas
def reset_listas()
    peticionantes_list = []
    requeridos_list = []

##############################
#test area